class Expense:
    def __init__(self,name,category,amount):
        self.name=name
        self.category=category
        self.amount=amount


    def __repr__(self):           #function for every class to convert c]obj into string
        return f"<Expense> {self.name} and {self.amount}:.."

        
        