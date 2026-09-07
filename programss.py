#check number is palindrome  or not

num = input("Enter the number value to check palindrome  : ")

if num == num[::-1]:
    print("Number is palindrome ")
else:
    print("number is not palindrome ")