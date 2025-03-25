from datetime import datetime


def get_days_from_today(dateString):
    # using try block to catch invalid formatting
    try:
        # converting into date object
        staticDate = datetime.strptime(dateString, "%Y-%m-%d")
        # getting current date
        currentDate = datetime.today()
        # calculating difference
        difference = currentDate-staticDate
        # returning difference as whole days
        return difference.days
    except ValueError:
        # printing out message to help user understand that there is formatting issue
        print("Try again as format Invalid. Please use 'YYYY-MM-DD'.")
        return None


print(get_days_from_today('2020-10-01'))
