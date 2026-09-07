#WAP to check the eligibility criteria for voting & participating in election

age =int(input("Enter the age for eligibility"))
if age>=21:
    print("Eligible for participating in election")
elif age>=18 and age<21:
    print("eligible for voting and not eligible for participating in election ")
else:
    print("not eligible for both")