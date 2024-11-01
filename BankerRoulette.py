import random
# initializing list
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

# printing original list
print("Original list is : " + str(friends))

# using random.choice() to get a random name
random_name = random.choice(friends)

# printing random name
print("Random selected friend is : " + random_name)