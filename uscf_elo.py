def expected_score(rating1, rating2):
    return 1 / (1 + 10**((rating2 - rating1) / 400))

def update_rating(rating, expected, actual, k_factor=32):
    return rating + k_factor * (actual - expected)

def main():
    your_rating = int(input("Enter your current chess rating: "))
    number_of_games = int(input("Enter the number of games you played in the tournament: "))

    new_rating = your_rating
    for i in range(number_of_games):
        opponent_rating = int(input(f"Enter the rating of opponent {i + 1}: "))
        result = float(input(f"Enter your result against opponent {i + 1} (1 for win, 0.5 for draw, 0 for loss): "))
        
        expected = expected_score(new_rating, opponent_rating)
        new_rating = update_rating(new_rating, expected, result)

    print(f"Your estimated rating after the tournament is: {int(new_rating)}")

if __name__ == "__main__":
    main()
