word = input("Enter a word: ").lower()
vowels = "aeiou"
count = 0

for char in word:
    if char in vowels:
        count = count + 1

print(f"The number of vowels in {word} is: {count}")