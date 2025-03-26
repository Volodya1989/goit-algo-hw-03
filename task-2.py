import random


def get_numbers_ticket(min: int, max: int, quantity: int) -> list[int]:
    '''
     Generates sorted list of uniques numbers within a given range.
     Parameters:
     min (int): Minimum number in range (must be at least 1).
     max (int): Maximum number in range (must be at most 1000).
     quantity (int): Number of unique numbers to generate.
     '''
       # Validate input constraints
    if not (1 <= min < max <= 1000 and 1 <= quantity <= (max - min + 1)):
            return []
        # Return generated sorted list of the unique numbers.
    return sorted(random.sample(range(min, max+1), quantity))


print(get_numbers_ticket(1, 49, 6))
