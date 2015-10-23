from collections import Counter
from mixpanel_export import EventStream

api_key = '...'
api_secret = '...'

es = EventStream(api_key, api_secret)

params = {
	'event': ["A"],
    'from_date': '...',
    'to_date': '...',
    'where': 'property["B"] == "2"'
}

count = Counter()


def do_count(e):
	count[e['properties']['C']] += 1

total = es.request(params, do_count)
print("Total events processed %s, tally: %s" % (total, count))