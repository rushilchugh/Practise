__author__ = 'Rushil'

import os

sub_dir = r'C:\NOS\Shows\Band Of Brothers\Band_of_Brothers - season 1'
ep_dir = r'C:\NOS\Shows\Band Of Brothers'

name_form = r'Band of Brothers 01 - Currahee.avi'
sub_form = r'Band of Brothers - 1x01 - Currahee.DVD.Xeros.en.srt'

name_list = []

for i in os.listdir(ep_dir)[:-2]:
        [name , ext] = i.split('.')

        if ext.lower() == 'avi':
            name_list.append(name)

print(name_list)

sub_list = []

for sub_num , i in enumerate(os.listdir(sub_dir)):
    if 'DVD' in i:
        sub_list.append(os.path.join(sub_dir , i))

print(sub_list)

m_list = list(zip(name_list , sub_list))

for i in m_list:

    os.rename(i[1] , i[0])