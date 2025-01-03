def most_frequent_char(text: str) -> str:
   if not text:
       return None
   
   char_count = {}
   for char in text:
       char_count[char] = char_count.get(char, 0) + 1
       
   return max(char_count, key=char_count.get) # this is a function to calculate max, nothing more

if __name__ == "__main__":
    text = "aeroplane"
    print(f"Character with max occurences is: {most_frequent_char(text)}")