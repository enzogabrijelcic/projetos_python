import datetime

mydate = datetime.datetime.now()

print("__str__() string: ", mydate.__str__())
print("str() string: ", str(mydate))

print("__repr__() string: ", mydate.__repr__())
print("repr() string: ", repr(mydate))
