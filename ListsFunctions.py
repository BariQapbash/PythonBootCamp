numbers = [44,7,18,32,17,27,37]
friends = ["Bari","Bari","Filore","Aliye","Waris"]
friends.append("Creed") # will add the item

friends.insert(1,"Filora") # will add an element and push another elements to the right

friends.remove("Filore")
friends.sort()
print(friends)
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)
print("______________________")
friends2 = friends.copy()
print(friends2)
print("______________________________")


# friends.clear() # remove all items from the list
friends.pop() # indicate index of element want to remove or delete last element

friends.extend(numbers) # will add a list to another list


print(friends)


print(friends.index("Bari"))
print(friends.count("Bari"))



