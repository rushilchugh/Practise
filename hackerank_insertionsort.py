__author__ = 'Rushil'

def insertion_sort(n,num_list):
    # 2 4 6 8 3

    m_num = num = num_list[-1]

    for iters in range(len(num_list)):
        for i,num in enumerate(num_list):
            try:
                if num_list[i] > num_list[i+1]:
                    num_list[i],num_list[i+1] = num_list[i+1],num_list[i]
                    #print(num_list)
                    temp = num_list[i]
                    num_list[i] = num_list[i+1]
                    print(' '.join(list(map(str,num_list))))
                    num_list[i] = temp
                    #print('--'*60)
            except:
                pass
    print(' '.join(list(map(str,num_list))))


n = int(input().strip())

array = list(map(int,input().strip().split(' ')))

insertion_sort(n,array)


