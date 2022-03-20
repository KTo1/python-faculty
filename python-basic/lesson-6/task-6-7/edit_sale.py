import sys
import engine


if len(sys.argv) != 3:
    print('Wrong arguments.', len(sys.argv))
    sys.exit(0)

num = int(sys.argv[1])
value = sys.argv[2]

end_num = engine.current_counter()

if num < 1 or num > end_num:
    print('Record number wrong')
    sys.exit(0)

engine.edit_record(num, value)

