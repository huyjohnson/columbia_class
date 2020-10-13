import random

listing = []
counter = 0
while counter < 10000:
    listing.append(random.randint(0,10))
    counter += 1
listing.sort()
result = listing[0]
