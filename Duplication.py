#Program to remove duplication in any list
list = [2,4,3,2,5,7,6,2,9,8,3]
final = []

for num in list:

    if num not in final:
        final.append(num)
print(final)