

score_map = {
    1 : "straight flush",
    2 : "4 of a kind",
    3 : "full house",
    4 : "flush",
    5 : "straight",
    6 : "3 of a kind",
    7 : "2 pair",
    8 : "pair",
    9 : "nothing",
}







def evaluate_winner(flops, players):
    if len(flops) != 5:
        print("we need 5 cards in the middle. Something wen wrong")
        exit(2)
    if len(players) <= 1:
        print("you must have at least 2 players. Something wen wrong")
        exit(2)






def evaluate_score_player_cards(player_cards_plus_5mid):
    type_counts = []
    for card in player_cards_plus_5mid:
        type_counts.append(len(player_cards_plus_5mid.filter(lambda c: c.face == card.face)))


#     to research: lambda functions and filter and map


