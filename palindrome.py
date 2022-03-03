number: int = int(input("enter the number :"))
temp = int(number)
rev: int = 0
while number > 0:
    rem = int(number % 10)
    rev = int(rev * 10 + rem)
    number = int(number / 10)
if rev == temp:
    print("palindrome")
else:
    print("not palindrome")

