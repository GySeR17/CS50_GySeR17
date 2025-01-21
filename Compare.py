x = int(input("What's x? "))
y = int(input("What's y? "))

if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
else:
    print("x is equal to y")

grade = int(input("Your grade: "))
if grade>=90:
    print("Your grade is: A")
elif grade>=80:
    print("Your grade is: B")
elif grade>=70:
    print("Your grade is: C")
elif grade>=60:
    print("Your grade is: D")
else :
    print("Your grade is: F")