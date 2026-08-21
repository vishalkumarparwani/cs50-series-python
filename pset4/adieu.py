def main():
    names = []

    try:
        while True:
            names.append(input("Name: "))

    except EOFError:
        print()

    if len(names) == 1:
        result = names[0]
    elif len(names) == 2:
        result = " and ".join(names)
    else:
        result = ", ".join(names[:-1]) + ", and " + names[-1]

    print(f"Adieu, adieu, to {result}")


if __name__ == "__main__":
    main()
