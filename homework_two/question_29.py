import random

listing = []
counter = 0
while counter < 10000:
    listing.append(random.randint(0,10))
    counter += 1

set_list = set(listing)
ratio_list = []

for i in set_list:
    a = listing.count(i)
    a /= len(listing)
    ratio_list.append(a)

value_ratio = {k:v for k,v in zip(set_list, ratio_list)}
