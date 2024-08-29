from datetime import datetime, date


def age_calc(n):

    current_date = date.today()
    age = current_date.year - n.year - ((current_date.month,
                                         current_date.day) < (n.month, n.day))
    return age


birthdate = input("Enter your birthdate: (YYYY-MM-DD)")

try:
    birthdate = datetime.strptime(birthdate, "%Y-%m-%d").date()
    age = age_calc(birthdate)
    print(f"You are {age} years old")
except ValueError:
    print("Please enter the date in YYYY-MM-DD format.")
