
result = []
with open('nginx_logs.txt') as f:
    for line in f:
        current_line_list = line.rstrip().split('-')
        ip_address = current_line_list[0]
        method = current_line_list[2].split(' ')[3][1:]
        resource = current_line_list[2].split(' ')[4]
        result.append((ip_address, method, resource))

dict_req_stat = dict()

for i in result:
    dict_req_stat.setdefault(i[0], 0)
    dict_req_stat[i[0]] += 1

dict_req_stat = sorted(dict_req_stat.items(), key=lambda item: item[1], reverse=True)

print('Spammer detected:',  dict_req_stat[0])
