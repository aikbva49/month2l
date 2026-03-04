def safe_password(password):

    if len(password) < 10:
        return False

    digits = "0123456789"
    lowers = "abcdefghijklmnopqrstuvwxyz"
    uppers = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    digit_found = False
    lower_found = False
    upper_found = False
    other_count = 0

    for p in password:
        if p in digits:
            digit_found = True
        elif p in lowers:
            lower_found = True
        elif p in uppers:
            upper_found = True
        else:
            other_count += 1

    if digit_found and lower_found and upper_found and other_count >= 2:
        return True
    else:
        return False

def find_nearest_number(numbers, target):

        if len(numbers) == 0:
            return None

        nearest = numbers[0]

        for n in numbers:
            diff_n = n - target
            if diff_n < 0:
                diff_n = -diff_n

            diff_nearest = nearest - target
            if diff_nearest < 0:
                diff_nearest = -diff_nearest

            if diff_n < diff_nearest:
                nearest = n

        return nearest

print(find_nearest_number([1, 2, 3], 5))  # 3
print(find_nearest_number([10, -2, 4, 7], 3))  # 4
print(find_nearest_number([8, 15, 3, 9], 10))  # 9

