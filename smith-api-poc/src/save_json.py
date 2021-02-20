import json

def save(text, str_data):
    filename = "{}.json".format(text)
    with open(filename, 'w') as outfile:
        data = json.dumps(str_data, indent=4)
        outfile.write(data)
