#writing
f=open('abc.txt','a+')
f.write('hello thre how are you?\n') 
f.write('what are you doing?\n\n')  #data will be added to new line but when next time programs runs all the previoius data will be gone.
f.close()