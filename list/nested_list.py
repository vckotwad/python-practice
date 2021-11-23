l=[10,20,[30,40,[90,100]]] #nested list
print(l[2][2][0]) #on index 2 also accessing 0th  index

l1=[[10,20,30],[40,50,60],[70,80,90]]
for i in range(3):
    for j in range(3):
        print(l1[i][j], end=" ")
    print("\n")
            
