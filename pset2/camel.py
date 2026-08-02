camel = input("camelCase: ")

snake = ""

for c in camel:

    if c.isupper():
        snake += "_"
        snake += c.lower()
    else:
        snake += c

print(snake)
