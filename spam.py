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

for meal in menu:
    if "spam" not in meal:
        print(meal)

        for item in meal:
            print(item)

    else:
        print("{0} has a spam of {1}"
              .format(meal, meal.count("spam")))
