import re

def normalize_phone(phone_number):
    # Removing all characters besides digits and '+'
    cleaned_phone = re.sub(r'[^0-9+]', '', phone_number)

    # If phone number starts with 380, but without '+', add it to the beginning of the string
    if re.match(r'^380', cleaned_phone):
        return '+' + cleaned_phone 

    # If phone number does not start with +38, than add it
    if not re.match(r'^\+?38', cleaned_phone):
        return '+38' + cleaned_phone

    # If any condition is not met, return phone number as is
    return cleaned_phone

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)
