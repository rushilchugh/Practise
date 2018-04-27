__author__ = 'Rushil'


def main(num):

    counts = set()
    i = 0
    flag = True
    eq_set = set(range(10))

    or_num = num
    f = num

    if num == 0:
        return "INSOMNIA"

    while flag:

        i += 1

        while num:

            counts.add(num % 10)
            num //= 10

        if counts == eq_set:
            flag = False

        else:
            num = or_num * i
            f = num

    return f

print(main(163444))