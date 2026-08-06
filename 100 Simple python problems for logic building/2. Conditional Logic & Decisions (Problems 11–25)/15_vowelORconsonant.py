# •	15. Vowel or Consonant: Check if an input character is a vowel or a consonant.

letter = str(input("Enter a letter : ")).lower()

vowel = ['a','e','i','o','u']
if letter in vowel:
    print(f"{letter} is Vowel.") 
elif letter.isalpha() and len(letter)== 1:
    print(f"{letter} is Consonant.")
else :
    print("ERROR!, Undefine character!")