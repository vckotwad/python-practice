
from pyaml import yaml
e={'name':{'first_name':'john','last_name':'alex'},'salary':'10000','ismarried':None}

#serialization to yaml string
print("serialization to yaml string :-\n")
yaml_string=yaml.dump(e)

print(yaml_string)

#serilization to yaml file
print("serialization to yaml string :-\n")
with open('file.yaml','w') as f:
    yaml.dump(e,f)

#deserilization of yaml string
print("deserilising yaml string:-\n")
e2=yaml.safe_load(yaml_string)
print(e2)

#deserilisation of yaml file
print("\ndeserilising yaml file:-\n")
with open('file.yaml','r') as f2:
    e3=yaml.safe_load(f2)

print(e3)