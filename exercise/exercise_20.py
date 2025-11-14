from abc import ABC, abstractmethod
import re


class Equation(ABC):
    """
    Abstract base class representing a polynomial equation.
    """

    degree: int
    type: str

    def __init__(self, *args):
        """
        Initialize equation coefficients.
        """
        if (self.degree + 1) != len(args):
            raise TypeError(
                f"'Equation' object takes {self.degree + 1} positional arguments "
                f"but {len(args)} were given"
            )

        if any(not isinstance(arg, (int, float)) for arg in args):
            raise TypeError("Coefficients must be of type 'int' or 'float'")

        if args[0] == 0:
            raise ValueError("Highest degree coefficient must be different from zero")

        self.coefficients = {(len(args) - n - 1): arg for n, arg in enumerate(args)}

    def __init_subclass__(cls):
        """
        Ensures any subclass of Equation defines required attributes:
        """
        if not hasattr(cls, "degree"):
            raise AttributeError(
                f"Cannot create '{cls.__name__}' class: "
                "missing required attribute 'degree'"
            )

        if not hasattr(cls, "type"):
            raise AttributeError(
                f"Cannot create '{cls.__name__}' class: "
                "missing required attribute 'type'"
            )

    def __str__(self):
        """
        Return a human-readable mathematical string of the equation.
        """
        terms = []

        for power, coefficient in self.coefficients.items():
            if not coefficient:
                continue

            if power == 0:
                terms.append(f"{coefficient:+}")
            elif power == 1:
                terms.append(f"{coefficient:+}x")
            else:
                terms.append(f"{coefficient:+}x**{power}")

        equation_string = " ".join(terms) + " = 0"
        equation_string = equation_string.strip("+")

        return re.sub(r"(?<!\d)1(?=x)", "", equation_string)

    @abstractmethod
    def solve(self):
        """
        Compute and return the numerical solutions of the equation.
        """
        pass

    @abstractmethod
    def analyze(self):
        """
        Return metadata describing the equation.
        """
        pass


class LinearEquation(Equation):
    """
    Represents a first-degree polynomial equation of the form:
    """

    degree = 1
    type = "Linear Equation"

    def solve(self):
        """
        Solve the linear equation ax + b = 0.
        """
        a, b = self.coefficients.values()
        x = -b / a
        return [x]

    def analyze(self):
        """
        Analyze the linear equation by returning its slope and y-intercept.
        """
        slope, intercept = self.coefficients.values()
        return {"slope": slope, "intercept": intercept}


class QuadraticEquation(Equation):
    """
    Represents a second-degree polynomial equation:
    """

    degree = 2
    type = "Quadratic Equation"

    def __init__(self, *args):
        """
        Initialize a quadratic equation and compute its discriminant (delta).
        """
        super().__init__(*args)
        a, b, c = self.coefficients.values()
        self.delta = b**2 - 4 * a * c

    def solve(self):
        """
        Solve the quadratic equation using the quadratic formula.
        """
        if self.delta < 0:
            return []

        a, b, _ = self.coefficients.values()
        sqrt_delta = self.delta**0.5

        x1 = (-b + sqrt_delta) / (2 * a)
        x2 = (-b - sqrt_delta) / (2 * a)

        if self.delta == 0:
            return [x1]

        return [x1, x2]

    def analyze(self):
        """
        Analyze the quadratic equation:
        """
        a, b, c = self.coefficients.values()

        x_vertex = -b / (2 * a)
        y_vertex = a * x_vertex**2 + b * x_vertex + c

        concavity = "upwards" if a > 0 else "downwards"
        min_max = "min" if a > 0 else "max"

        return {
            "x": x_vertex,
            "y": y_vertex,
            "min_max": min_max,
            "concavity": concavity,
        }


def solver(equation):
    """
    Generate a formatted report for any Equation object.
    """
    if not isinstance(equation, Equation):
        raise TypeError("Argument must be an Equation object")

    output_string = f"\n{equation.type:-^24}"
    output_string += f"\n\n{equation!s:^24}\n\n"
    output_string += f'{"Solutions":-^24}\n\n'

    results = equation.solve()

    match results:
        case []:
            result_list = ["No real roots"]
        case [x]:
            result_list = [f"x = {x:+.3f}"]
        case [x1, x2]:
            result_list = [
                f"x1 = {x1:+.3f}",
                f"x2 = {x2:+.3f}",
            ]

    for result in result_list:
        output_string += f"{result:^24}\n"

    output_string += f'\n{"Details":-^24}\n\n'

    details = equation.analyze()

    match details:
        case {"slope": slope, "intercept": intercept}:
            details_list = [
                f"slope = {slope:>16.3f}",
                f"y-intercept = {intercept:>10.3f}",
            ]

        case {
            "x": x,
            "y": y,
            "min_max": min_max,
            "concavity": concavity,
        }:
            coord = f"({x:.3f}, {y:.3f})"
            details_list = [
                f"concavity = {concavity}",
                f"{min_max} = {coord}",
            ]

    for detail in details_list:
        output_string += f"{detail}\n"

    return output_string


if __name__ == "__main__":
    # Example usage for testing
    lin_eq = LinearEquation(2, 3)
    quadr_eq = QuadraticEquation(1, 2, 1)

    print(solver(quadr_eq))
