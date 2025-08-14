dict1 = {'a':1,'b':2}
dict2 = {'c':4,'d':5}

dict3 = dict(zip(dict1.keys(), dict2.values()))
print(dict3)  