
coordinates = (4,5,6)
# coordinates[1] = 10 we can't change value of the items in tuple, they are immutable
print(coordinates[2])

coordinates1 = [(4,5,6),(6,7),(80,34)]
coordinates1.pop()
print(coordinates1) # [(4, 5, 6), (6, 7)]

