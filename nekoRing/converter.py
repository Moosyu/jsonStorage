import json
import re

def parse_js_to_json(js_content):
    # this pattern matches sites = []. the var is looking for variables and the s+ matches for one or more spaces
    # the \s* allows for spaces around the =. the \[(.*?)\] is getting the actual list of sites
    # the \[ and \] match for any square brackets opening and closing the sites array
    # (.*?) matches everything between the square brackets
    # the ; is just matching for the semi colon at hte end of javascripts
    # re.DOTALL lets the pattern go through many lines
    sites_match = re.search(r'var\s+sites\s*=\s*\[(.*?)\];', js_content, re.DOTALL)
    if not sites_match:
        raise ValueError("sites isnt in the js file loaded !!")
    
    # sites_match_group(1) is grabbing the regex group, the 1 is just the group number even tho we only have 1 group anyways.
    # strip is removing whitespace 
    sites_cleaned = sites_match.group(1).strip()
    
    # this is going through the cleaned data and pulling every singular site.
    # [^\]]* is matching for everythingb but the closing square bracket
    # (* just means everything)
    sites_entries = re.findall(r'\[([^\]]*)\]', sites_cleaned, re.DOTALL)

    json_data = []

    for entry in sites_entries:
        #this is matching everything between double squotes
        # the .*? is so it works if there are two sets of double quotes
        sites = re.findall(r'"(.*?)"', entry)

        # skips over things that dont have urls
        if len(sites) < 1:
            continue
        
        # grabbing the url (because the url is always first) and getting rid of whitespace
        url = sites[0].strip()

        # getting the name, len(parts) > 1 makes sure there isnt just one part to the entry
        # parts[1].strip() makes sure the name isnt empty
        # parts[1].strip() != "? is making sure the name isnt "?" which is what it seems like they used to name things missing names
        # then name is set to whatever the name is set as without whitespaces
        if len(sites) > 1 and sites[1].strip() and sites[1].strip() != "?":
            name = sites[1].strip()
        else:
            # this is making names from whatever is in between https:// and the first dot
            # it just calls it unknown if it cant do it for some reason
            name_match = re.search(r'https?://(.*?)\.', url)
            name = name_match.group(1) if name_match else "unknown"

        # this is making the description. not really needed yk im just like that
        # len(parts) > 2 is checking if there is a third part (the first part is the url and second is name, 2 because thats just how arrays work)
        # parts[2].strip() makes sure name isnt empty
        # if it cant find anything it makes the desc "n/a", if it can it sets the desc to the desc set in the js file
        desc = sites[2].strip() if len(sites) > 2 and sites[2].strip() else "n/a"

        # this is making the names lowercase and removing anything that isnt numbers and letters
        name = re.sub(r'\W+', '', name.lower())

        # putting the data in a json list
        json_data.append({
            "name": name,
            "desc": desc,
            "url": url
        })

    return json_data

def main():
    with open('onionring-variables.js', 'r', encoding='utf-8') as file:
        js_content = file.read()

    json_data = parse_js_to_json(js_content)

    with open('sitesNekoRing.json', 'w', encoding='utf-8') as json_file:
        json.dump(json_data, json_file, ensure_ascii=False, indent=2)

main()
