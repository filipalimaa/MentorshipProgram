def countingCards(baralho, gaveta):
    # Count the cards in the drawer
    countCards = {}
    for carta in gaveta:
        if carta in countCards:
            countCards[carta] += 1
        else:
            countCards[carta] = 1