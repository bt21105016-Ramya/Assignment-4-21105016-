#Question 1
print("Question 1")
print("Solution  of the problem of tower of Hanoi with three disks.")
print("")
def hanoi(n, fro, to, aux):
    if n == 0:
        return
    
    hanoi(n-1, fro, aux, to)
    print(f"Move Disk {n} from {fro} to {to}")
    hanoi(n-1, aux, to, fro)

#calling funtion for 3 disks
hanoi(3, 'A', 'C', 'B')
#########################################################################

#Question 2
print("Question 2")
n = int(input("Number of rows in Pascal's Triangle: "))

print("\nUsing recursions:\n")
def pascal(n, originaln=n):
    if n == 0:
        return
    
    pascal(n-1,originaln)

    print('  '*(originaln-n), end='')
    
    entry=1
    for i in range(1, n+1):

        print(entry, end ='   ')

        #using Binomial Coefficient
        entry = entry * (n - i) // i
    print()
pascal(n)
########################################################################

#Question 3
print("Question 3")

a=int(input("Enter the first integer:"))
b=int(input("Enter the second integer:"))
c=a%b
d=a//b
print("Remainder is:", c)
print("Quotient is:",d)
if(c!=0):
    if (d!=0):
        print("Both valus are non-zero")
    else:
        print("One value is zero")
else:
    if (d!=0):
        print("One value is zero")
    else:
        print("Both values are zero")
set1=set()
for i in range (4,7):
    e=c+i
    f=d+i
    if(e>4):
        set1.add(e)
        print(set1)
    if(f>4):
        set1.add(f)
        print(set1)

print(set1)
set2=frozenset(set1)
print("Immutable set: ", frozenset(set1))
print("Largest value in the set: ", max(set2))
k=max(set2)
print("Hash value: ", hash(k))
###################################################################

#Question 4
print("Question 4")
class Student:
    def __init__(self, student, sid):
        self.name = student
        self.sid = sid
    
    def __del__(self):
        print("Object is destroyed")

#creating the object
student = Student("Ramya Garg", 21105016)
print("Object is created")

#printing the assigned values to the object
print(f"The name of the student is {student.name} and SID is {student.sid}.")

#deleting the object
del student
####################################################################

#Question 5
print("Question 5")
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def __del__(self):
        print(f"The record of employee {self.name} is deleted")

employee1 = Employee("Mehak", 40000)
employee2 = Employee("Ashok", 50000)
employee3 = Employee("Viren", 60000)

employee1.salary = 70000
print(f"a. The updated salary of employee {employee1.name} is {employee1.salary}")

print("b. ", end='')
del employee3
######################################################################

#Question 6
print("Question 6")
word = input("Enter the first word: ")

test_word = input("\nEnter a new meaningful for friendship test: ")

def count_in_dict(word):
    count = {}
    list1 = list(word)
    
    n = len(list1)
    for i in range(n):
        if list1[i] in count:
            count[list1[i]] += 1
        else:
            count[list1[i]] = 1
    return count

if count_in_dict(word) != count_in_dict(test_word):
    print("Word is not maeinungful,friendship is fake")

def new_input():
    ans = input("\nDoes the word makes sense?(Yes or No)\n")

    if ans == 'Yes':
        print("Meaningful word is created by Barbie,friendship test is passed.\n\n")
    elif ans == 'No':
        print("The word is not meaningful,their friendship is fake.\n\n")
    else:
        print("Invalid input, try again")
        new_input()
new_input()

print("\nUsing loops:\n")
for line in range(1, n+1):

    print('  '*(n - line), end='')

    x = 1
    for i in range(1, line+1):

        print(x, end='   ')

        x = x * (line - i) // i
#########################################################################

