
time_list = [86400, 3600, 60, 1]
title_list = ['дн', 'час', 'мин', 'сек']

duration = int(input('Введите время в секундах: '))

for i in range(len(time_list)):
    cur_time = duration // time_list[i]
    print(cur_time, title_list[i],  end=' ')
    duration -= cur_time * time_list[i]