def countingCards(deck, drawer):
    # Count the cards in the drawer
    countCardsDrawer = {}
    for card in drawer:
        if card in countCardsDrawer:
            countCardsDrawer[card] += 1
        else:
            countCardsDrawer[card] = 1
    
    # count the cards in the deck, check that each one is in the drawer and then count as few decks as possible.
    min_decks = None
    for card in deck:
        if card not in countCardsDrawer:
            return 0
        count = countCardsDrawer[card]
        if min_decks is None or count < min_decks:
            min_decks = count
    
    return min(min_decks)
