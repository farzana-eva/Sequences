menu = [
    ["egg", "milk"],
    ["egg", "bread", "milk"],
    ["egg", "spam"],
    ["egg", "milk", "spam"],
    ["egg", "milk", "bread", "spam"],
    ["spam", "milk", "bread", "spam"],
    ["spam", "egg", "spam", "spam", "milk", "spam"],
    ["spam", "bread", "spam", "milk", "spam", "tomato", "spam"],
]
# 1st sloution

#for meal in menu:
#   for index in range(len(meal) - 1, -1, -1):
#        if meal[index] == "spam":
#            del meal[index]
#    print(meal)


# Second sloution

for meal in menu:
    for item in meal:
        if item != "spam":
            print(item)
    print()
