
Print Even Numbers: Write a Python program to print all even numbers from 1 to 50 using a loop and a conditional statement.
for i in range (1,51):
  if i%2==0:
    print(i)

Skip Multiples of 3: Print numbers from 1 to 30, but skip numbers that are divisible by 3 using continue.
for i in range (1,31):
  if i%3==0:
    continue
  print(i)


Stop at a Specific Number: Get a number from the user and print numbers from 1 up to that number. Stop the loop when the number reaches 15 using break.
n=int(input("Enter the number:"))
for i in range(1, 50):
  if i==15:
    break

  print(i)


Positive and Negative Numbers: Get 10 numbers from the user. Check whether each number is positive, negative, or zero. Stop the loop if the user enters 0.
for i in range(1, 11):
    n = int(input("Enter a number: "))

    if n > 0:
        print("Positive number")
    elif n < 0:
        print("Negative number")
    else:
        print("Zero")
        break
