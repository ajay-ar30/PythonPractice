'''Problem 1
Fill in the Line class methods to accept coordinates as a pair of tuples and return the slope and distance of the line.'''

class Line():
    
    def __init__(self,coor1,coor2):
        self.coor1 = coor1
        self.coor2 = coor2
    
    def distance(self):
        x1,y1 = self.coor1
        x2,y2 = self.coor2
        return ((x2-x1)**2+(y2-y1)**2)**0.5    
    def slope(self):
        x1,y1 = self.coor1
        x2,y2 = self.coor2
        return (y2-y1)/(x2-x1)
# EXAMPLE OUTPUT

coordinate1 = (3,2)
coordinate2 = (8,10)

li = Line(coordinate1,coordinate2)
print(li.distance())
print(li.slope())

'''
Problem 2
Fill in the class

'''
class Cylinder():
    pi = 3.14
    def __init__(self,height=1,radius=1):
        self.height = height
        self.radius = radius
        
    def volume(self):
        return self.pi * self.radius**2 * self.height
    def surface_area(self):
        top = self.pi * (self.radius)**2
        return (2*top) + (2*self.pi*self.radius*self.height)
# EXAMPLE OUTPUT
c = Cylinder(2,3)
print(c.volume())
print(c.surface_area())


'''Object Oriented Programming Challenge
For this challenge, create a bank account class that has two attributes:

owner
balance
and two methods:

deposit
withdraw
As an added requirement, withdrawals may not exceed the available balance.

Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn.'''

class BankAccount():
    def __init__(self, owner,balance=0):
        self.owner = owner
        self.balance = balance
        print(f"Account owner: {self.owner}\nAccount balance:${self.balance}")

    def deposit(self,dep_amt):
        self.balance += dep_amt
        return "Deposit accepted"
    
    def withdraw(self, wd_amt):
        if self.balance >= wd_amt:
            self.balance -= wd_amt
            print('Withdrawal Accepted')
        else:
            print('Funds Unavailable!')
acct1 = BankAccount("Jose",100)
acct1.deposit(5000)
print(acct1.balance)
    
