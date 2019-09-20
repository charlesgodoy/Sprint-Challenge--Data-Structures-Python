import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

"""
Above code goes through the entirety of name_1 then for each
element in names_1, goes through the entirety of names_2, 
then after that, does a check to see where they match
which causes it to be take too long.
"""

for x in names_1:
    if x in names_2:
            duplicates.append(x)

"""
Now the above code here takes element from names_1,
and then goes straight to to see if it appears in names_2, then adds to list.
Process reduces time.
"""


end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

