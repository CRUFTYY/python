def predict_next_number(numbers):
    """
    Predicts the next number in the 1xBet Aviator game.

    Parameters:
    - numbers: list of int
        A list of numbers representing the sequence of numbers in the game.

    Returns:
    - int:
        The predicted next number in the game.

    Raises:
    - ValueError:
        Raises an error if the input list is empty or contains less than 3 numbers.
    """

    # Checking if the input list is empty or contains less than 3 numbers
    if len(numbers) < 3:
        raise ValueError("Input list should contain at least 3 numbers.")

    # Extracting the last three numbers from the list
    last_three_numbers = numbers[-3:]

    # Calculating the difference between the second and first number
    diff1 = last_three_numbers[1] - last_three_numbers[0]

    # Calculating the difference between the third and second number
    diff2 = last_three_numbers[2] - last_three_numbers[1]

    # Predicting the next number by adding the difference to the last number
    next_number = last_three_numbers[2] + diff2

    return next_number

# Example usage:

# Example 1: Predicting the next number in the game
numbers1 = [10, 20, 30, 40, 50]
next_number1 = predict_next_number(numbers1)
print(f"The next number in the 1xBet Aviator game is predicted to be: {next_number1}.")

# Example 2: Predicting the next number with an input list containing less than 3 numbers (should raise an error)
try:
    numbers2 = [10, 20]
    next_number2 = predict_next_number(numbers2)
    print(f"The next number in the 1xBet Aviator game is predicted to be: {next_number2}.")
except ValueError as e:
    print(f"Error: {e}")