import json

"""
    For extracting bulletMoveSpeed from _weapons

    Update: Can also be used for other different keys
"""

def readFile(p: str, encoding='utf-8'):
    try:
        with open(p, 'r', encoding=encoding) as f:
            return f.read()
    except Exception as e:
        print(e)
        return None


content = readFile('_weapons')
data = json.loads(content)

print(len(data))

d = {}

key = 'clipSize'

for i in data:
    if (key in i):
        id = i['inventoryID']
        value = i[key]

        print(f"{id} | {value}")
        d[id] = value

print('---')
print(d)
