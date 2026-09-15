# WAP to print Grades:
# Grade A: if marks is beteween 76 and 100
# Grade B: if marks is beteween  51 and 75
# Grade C: if marks is beteween 26 and 50
# Grade D: if marks is beteween 0 and 25

marks = int(input("Enter the marks = "))
if marks>=76 and marks<=100:
    print("Grade A")
elif marks>=51 and marks<=75:
    print("Grade B")
elif marks>=26 and marks<=50:
    print("Grade C")
else:
    print("Grade D")