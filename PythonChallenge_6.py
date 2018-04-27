import zipfile
import os
import re
import glob

path = os.getcwd()
path = os.path.join(path , 'Channel')

os.chdir(path)

num = '90052'
filename = num + '.txt'

while True:
    a = open(filename , 'r')
    page_text = a.read()
    num = re.findall('\d+' , page_text)[0]
    filename = num + '.txt'
    print(filename)


filename2 = '46145.txt'
