import random 

VALORES = 30
LIMITE_NUM = 100


file = open ("valores.txt", "a")

for i in range(0,VALORES):
    a = str(random.randint(1,LIMITE_NUM)) + "\n"
    file.write(a)
file.close ()