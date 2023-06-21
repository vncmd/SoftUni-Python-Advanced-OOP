class NegativeValueError(Exception):
    """
    Number not valid, value is negative.
    """
    pass


nums = [int(input()) for _ in range(5)]

for num in nums:
    number = int(input())

    if number < 0:
        raise NegativeValueError('The integer you provided is not a positive number')
