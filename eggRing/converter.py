# go to https://eggring.neocities.org/js/eggring-config.js for eggring-config.js
import json
import re

input_js_file = 'eggring-config.js'
output_json_file = 'sitesEggRing.json'

with open(input_js_file, 'r') as file:
    js_content = file.read()

# looks nicer then nekoRings one because eggRing is way more uniform
# this is finding something that looks like new webringMember("", "", "")
# "([^"]+)" looks for the name inside quotes, the [^"]+ matches characters not in double quotes
# \s* matches any whitespace in beetween
# "([^"]*)" matches for the button, the * is here bc button can be empty
# "([^"]+)" same as the first one
site_list_pattern = r'new webringMember\("([^"]+)",\s*"([^"]*)",\s*"([^"]+)"\)'

# gets matches from site_list_pattern
site_list_matches = re.findall(site_list_pattern, js_content)

site_list = []
for name, button, url in site_list_matches:
    # re.sub(r'\W+', '', name.lower()) replaces things that arent part of the alphabet with 'an empty string to get rid of them
    formatted_name = re.sub(r'\W+', '', name.lower())
    site_list.append({
        "name": formatted_name,
        "button": "https://eggring.neocities.org/" + button,
        "url": url
    })

with open(output_json_file, 'w') as json_file:
    json.dump(site_list, json_file, indent=2)