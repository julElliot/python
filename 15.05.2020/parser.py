import os
import re

PROJECT_FOLDER = os.path.abspath('.')
FILE = os.path.join(PROJECT_FOLDER, 'Apache_logs.txt')
print(FILE)

fp = open(FILE, 'r')
strings_count = len(fp.readlines())
print('Количество строк в файле: ', strings_count)
fp.seek(0)

ip_list = []
safari_count = 0
firefox_count = 0
line = fp.readline()
while (line != ''):
    str = line.split()
    ip_list.append(str[0])
    browser = str[len(str)-1]
    if 'Safari' in browser:
        safari_count +=1
    elif 'Firefox' in browser:
        firefox_count += 1
    line = fp.readline()
fp.close()

ip_uniqe_list = list(set(ip_list))
print('Количество уникальных ip-адресов: ', len(ip_uniqe_list))
print('Количество браузеров Safari: ', safari_count)
print('Количество браузеров Firefox: ', firefox_count)