d = {} # empty dictionary
print(d)

eng_to_spa = {"one": "uno", "two": "dos", "three": "tres"}
print(eng_to_spa)
print(eng_to_spa["one"])
eng_to_spa["tree"] = "arbol" # add item into the dict
print(eng_to_spa["tree"])
eng_to_spa.update({"yes": "si", "no": "no"})
print(eng_to_spa)

del eng_to_spa["yes"]
print(eng_to_spa)

print("These are the spanish words that I know:")
for key in eng_to_spa:
    print(f"{eng_to_spa[key]} means {key}")

print(dir(eng_to_spa))
# 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values'
eng_spa2 = eng_to_spa.copy()
eng_to_spa.clear()
print(eng_spa2)
new_d = eng_spa2.fromkeys(eng_spa2, "YES")
print(new_d)

# get is one of the most useful
print(f"car in spanish is {eng_spa2.get('car', 'UNKNOWN')}")
print(list(eng_spa2.items()))

for key, value in eng_to_spa.items():
    print(f"{value} means {key}")

print(eng_spa2.pop("one"))
print(list(eng_spa2.items()))
eng_spa2.setdefault("red", "rojo")
print(eng_spa2)