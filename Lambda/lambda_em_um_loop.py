callables = []
a = ""
for i in (1, 2, 3):
    callables.append(lambda a=i: a)

for f in callables:
    print(f())
