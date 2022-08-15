import sys
import engine


if len(sys.argv) > 3:
    print('Wrong arguments.', len(sys.argv))
    sys.exit(0)

start_num = 0
end_num = engine.current_counter()

if len(sys.argv) == 2:
    start_num = int(sys.argv[1])

if len(sys.argv) == 3:
    start_num = int(sys.argv[1])
    end_num = int(sys.argv[2])

engine.show_records(start_num, end_num)

