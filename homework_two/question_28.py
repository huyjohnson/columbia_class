import random

listing = []
counter = 0
while counter < 10000:
    listing.append(random.randint(0,10))
    counter += 1

set_list = set(listing)
count_list = []

for i in set_list:
    a = listing.count(i)
    count_list.append(a)

value_counts = {k:v for k,v in zip(set_list, count_list)}
