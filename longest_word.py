#sen = input("Enter sentence: ")
sd = "This is my test sentence with comparatively long words."

words = sd.split(" ")

longestWord = 0
wrd = ""

for x in words:
    if len(x) > longestWord:
        longestWord = len(x)
        wrd = x
print(f"{wrd} is the longest word with {longestWord} letters")