#Given a number N.Find if the digit sum(or sum of digits) of N is a Palindrome number or not.

N = input("Input any number: ")
counter=1
z=int()
for i in range(len(N)):
    x=(N[i:counter])
    counter += 1
    if i == 0:
        z = x
    else:
        z =int(z)
        x =int (x)
        z += x
z = str(z)
check = z[::-1]
if z==check:
    print(z," is a palindrome number")
else:
    print(z," is not a palindrome number")