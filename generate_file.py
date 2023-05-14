import requests
import os
import six
import csv
def download_json(url):
    try:
        return requests.get(url).json()
    except requests.exceptions.RequestException as e:
        raise Exception("Unable to read JSON file {}".format(e))

def write_properties(filename, dictionary, delimiter='='):
    ''' Writes the provided dictionary in key sorted order to a properties
        file with each line in the format: key<delimiter>value
            filename -- the name of the file to be written
            dictionary -- a dictionary containing the key/value pairs.
    '''
    open_kwargs = {'mode': 'w', 'newline': ''} if six.PY3 else {'mode': 'wb'}
    with open(filename, **open_kwargs) as csvfile:
        writer = csv.writer(csvfile, delimiter=delimiter, escapechar='\\',
                            quoting=csv.QUOTE_NONE)
        writer.writerows(sorted(dictionary.items()))
stack = "" # your choice
url = VOT_DATASETS[stack]
meta = download_json(url)
root = '' # your choice
for sequence in meta["sequences"]:
    sequence_directory = os.path.join(root, sequence['name'])
    write_path = os.path.join(sequence_directory, 'sequence')
    if os.path.exists(write_path):
        print(f"{sequence['name']} has existed!")
        continue
    print(f"Writing {sequence['name']}")
    data = {'name': sequence["name"], 'fps': sequence["fps"], 'format': 'default'}
    for cname, channel in sequence["channels"].items():
        if "pattern" in channel:
            data["channels." + cname] = cname + os.path.sep + channel["pattern"]
        else:
            data["channels." + cname] = cname + os.path.sep
    write_properties(write_path, data)
with open(os.path.join(root, "list.txt"), "w") as fp:
    for sequence in meta["sequences"]:
        fp.write('{}\n'.format(sequence["name"]))

