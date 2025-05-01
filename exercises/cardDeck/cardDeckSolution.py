def countingCards(deck, drawer):
    # Count the cards in the drawer
    countCardsDrawer = {}
    for card in drawer:
        if card in countCardsDrawer:
            countCardsDrawer[card] += 1
        else:
            countCardsDrawer[carta] = 1

    # count as few decks as possible
    countCardsDeck = []
    for carta in baralho:
        if carta not in countCardsDrawer:
            return 0
        countCardsDeck.append(countCardsDrawer.get(carta, 0))

    return min(countCardsDeck)
