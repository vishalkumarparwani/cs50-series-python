def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    num_started = False

    if len(s) < 2 or len(s) > 6:
        return False

    if not s[0:2].isalpha():
        return False

    for c in s:
         if c.isdigit():
             if not num_started and c == "0":
                 return False
             num_started = True
         elif num_started:
             return False

    if not s.isalnum():
        return False

    return True

main()
