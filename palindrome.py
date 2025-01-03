def is_palindrome(word: str):
    is_palindrome = True
    for i in range(len(word) // 2):
        first = word[i]
        last = word[len(word) - 1 - i]
        
        print(f"Comparing '{first}' with '{last}'")
        if first != last:
            is_palindrome = False
            print(f"❌ Characters don't match!")
            break
        else:
            print(f"✅ Characters match!")
            
    print("\nFinal Result:")
    if is_palindrome:
        print(f"'{word}' is a palindrome! 🎉")
    else:
        print(f"'{word}' is not a palindrome 😔")
        
if __name__ == "__main__":
    is_palindrome("odo")