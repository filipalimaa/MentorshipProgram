def countingCards(deck, drawer):
    # Count the cards in the drawer
    countCardsDrawer = {}
    for card in drawer:
        if card in countCardsDrawer:
            countCardsDrawer[card] += 1
        else:
            countCardsDrawer[card] = 1
    
    # count the cards in the deck, check that each one is in the drawer and then count as few decks as possible.
    countCardsDeck = []
    for card in deck:
        if card not in countCardsDrawer:
            return 0
        countCardsDeck.append(countCardsDrawer.get(card, 0))
    
    return min(countCardsDeck)
