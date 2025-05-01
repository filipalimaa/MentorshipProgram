def countingCards(deck, drawer):
    # Count the cards in the drawer
    countCardsDrawer = {}
    for card in drawer:
        if card in countCardsDrawer:
            countCardsDrawer[card] += 1
        else:
            countCardsDrawer[card] = 1
    
    # count as few decks as possible
    countCardsDeck = []
    for carta in baralho:
        if carta not in countCardsDrawer:
            return 0
        count = countCardsDrawer[card]
        if min_decks is None or count < min_decks:
            min_decks = count
    
    return min(countCardsDeck)
