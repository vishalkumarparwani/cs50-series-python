months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    try:
        date = input("Date: ").strip().title()

        if date.find("/") != -1:
            month, day, year = date.split("/")
            month = int(month)
            day = int(day)
            year = int(year)
            if (month < 1 or month > 12) or (day < 1 or day > 31) or year < 1:
                continue

        elif date.find(" ") != -1:
            if "," not in date:
                continue
            date = date.replace(",", "").strip()
            month, day, year = date.split()
            month = months.index(month) + 1
            day = int(day)
            year = int(year)
            if (month < 1 or month > 12) or (day < 1 or day > 31) or year < 1:
                continue

        else:
            continue

        print(f"{int(year):04d}-{int(month):02d}-{int(day):02d}")
        break

    except (ValueError, KeyError):
        continue;

