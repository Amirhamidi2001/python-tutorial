def arithmetic_arranger(problems, show_answers=False):
    """Arrange arithmetic problems vertically and optionally show answers."""

    # Check if there are too many problems
    if len(problems) > 5:
        return "Error: Too many problems."

    first_line = []
    second_line = []
    dash_line = []
    answer_line = []

    for problem in problems:
        # Split the problem into parts
        parts = problem.split()

        # Check if the problem has the correct format
        if len(parts) != 3:
            return "Error: Invalid problem format."

        num1, operator, num2 = parts

        # Check if operator is valid
        if operator not in ["+", "-"]:
            return "Error: Operator must be '+' or '-'."

        # Check if numbers contain only digits
        if not num1.isdigit() or not num2.isdigit():
            return "Error: Numbers must only contain digits."

        # Check if numbers have more than 4 digits
        if len(num1) > 4 or len(num2) > 4:
            return "Error: Numbers cannot be more than four digits."

        # Determine the width needed for this problem
        width = max(len(num1), len(num2)) + 2

        # Format the first line (right-aligned)
        first_line.append(num1.rjust(width))

        # Format the second line (operator + space + number)
        second_line.append(f"{operator} {num2.rjust(width - 2)}")

        # Format the dash line
        dash_line.append("-" * width)

        # Calculate and format the answer if needed
        if show_answers:
            if operator == "+":
                answer = str(int(num1) + int(num2))
            else:
                answer = str(int(num1) - int(num2))

            answer_line.append(answer.rjust(width))

    # Combine all lines with 4 spaces between problems
    arranged_problems = (
        "    ".join(first_line)
        + "\n"
        + "    ".join(second_line)
        + "\n"
        + "    ".join(dash_line)
    )

    # Add answer line if needed
    if show_answers:
        arranged_problems += "\n" + "    ".join(answer_line)

    return arranged_problems


if __name__ == "__main__":
    print(arithmetic_arranger(["32 + 69", "3801 - 2", "45 + 49", "123 + 49"]))

    print(
        arithmetic_arranger(
            ["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], show_answers=True
        )
    )
