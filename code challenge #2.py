def MinionGame(Word):
    Player_one_letters = "aeiou"
    Player_two_letters = "bcdfghjklmnpqrstvwxyz"
    Player_one_score = 0
    Player_two_score = 0
    Player_one_input = input("Player One Type a letter or substring")
    while Player_one_input != Word:
        if Player_one_input[0] not in Player_one_letters:
            Player_one_input = input("You have to start with a vowel")
        Player_one_score += Word.count(Player_one_input)
        print(Word.count(Player_one_input))
        Player_one_input = input("Player One Type a letter or substring")

    Player_two_input = input("Player Two Type a letter or substring")
    while Player_two_input != Word:
        if Player_two_input[0] not in Player_two_letters:
            Player_two_input = input("You have to start with a consonant")
        Player_two_score += Word.count(Player_two_input)
        print(Word.count(Player_two_input))
        Player_two_input = input("Player Two Type a letter or substring")
        
    if Player_one_score > Player_two_score:
        return "Player One Won!"
    elif Player_two_score > Player_one_score:
        return "Player Two Won!"
    return "Its a Draw!"

