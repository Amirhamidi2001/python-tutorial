from typing import List, Dict


class Category:
    def __init__(self, name: str) -> None:
        self.name: str = name
        self.ledger: List[Dict[str, str | float]] = []

    def deposit(self, amount: float, description: str = "") -> None:
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount: float, description: str = "") -> bool:
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self) -> float:
        return sum(item["amount"] for item in self.ledger)

    def transfer(self, amount: float, category: "Category") -> bool:
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount: float) -> bool:
        return self.get_balance() >= amount

    def __str__(self) -> str:
        title = f"{self.name:*^30}\n"
        items = ""
        for entry in self.ledger:
            description = entry["description"][:23]
            amount = f"{entry['amount']:.2f}"
            items += f"{description:<23}{amount:>7}\n"
        total = f"Total: {self.get_balance():.2f}"
        return title + items + total


def create_spend_chart(categories: List[Category]) -> str:
    """Generate a bar chart of spending percentages per category."""
    category_spending: List[float] = []
    total_spent: float = 0

    # Calculate spending per category
    for category in categories:
        spent = sum(-item["amount"] for item in category.ledger if item["amount"] < 0)
        category_spending.append(spent)
        total_spent += spent

    # Calculate rounded percentages
    spent_percentages: List[int] = []
    for spent in category_spending:
        if total_spent > 0:
            percentage = (spent / total_spent) * 100
            rounded = int(percentage // 10) * 10
        else:
            rounded = 0
        spent_percentages.append(rounded)

    # Build chart string
    chart = "Percentage spent by category\n"
    for i in range(100, -1, -10):
        chart += f"{i:>3}| "
        for percentage in spent_percentages:
            chart += "o  " if percentage >= i else "   "
        chart += "\n"

    # Horizontal line
    chart += "    -" + "---" * len(categories) + "\n"

    # Vertical category names
    max_name_len = max(len(category.name) for category in categories)
    for i in range(max_name_len):
        chart += "     "
        for category in categories:
            chart += (category.name[i] + "  ") if i < len(category.name) else "   "
        if i < max_name_len - 1:
            chart += "\n"

    return chart
