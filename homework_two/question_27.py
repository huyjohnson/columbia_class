import random

listing = []
counter = 0
while counter < 10000:
    listing.append(random.randint(0,10))
    counter += 1
no_ord = []
for i in listing:
    a = [i]
    if set(a).issubset(set(no_ord)) == False:
        no_ord.append(i)
    else:
        pass
result = no_ord
