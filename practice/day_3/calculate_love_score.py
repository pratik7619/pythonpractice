def calculate_love_score(name1, name2):
    # need to combine both names
    combined_names = (name1 + name2).lower()

    # calculate chars for true
    true_count = sum(combined_names.count(char) for char in 'true')

    # calculate love count
    love_count = sum(combined_names.count(char) for char in 'love')

    print(int(f'{true_count}{love_count}'))


calculate_love_score("Pratik", "Radha")
