import re


def email_parse(email_str):
    re_pattern = r"^(\w+)([@])(\w+\.\w+)"

    # re_email = re.compile(re_pattern)
    re_group = re_email.findall(email_str)
    if re_group:
        return {'username': re_group[0][0], 'domain:': re_group[0][2]}
    else:
        raise ValueError(f'Wrong email: {email_str}')


try:
    print(email_parse("qeqwewe@qwe1qwewqe.we"))
except ValueError as e:
    print(e.args)

try:
    print(email_parse("qweqw@we$1we.we"))
except ValueError as e:
    print(e.args)

try:
    print(email_parse("s&df1sdfsdf@sadf.ru"))
except ValueError as e:
    print(e.args)

try:
    print(email_parse("wewe_wwerwer@kasdf.ru"))
except ValueError as e:
    print(e.args)


