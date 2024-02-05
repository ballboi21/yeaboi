import random
pepechopa_list = []
pepechopa2_list = []
length = 100
change = 1
for i in range(100):
    x = random.randint(1, 100)
    pepechopa_list.append(x)

for i in range(100):
    x = pepechopa_list[length - change]
    pepechopa2_list.append(x)

    change = change + 1

print(pepechopa_list)
print(pepechopa2_list)