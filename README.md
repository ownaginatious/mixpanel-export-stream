# mixpanel-export-stream

A small Python library for exporting and reading raw event data from Mixpanel while taking advantage of the streamable JSONLine data format.

This library is based on the Mixpanel's own data export library found [here](https://mixpanel.com/docs/api-documentation/data-export-api#libs-python).

## What do you mean by a "stream"?

Mixpanel's raw event data API returns data in JSONLine format, meaning each event is a JSON object on its own line.

Mixpanel gives a warning to **not** attempt to read this data until it has downloaded in its entirety due to being zipped in `gzip` format, but this compression type is streamable, meaning it shouldn't matter.

Streaming reduces the footprint in RAM significantly as compared to Mixpanel's own Python API implementation when you only care about doing reduces over events.

## Example

Let's assume we want to get all events 'A' with a property 'B' that is equal to "2". Events 'A' also have a property 'C', which is some random string value. We want the results grouped and tallied by 'C' to see how many property 'C' events occurred.

This is simple and fast to do with this library.

```python
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
```
