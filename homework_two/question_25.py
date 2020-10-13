key_list = [x for x in range(0,100)]
value_list = []

for i in key_list:
    #finding the least prime factor
    if i == 0:
        i = 1
        value_list.append(i)
    else:
        #if even, smallest prime is always 2
        if i % 2 == 0:
            i = 2
            value_list.append(i)
        #if odd, start from 3 on up in increments of 2 to search all odd numbers
        else:
            x = 3
            while x * x <= i:
                if i % x:
                    x += 2
                else:
                    i = x
            value_list.append(i)

dicter = {k:k//v for k, v in zip(key_list, value_list)}
