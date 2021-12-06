import json

"""
    For extracting bulletMoveSpeed from _weapons
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

for i in data:
    if ('bulletMoveSpeed' in i):
        id = i['inventoryID']
        speed = i['bulletMoveSpeed']

        print(f"{id} | {speed}")
        d[id] = speed

print('---')
print(d)
