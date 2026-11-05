n=int(input("Enter a number to count: "))
count=0
while n>0:
    count=count+1
    n=n//10
print("The number of digits in the given number is:",count)