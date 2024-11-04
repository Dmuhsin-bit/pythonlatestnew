#Print "Vowel" if the character is a vowel (a, e, i, o, u).
#Print "Consonant" if the character is a consonant (any other alphabetical character).
#Print "Not an alphabet" if the character is not an alphabetical character.
#Use shorthand if-else (ternary operator) to implement this logic.

ilyas = 'b'

print("vowel" if ilyas.lower() in 'aeiou' else "consonant" if ilyas.isalpha() else "not an alphabet")
