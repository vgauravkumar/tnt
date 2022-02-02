def print_pairs(di):
    print("Key-Value pair are as follows:-")
    for key in di:
        print(key, ":", di[key])

di = {'jack': 4098, 'guido': 4127, 'irv': 4127}
di2 = {'jack': 4098, 'sape': 4139}
print(type(di))
print_pairs(di)
di["cars"] = 1729
print_pairs(di)
print(di.update(di2))
print_pairs(di)
print(di.pop("cars"))
print_pairs(di)
print("cars" in di)
print("guido" in di)
print(len(di))
print(di.keys())
print(di.values())
print(max(di))
print(min(di))