import csv
import json

from more_itertools import unique_everseen

with open('C:\Suraj\Work_Infa\Projects\India\Schlumberger\Misc\\test.json') as json_file:
    data = json.load(json_file)


def get_links(obj, indices):
    for k, v in obj.items() if isinstance(obj, dict) else enumerate(obj):
        if isinstance(v, (dict, list)) :
            yield from get_links(v, indices + [k])
        else:
            yield indices + [k]


with open('C:\Suraj\Work_Infa\Projects\India\Schlumberger\Misc\\links1.csv', 'w+', newline='') as linksfile:
    writer1 = csv.writer(linksfile)
    writer1.writerow(['association', 'fromObjectIdentity', 'toObjectIdentity'])

    for a in get_links(data, []):
        r = 0
        no_integers = [x for x in a if not isinstance(x, int)]

        l = len(no_integers)
        # print(l)
        if (no_integers[0] == 'paginationmetadata' or no_integers[0] == 'links'):
            pass
        else:
            while (r < l - 1):
                # print(no_integers[r],no_integers[r+1])
                writer1.writerow(['com.slb.custom.api.fdp.APIField', no_integers[r], no_integers[r + 1]])
                r += 1

with open('C:\Suraj\Work_Infa\Projects\India\Schlumberger\Misc\\links1.csv', 'r') as f1, open(
        'C:\Suraj\Work_Infa\Projects\India\Schlumberger\Misc\\links.csv', 'w+') as f2:
    f2.writelines(unique_everseen(f1))


def show_indices(obj, indices):
    for k, v in obj.items() if isinstance(obj, dict) else enumerate(obj):
        if isinstance(v, (dict, list)):
            yield from show_indices(v, indices + [k])
            if (k == 0):
                break
        else:
            yield indices + [k]


t2 = []
t3 = []
for keys in show_indices(data, []):
    for k in keys:
        t2.append(k)
for i in t2:
    if i not in t3:
        t3.append(i)

parsed_data = data['value']
t4 = []

for d in parsed_data:
    t4 = list(d.keys())
for j in t4:
    if j not in t3:
        t3.append(j)
print(t3)

with open('C:\Suraj\Work_Infa\Projects\India\Schlumberger\Misc\\objects.csv', 'w+', newline='') as objectsfile:
    writer = csv.writer(objectsfile)
    writer.writerow(['class', 'identity', 'core.name', 'core.description', 'com.slb.custom.api.fdp.URL'])
    writer.writerow(['com.slb.custom.api.fdp.System', 'S1', 'FDP', 'FDP API', 'www.google.com'])
    for i in t3:
        if str(i) != '0' and str(i) != 'value':
            writer.writerow(['com.slb.custom.api.fdp.APIField', i, i, 'API Field', ''])
