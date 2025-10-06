### Palindrome checker
### "racecar" -> true, "nurses run" -> true, "kamel" -> false
def my_palindromeVersion():
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
def weirdStringStuff(inputStr):
    amount = 12
    ### if I now add new stuff here and push it to NewFeatures, then main will be behind and I need to pull from NewFeatures once I switch path
    output = f"{inputStr} has exactly {amount:.2f} dollars, which is half of {amount * 2:.2f}."
    print(output)

# Online variant, smoother
def online_palindrome_version(word):
  
  reversed_word = word[::-1] #This :: operation basically reverts a list step by step

  if reversed_word == word:
    return True
  return False

print(online_palindrome_version(input("Test this word: ")))