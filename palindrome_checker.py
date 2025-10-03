### Palindrome checker
### "racecar" -> true, "nurses run" -> true, "kamel" -> false

inputStr = input("Please input the word or sentence to be checked: ")
newAr = ""
inputLength = len(inputStr)

while inputLength > 0:
    inputLength -= 1
    newAr += inputStr[inputLength]
    
if inputStr.lower().replace(" ", "") == newAr.lower().replace(" ", ""):
    print(f"{inputStr} is a palindrome")
else:
    print(f"{inputStr} is not a palindrome")

#F-Strings are powerful
def weirdStringStuff():
    amount = 12

    output = f"{inputStr} has exactly {amount:.2f} dollars, which is half of {amount * 2:.2f}."
    print(output)