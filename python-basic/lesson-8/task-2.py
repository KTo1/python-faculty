import re
import requests

RE_PATTERN = r'^((?:\w{1,4}.|:)+\w{1,4}).*[\[](\d{1,2}/\w+/\d{4}(?::\d{2}){3} \+0000)[\]] \"([A-Z]+) (.*1[.]1)\" (\d+) (\d+)'
RE_PATTERN = r'([^ \[\"]+ )'

re_email = re.compile(RE_PATTERN)

response = requests.get('https://github.com/elastic/examples/raw/master/Common Data Formats/nginx_logs/nginx_logs')

if not response.status_code == 200:
    print('Could"t get data from service.')
    exit(1)

result = list()
res_list = response.text.split('\n')
for str_res in res_list:
    if not str_res:
        continue
    re_group = re_email.split(str_res.strip())
    if re_group:
        _ = dict()
        _['remote_addr'] = re_group[1]
        _['request_datetime'] = re_group[7]
        _['request_type'] = re_group[11]
        _['requested_resource'] = re_group[13]
        _['response_code'] = re_group[15]
        _['response_size'] = re_group[17]
        result.append(_)


print('All right' if len(res_list) == len(result) else f'Something going wrong ({len(res_list)} {len(result)})')
