def all_longest(my_list: list):
    all_longest = []
    longest = 0
    for i in my_list:
        if len(i) > longest:
            longest = len(i)
    
    for i in my_list:
        if(len(i)) == longest:
            all_longest.append(i)
    return all_longest

def shortest(my_list: list):
    # Start with first word as our shortest
    shortest_word = my_list[0]
    
    # Find any word that's shorter
    for word in my_list:
        if len(word) < len(shortest_word):
            shortest_word = word
            print(f"New shortest word found: {shortest_word}")
    
    return shortest_word

if __name__ == "__main__":
    my_list = ["B", "Anna", "Bello", "Shnurki", "Tornado", "A", "", ""]
    print(all_longest(my_list))
    print(shortest(my_list))