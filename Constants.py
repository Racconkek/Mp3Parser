import json

with open('genres.json', 'r', encoding='utf-8') as f:
    GENRES = json.load(f)

with open('tags.json', 'r', encoding='utf-8') as f:
    TAG_NAMES_TO_DESCRIPTION = json.load(f)


