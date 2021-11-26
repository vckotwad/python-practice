import gc  #import gc module 
print(gc.isenabled()) #by default it is enabled
gc.disable() # disabling gc
print(gc.isenabled())
gc.enable()
print(gc.isenabled())