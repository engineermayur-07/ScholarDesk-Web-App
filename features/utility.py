def date_checker(date):
    try:
        day, month, year = map(int, date.split('-'))
        if 1 <= day <= 31 and 1 <= month <= 12 and year >= 2020:
            if month == 2:
                if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
                    if day <= 29:
                        return True
                    else:
                        return False
                else:
                    if day <= 28:
                         return True
                    else:
                        return False
            return True
        else:
            return False
    except ValueError:
        return False

def password_checker(password):
    if len(password) < 8:
        print("❌ Password must be at least 8 characters long.")
        return False
    if not any(char.isdigit() for char in password):
        print("❌ Password must contain at least one digit.")
        return False
    if not any(char.isalpha() for char in password):
        print("❌ Password must contain at least one letter.")
        return False
    return True