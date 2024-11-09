import random

def random_integer(min_val, max_val):
    """
    Random integer is generated between minimum value and maximum value.
    """
    return random.randint(min_val, max_val)

def random_operator():
    """
    Select a random operator from the provided operators.
    """
    return random.choice(['+', '-', '*'])

def problem(num1, num2, operator):
    """
    :param num1: First number in the problem.
    :param num2: Second number in the problem.
    :param operator: The chosen operator.
    """
    problem_stmt = f"{num1} {operator} {num2}"
    if operator == '+':
        ans = num1 + num2
    elif operator == '-':
        ans = num1 - num2
    elif operator == '*':
        ans = num1 * num2
    else:
        raise ValueError("Invalid operator")
    return problem_stmt, ans

def math_quiz():
    """
    Conduct a math quiz game where the user is presented with random math problems.
    """
    score = 0
    total_questions = 4

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions):
        num1 = random_integer(1, 10)
        num2 = random_integer(1, 5)
        operator = random_operator()

        problem_stmt, ans = problem(num1, num2, operator)
        print(f"\nQuestion: {problem_stmt}")

        # Error handling for user input
        try:
            user_ans = int(input("Your answer: "))
        except ValueError:
            print("Invalid input! Please enter an integer.")
            continue

        # Check if user answer is correct
        if user_ans == ans:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {ans}.")
            print(f"\nGame over! Your score is: {score}/{total_questions}")
            break
    else: print(f"\nGame over! Your score is: {score}/{total_questions}")

if __name__ == "__main__":
    math_quiz()
