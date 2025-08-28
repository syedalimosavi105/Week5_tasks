from datetime import date, timedelta

def next_leap_year_from(y):
    """Return the next year >= y that is a leap year."""
    year = y
    while True:
        if (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)):
            return year
        year += 1

def get_next_birthday(month, day, today=None):
    """Return a date object for the next occurrence of given month/day."""
    if today is None:
        today = date.today()

    # Special handling for Feb 29
    if month == 2 and day == 29:
        # start search from this year
        year = today.year
        # if this year's Feb 29 is still ahead (only possible if today <= Feb 29 in a leap year)
        try:
            candidate = date(year, 2, 29)
            if candidate >= today:
                return candidate
        except ValueError:
            pass
        # otherwise find the next leap year and return Feb 29 of that year
        next_leap = next_leap_year_from(year + 1)
        return date(next_leap, 2, 29)

    # Normal birthdays
    year = today.year
    try:
        candidate = date(year, month, day)
    except ValueError:
        return None  # invalid date like April 31
    if candidate >= today:
        return candidate
    else:
        # use next year
        return date(year + 1, month, day)

def days_until_birthday(month, day):
    today = date.today()
    nb = get_next_birthday(month, day, today)
    if nb is None:
        return None, today, None
    delta = (nb - today).days
    return delta, today, nb

if __name__ == "__main__":
    print("Compute days until your next birthday.")
    try:
        m = int(input("Enter birth month (1-12): ").strip())
        d = int(input("Enter birth day (1-31): ").strip())
    except ValueError:
        print("Invalid input. Please enter numeric month and day.")
        raise SystemExit(1)

    days, today, next_bday = days_until_birthday(m, d)
    if days is None:
        print("Invalid date entered. Please check month/day.")
    else:
        # friendly messages
        print(f"\nToday: {today.isoformat()}")
        print(f"Next birthday: {next_bday.isoformat()}")
        if days == 0:
            print("Happy Birthday! 🎉 Today is your birthday.")
        else:
            print(f"Days until next birthday: {days} day(s).")
