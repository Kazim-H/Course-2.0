# Task 2
# Given a List of distinct elements. Find the third largest element in it.
# Suppose you have A= {1, 2, 3, 4, 5, 6, 7}, its output will be 5 because
# it is the 3rd largest element in list
A=[1,2,3,4,5,6,7]
counter = 0
while counter < 2:
    max = 0
    for i in A:
        if i > max:
            max = i
    A.remove(max)
    counter += 1
max= 0
for i in A:
    if i > max:
        max = i
print("The third largest number is:", max)
