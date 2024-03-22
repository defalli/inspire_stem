laptop = {"make":"lenovo","color" :"black", "year": "2024"}
print(laptop ["make"])
print(laptop["color"])
print(laptop["year"])
#change values in a dictionary
laptop ["color"] = "red"
laptop["year"] = "2009"

print(laptop)

laptop["size"] = "120mm x 100"
print(laptop)

"""
for key,value in laptop.items():
    print(key)
    print("\n")
    print(value)
"""
