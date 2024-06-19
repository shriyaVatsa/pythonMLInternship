number=int(input("Type a natural number here"))
if number<0:
    print("Type a valid number here")
count=1
factorial=1
while count<=number:
    factorial=factorial*count
    count = count+1

print("The factorial of",number,"is",factorial)

