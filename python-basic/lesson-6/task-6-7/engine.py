DB_SUM_LENGTH = 15
DB_NAME = 'bakery_db.csv'
DB_CNT_NAME = 'bakery_db.cnt'


def current_counter():
    with open(DB_CNT_NAME, 'a+', encoding='utf-8') as db_cnt:
        db_cnt.seek(0)
        for line in db_cnt:
            return int(line)

        return 0


def update_counter(new_value):
    with open(DB_CNT_NAME, 'w', encoding='utf-8') as db_cnt:
        db_cnt.write(str(new_value))


def add_record(value):
    new_counter = current_counter() + 1

    with open(DB_NAME, 'a', encoding='utf-8') as db:
        db.write(f'{new_counter};{value.rjust(DB_SUM_LENGTH, " ")}\n')

    update_counter(new_counter)


def edit_record(record_number, new_value):
    str_byte = b''
    new_val_format = f'{new_value.rjust(DB_SUM_LENGTH, " ")}\r\n'

    with open(DB_NAME, 'rb+') as db:
        byte = db.read(1)
        while byte:
            if byte == b'\r':
                db.read(1)
                str_list = (str_byte + b'\r\n').decode().split(';')
                num = int(str_list[0])
                val = str_list[1]
                if num == record_number:
                    db.seek(db.tell() - len(val))
                    db.write(new_val_format.encode('utf-8'))
                    break
                str_byte = b''
            else:
                str_byte += byte

            byte = db.read(1)


def show_records(start_num, end_num):
    with open(DB_NAME, encoding='utf-8') as db:
        for line in db:
            line_list = line.split(';')
            if len(line_list) < 2:
                break
            if start_num <= int(line_list[0]) <= end_num:
                print(line, end='')
