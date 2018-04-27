__author__ = 'Rushil'

from math import sqrt
import threading
import time

def convert_fraction(a,b,c):
    return a*b+c , c

def get_trip(num_list):
    a = num_list[2]*num_list[0]+num_list[1]
    b = num_list[2]
    c = sqrt(a**2 + b**2)
    return a , b , int(c)

stife = list(zip(range(1,1000) , range(1,1000) , range(3,1000,2)))
ozanam = list(zip(range(1,1000) , range(7,1000,4) , range(8,1000,4)))

print(stife)
print(ozanam)

main_trips = []

def A():
    for i in stife:
            main_trips.append(get_trip(i))

def B():
    for j in ozanam:
        main_trips.append(get_trip(j))

t1 = threading.Thread(target = A).start()
t2 = threading.Thread(target = B).start()

time.sleep(1)

print(main_trips)

sum_list = list(map(sum , main_trips))
print(sum_list)
