__author__ = 'Rushil'

import re
import shutil

file_path = r'C:\NOS\Music\Playlists\Taylor Swift.wpl'
dest_path = r'C:\NOS\Tay_music_temp'
path_ap = r'C:\NOS\Music'

a = open(file_path , 'r').read()

exp = re.compile(r'".+mp3"')
src_list = exp.findall(a)

path_list = []


for i in src_list:
    path_list.append(path_ap + i[3:-1])

for i in path_list:
    shutil.copy2(i,dest_path)



