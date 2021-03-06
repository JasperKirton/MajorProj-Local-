import json

# Sequentially store review text data for model

data = json.loads(review_string)

for entry in data['reviews']:
    del entry['user']

new_string = json.dumps(data, indent=2, sort_keys=True)

print(new_string)

# Get artist from id

artist_id = "c5c2ea1c-4bde-4f4d-bd0b-47b200bf99d6"
try:
    result = musicbrainzngs.get_artist_by_id(artist_id)
except WebServiceError as exc:
    print("Something went wrong with the request: %s" % exc)
else:
    artist = result["artist"]
    print("name:\t\t%s" % artist["name"])
    print("sort name:\t%s" % artist["sort-name"])

