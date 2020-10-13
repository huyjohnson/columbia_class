key_list = [x for x in range(0,100)]
value_list = []

for i in key_list:
    #finding the largest prime factor
    x = 2
    if i == 0:
        i = 1
        value_list.append(i)
    else:
        while x * x <= i:
            if i % x:
                x += 1
            else:
                i //= x
        value_list.append(i)

dicter = {k:k//v for k, v in zip(key_list, value_list)}
