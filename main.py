# coding=utf-8
"""
@author:'guojie'
@Email:guojie_app@163.com
@createtime:2020/06/02
"""
import datetime
import time


def computing_time(auto_conf):
    now_time = time.strftime("%H:%M:%S", time.localtime())
    left_days = 0
    today = datetime.date.today()
    # print(today)
    # today = "2021-07-31"
    # today = datetime.datetime.strptime(today, "%Y-%m-%d")
    if auto_conf['auto_tag'] == 1:
        if auto_conf['auto_cycle'] == 1:
            left_days = 1
        elif auto_conf['auto_cycle'] == 2:
            auto_rule = auto_conf['auto_date']
            now_mday = time.strftime("%w", time.localtime())
            if now_mday == 0:
                now_mday = 7
            for temp_mday in auto_rule:
                if int(now_mday) <= temp_mday:
                    if int(now_mday) == 7:
                        left_days = int(auto_rule[0])
                    elif int(now_mday) == int(temp_mday):
                        left_days = int(
                            auto_rule[(auto_rule.index(temp_mday) + 1) % len(auto_rule)] - int(now_mday) + (
                                    auto_rule.index(temp_mday) + 1) / len(auto_rule) * 7)
                    elif int(temp_mday) > int(now_mday):
                        left_days = int(temp_mday) - int(now_mday)
                    break
            if not left_days:
                left_days = int(auto_rule[0]) + 7 - int(now_mday)
        elif auto_conf['auto_cycle'] == 3:
            auto_rule = auto_conf['auto_date']
            now_day = time.strftime("%d", time.localtime())
            now_month = time.strftime("%m", time.localtime())
            key_29 = [2]
            key_30 = [4, 6, 9, 11]
            if int(now_month) in key_29:
                key_num = 28
            elif int(now_month) in key_30:
                key_num = 30
            else:
                key_num = 31
            for temp_day in auto_rule:
                if int(now_day) <= temp_day:
                    if int(now_day) == temp_day:
                        left_days = int(
                            auto_rule[(auto_rule.index(temp_day) + 1) % len(auto_rule)] - int(now_day) +
                            int((auto_rule.index(temp_day) + 1) / len(auto_rule)) * key_num)
                    elif int(now_day) < temp_day:
                        left_days = int(temp_day - int(now_day))
                    break
            if not left_days:
                left_days = int(auto_rule[0]) + key_num - int(now_day)
        if now_time > auto_conf['auto_time']:
            nextTime = str(
                today + datetime.timedelta(days=left_days)) + ' ' + auto_conf['auto_time']
        else:
            nextTime = str(datetime.date.today()) + ' ' + auto_conf['auto_time']

        return nextTime


if __name__ == '__main__':
    computing_time({"auto_time": "10:40:00", "auto_tag": 1, "auto_cycle": 1, "auto_date": [31]})
