#Question


# Given a string of digits 2 to 9 a user has pressed on a T9 “old school” telephone keypad, 
# return a list of all letter combinations they could have been trying to type on the keypad.
# Example execution 1:  t9_letters("23")  ⇒  ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"])
# Example execution 2:  t9_letters("4663")  ⇒  ["gmmd", …, "gone", …, "good", …, "home", …, "hood", …, "ioof"]

#Solution

def t9_letters(digits):
    # Step 1: Create a dictionary mapping each digit to the corresponding letters on the T9 keypad
    keypad = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
    }

    # Step 2: Create a list containing the first set of letters (i.e., the letters corresponding to the first digit)
    letters = [char for char in keypad[digits[0]]]

    # Step 3: For each subsequent digit in the input string, create a new list containing all possible combinations of the current letters and the letters corresponding to the current digit
    for digit in digits[1:]:
        new_letters = []

        for letter in keypad[digit]:
            for item in letters:
                new_letters.append(item + letter)

        letters = new_letters

    # Step 4: Return the final list of letter combinations
    return letters
