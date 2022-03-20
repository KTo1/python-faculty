import sys
import engine


if len(sys.argv) != 2:    
    print('Wrong arguments.', len(sys.argv))
    sys.exit(0)

engine.add_record(sys.argv[1])

