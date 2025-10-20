from abc import ABC , abstractmethod

class Employee(ABC):
    def __init__(self,first_name , last_name , ssn):
        self.first_name = first_name
        self.last_name= last_name
        self.ssn = ssn

    @abstractmethod
    def earnings(self):
        pass

    def __repr__(self):
        return f"{self.first_name}  {self.last_name}  (SSN :{self.ssn})"




class SalariedEmployee(Employee):
    def __init__(self, first_name, last_name, ssn , weekly_salary):
        super().__init__(first_name, last_name, ssn)

        if weekly_salary < 0 :
         raise ValueError("weekly salary cannot be negative")
        self.weekly_salary =weekly_salary

    def earnings(self):
        return self.weekly_salary
    



class HourlyEmployee(Employee):
    def __init__(self, first_name, last_name, ssn, hours, wage_per_hour):
        super().__init__(first_name, last_name, ssn)

        if hours < 0 or hours > 168:
            raise ValueError ("Hours should be in between 0 and 168 ")
        
        if wage_per_hour < 0:
              raise ValueError("Wage per hour must be non negative")
        
        self.hours = hours
        self.wage_per_hour = wage_per_hour


    def earnings(self):
        if self.hours <= 40:
            return self.hours * self.wage_per_hour
        else:
            overtime = self.hours - 40
            return (40 * self.wage_per_hour) + (overtime * 1.5 * self.wage_per_hour)
        


employee = [
    SalariedEmployee("Saim" , "Anwar", "0308-6767-370" , 15000),
    HourlyEmployee("Ahmed" , "Azeem" ,  "0388-6676-670", 46 , 700) 
]

for emp in employee:
    print(f"{emp}  Earnings: ${emp.earnings():.2f}")
       
   



