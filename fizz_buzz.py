### first time python loops
i = 0
while i < 100:
    i += 1
    if i / 3 % 1 == 0 and i / 5 % 1 == 0:
        print("FizzBuzz")
        continue
    elif i / 3 % 1 == 0:
        print("Fizz")
        continue
    elif i / 5 % 1 == 0:
        print("Buzz")
        continue
    else: 
        print(i)