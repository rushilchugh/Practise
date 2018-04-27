import itertools

a = [1, 11, 21, 1211, 111221]

for i in range(0,len(a)):
    a[i] = str(a[i])

test = '1233333334558999999999999'
[''.join(value) for key, value in itertools.groupby(test)]

def in_way(test):
    w_list = []
    index = 0
    var = ''
    start1 = 0
    start2 = 0
    initial = 0
    final = 0
    
    for index in range(0,len(test)):
        print(index , end = '|')
        try:
            if(test[index] != test[index + 1]):
                w_list.append(test[index])
            else:
                start1 = index
                initial = index
                while(test[start1] == test[start1 + 1]):
                    start1+=1
                    pass
                final = start1
                print(initial , final)
                index = final
                
        except IndexError:
            pass
    print('\n')
    return w_list
