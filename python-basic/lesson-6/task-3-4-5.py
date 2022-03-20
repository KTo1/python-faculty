
import sys
from itertools import zip_longest

if len(sys.argv) != 4:
    print('Wrong arguments.', len(sys.argv))
    sys.exit(0)

if sys.argv[1] == sys.argv[3] or sys.argv[2] == sys.argv[3]:
    print('Output file must be different!')
    exit(0)

result = []
with open(sys.argv[1], encoding='utf-8') as uf:
    with open(sys.argv[2], encoding='utf-8') as hf:
        for user, hobby in zip_longest(uf, hf):
            if user is None:
                sys.exit(1)
            result.append(f'{user.rstrip()}: {hobby}')

with open(sys.argv[3], 'w', encoding='utf-8') as uhf:
    uhf.writelines(result)
