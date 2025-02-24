

class Budget:

    # The budeget category, the maximum allowed spending for that category, the current amount spent in the category
    def __init__(self, category, limit, current_spent):
        self.category = category
        self.limit = limit
        self.current_spent = 0

    # String of details from this class
    def __str__(self):
        return f"Budget Status\nCategory: {self.category}, Limit: {self.limit}, Current Spend: {self.current_spent}. Amount left of the budget: {self.limit - self.current_spent}"

    def is_exceeded(self):
            """Returns True if spending exceeds the limit, False otherwise."""
            return self.current_spent > self.limit

    def check_budget(self):
        if self.is_exceeded():
            return f"Budget exceeded for {self.category}, stop spending! Exceeded by {abs(self.limit - self.current_spent)}"
        else:
            return f"Budget is still valid for {self.category}, Limit: {self.limit}, Current Spent: {self.current_spent}. Amount left: {self.limit - self.current_spent}"