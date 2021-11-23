item=[10,20,30,600,70,80]
for i in  item:
    if i>500:
        print("value is greater than 500, insurance is required")
        break
    print("processing item",i)
print("now out of loop")
