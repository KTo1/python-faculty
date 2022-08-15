import os
import sys
import json

if len(sys.argv) > 2:
    print('Wrong arguments.', len(sys.argv))
    sys.exit(0)

root_dir = sys.argv[1]

dict_stat = dict()

for file in os.scandir(root_dir):
    if file.is_dir():
        continue
    key = 10 ** len(str(file.stat().st_size))
    dict_stat.setdefault(key, [0, set()])
    dict_stat[key][0] += 1
    dict_stat[key][1].add(os.path.splitext(file.path)[1])

dict_stat = {k: (v[0], list(v[1])) for k, v in dict_stat.items()}
dict_stat = dict(sorted(dict_stat.items(), key=lambda item: item[0]))

print('File sizes statistic:')
for k, v in dict_stat.items():
    print(f'{k}:{v}')

file_name = os.path.basename(root_dir) + "_summary.json"
with open(file_name, 'w') as f:
    json.dump(dict_stat, f)
    print()
    print(f'Store in file: {file_name}')
