import os
import re
import datetime

PROJECT_FOLDER = os.path.abspath('.')
FILE = os.path.join(PROJECT_FOLDER, 'Apache_logs.txt')

def output(ip_list, safari_count, firefox_count):
    ip_uniqe_list = list(set(ip_list))
    print('Количество уникальных ip-адресов: ', len(ip_uniqe_list))
    print('Количество браузеров Safari: ', safari_count)
    print('Количество браузеров Firefox: ', firefox_count)

def init():
    ip_list = []
    safari_count = 0
    firefox_count = 0
    return ip_list, safari_count, firefox_count

def getTime(line):
    str = line.split()
    time = str[3][1:12]
    time_obj = datetime.datetime.strptime(time, '%d/%b/%Y')
    return str, time, time_obj


def main():
    fp = open(FILE, 'r')
    line = fp.readline()

    while (line != ''):
        ip_list, safari_count, firefox_count = init()
        str, time, time_obj = getTime(line)
        print(time)
        temp = time_obj

        while temp == time_obj:
            ip_list.append(str[0])
            browser = str[len(str)-1]
            if 'Safari' in browser:
                safari_count +=1
            elif 'Firefox' in browser:
                firefox_count += 1

            line = fp.readline()
            if line == '':
                break
            str, _, temp = getTime(line)

        output(ip_list, safari_count, firefox_count)    

    fp.close()


if __name__ == "__main__":
    main()