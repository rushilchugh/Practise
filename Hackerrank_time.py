#!/bin/python3

import sys


time = input().strip()

def am_to_pm(time):

    if time == '00:00:00AM':
        return '00:00:00'

    if time == '12:00:00PM':
        return '12:00:00'

    if time == '12:00:00AM':
        return '12:00:00'

    act_time = time[:-2]
    time_suff = time[-2:]

    if time_suff == 'AM':

        return act_time

    if time_suff == 'PM':
        str_act_time = act_time.split(':')
        hrs = int(str_act_time[0]) + 12
        str_act_time[0] = str(hrs)
        return ':'.join(str_act_time)


print(am_to_pm(time))
