

class Budget:

    # The budeget category, the maximum allowed spending for that category, the current amount spent in the category
    def __init__(self, category, limit, current_spent)
        self.category = category
        self.limit = limit
        self.current_spent = current_spent

    # String of details from this class
    def __str__(self):
        return f"Budget Status \n Category: {self.category}, Limit: {self.limit}, Current Spend: {self.current_spent}" 
    

    # Updates the current amount spent by adding the amount you just spent to the current spent
    def update_spent(self,amount):
        self.current_spent += amount
        return f"Current spent is now {self.current_spent}"
    
    # Checks if you are over the budget for the category returns warning 
    # If the limit hasnt been exceeded return budget still valid and shows the 
    # limit and how much you have spent.
    def check_budget(self):
        if self.current_spent > limit:
            return f"Budget exceeded for {self.category}, stop spending!"
        else:
            return f"Budget is still valid for {self.category}, Limit: {self.limit}, Current Spent {self.current_spent}"

