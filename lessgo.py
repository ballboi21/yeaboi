import random
da_list = []
for i in range(50):
    # i = 0, 1, 2 ...499
    x = random.randint(1, 100)
    da_list.append(x)


for i in range(50):
    if 42 == da_list[i]:
        print("i found the meaning of life")
        exit(0)    
        
        
print("I did not find")