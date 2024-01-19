#iven an integer list and an integer element. The task is to find if the given element is present in list or not.
# Display the position (index) of the element
list = [75, 55, 22, 82, 12]
element = 22


for i in range(len(list)):
    if list[i] == element:
        print("The element", element, "is present at position", i, "in the list.")
        break
else:
    print("The element", element, "is not present in the list.")