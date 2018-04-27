__author__ = 'Rushil'

# −2, 1, −3, 4, −1, 2, 1, −5, 4
#-2, -1, 5, -7, 5

# if num >

def max_contiguous_sum(num_list):
    sum_prev = 0
    curr_sum = 0

    for num in num_list:
        if num + sum_prev >= sum_prev:
            curr_sum = num + sum_prev
            sum_prev = curr_sum
        elif num + sum_prev < sum_prev:
            sum_prev = 0

    return curr_sum

print(max_contiguous_sum([1,-1,2,3,-1,87,-10]))

def max_contiguous_sum_2(num_list):
    sum_prev = 0
    sum_curr = 0

    for index in range(len(num_list)):
        if num_list[index] + sum_prev >= sum_curr:
            sum_curr = num_list[index] + sum_prev
            sum_prev = sum_curr
        elif num_list[index] + sum_prev < sum_prev:
            sum_prev = 0

    return sum_curr

print(max_contiguous_sum_2([1,-1,2,3,-1,87,-10]))