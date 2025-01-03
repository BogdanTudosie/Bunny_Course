def length_of_longest(my_list: list):
    longest = 0
    for i in my_list:
        if len(i) > longest:
            longest = len(i)
    return longest

if __name__ == "__main__":
    my_list = ["Anna", "Bello", "Shnurki"]
    print(length_of_longest(my_list))
    