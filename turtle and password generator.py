# # Right angled triange by turtle
# import turtle
# turtle.forward(100)
# turtle.left(90)
# turtle.forward(100)
# turtle.left(135)
# turtle.forward(140)
# input()

# Random Password Generator
import random

lc= list('abcdefghijklmnopqrstuvwxyz')
uc= list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
n = list('0123456789')
sc = list('!@#$%&*()')
tc = list('!@#$%&*()0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz')
c1 = random.choice(lc)
n1 = random.choice(n)
sc1 = random.choice(sc)
all0 = random.choice(tc)
all1 = random.choice(tc)
all2 = random.choice(tc)
all3 = random.choice(tc)
all4 = random.choice(tc)
total = c1+n1+sc1+all0+all1+all2+all3+all4
total = list(total)
random.shuffle(total)
total = ''.join(total)
print("Random Password:", total[:8])