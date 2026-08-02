fruits = {
    "apple": 130,
    "avocado": 50,
    "banana": 110,
    "sweet cherries": 100,
    "kiwifruit": 90,
    "pear": 100
}

item = input("Item: ")

item = item.lower()

if item in fruits:
    print(f"Calories: {fruits[item]}")
