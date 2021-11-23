#if loop executed without break then else executes
l=[10,20,600, 30,40]
for i in l:
    if i > 500:
        print("{} cant be processed, insurance req for further processing".format(i))
        break
    print("processing",i)
else:
    print("all item processed succesfully")

