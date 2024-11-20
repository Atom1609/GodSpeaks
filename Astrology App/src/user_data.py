def get_user_details():
    """Prompt user for birth details."""
    name = input("Enter your name: ")
    day = int(input("Enter your birth day (DD): "))
    month = int(input("Enter your birth month (MM): "))
    year = int(input("Enter your birth year (YYYY): "))

    return {
        "name": name,
        "birth_day": day,
        "birth_month": month,
        "birth_year": year
    }
