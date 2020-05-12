from pro008_singleton import SingeltonObject

obj1 = SingeltonObject()
obj1.val = "Obj value 1"

print("print obj1: ", obj1)

obj2 = SingeltonObject()
obj2.val = "Obj value 2"


print("print obj1: ", obj1)
print("print obj2: ", obj2)