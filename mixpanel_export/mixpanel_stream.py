from contextlib import closing
import hashlib
import json
import requests
import time


class EventStream(object):

    ENDPOINT = 'https://data.mixpanel.com/api'
    VERSION = '2.0'

    def __init__(self, api_key, api_secret):

        self.api_key = api_key
        self.api_secret = api_secret

    def request(self, params, handler, expire=600):
        """
        params - Extra parameters associated with method
        handler - A function to handle an incoming json event
        expire - The amount of time to expire a request after in seconds
        """
        params['api_key'] = self.api_key
        params['expire'] = int(time.time()) + expire
        params['format'] = 'json'

        if 'sig' in params:
            del params['sig']

        params['sig'] = self.__hash_args(params)

        request_url = '/'.join([self.ENDPOINT, str(self.VERSION)]) + "/export"

        with closing(requests.get(request_url, params, stream=True)) as s:

            event_count = 0

            for line in s.iter_lines():

                if line.strip() == "":
                    break

                jsonl = json.loads(line.decode('utf-8'))

                if 'properties' not in jsonl:
                    if 'error' in jsonl:
                        raise Exception(jsonl['error'])
                    else:
                        raise Exception(line)

                handler(jsonl)

                event_count += 1

            return event_count

    def _hash_args(self, args):
        """
        Hashes arguments by joining key=value pairs, appending a secret, and
        then taking the MD5 hex digest.
        """
        for a in args:
            if isinstance(args[a], list):
                args[a] = json.dumps(args[a])

        args_joined = "".join([a + '=' + str(args[a])
                              for a in sorted(args.keys())])
        sig_hash = hashlib.md5(args_joined.encode('utf-8'))
        sig_hash.update(self.api_secret.encode('utf-8'))

        return sig_hash.hexdigest()
