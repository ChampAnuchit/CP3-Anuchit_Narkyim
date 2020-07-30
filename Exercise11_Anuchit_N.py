pyramid = int(input("Number of floors = "))
for i in range(pyramid):
    for j in range(i+1):
        result = (" "*(pyramid-(j+1))+"*"*(1+(2*i)))
    print(result)



