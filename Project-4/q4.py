def number_machine(number: int) -> None:
    # reverse Method
    temp_num = number
    rev_number = 0
    while temp_num > 0:
        # get the current units placed value
        last_digit = temp_num % 10
        # Construct teh revers string
        rev_number = rev_number*10 + last_digit
        # divide to remove by an order of magnitude of 10 to shift to the next place
        temp_num //= 10
    print(f"Reversed Number from {number}: {rev_number}")

    # sum of digits Method
    temp_num = number
    sum = 0
    while temp_num > 0:
        # gets the last units place(remainder)
        digit = temp_num % 10
        # adds the digit
        sum += digit
        # divides by 10 and rounds to remove the last units place
        temp_num //= 10
    print(f"Sum of digits of {number} is: {sum}")

    # generate new number by adding 1 to each digit
    temp_num = number
    new_number = 0
    place = 1
    while temp_num > 0:
        # gets the last units place(remainder)
        digit = temp_num % 10
        # Add 1 to the digit and place it correctly
        new_number += (digit + 1) * place
        # Move to the next place value
        place *= 10
        # Remove the last digit
        temp_num //= 10
    print(f"New Number created from {number} is: {new_number}")
