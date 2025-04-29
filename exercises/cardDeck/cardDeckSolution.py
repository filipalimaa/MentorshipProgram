def countingCards(baralho, gaveta):
    # Count the cards in the drawer
    countCardsDrawer = {}
    for carta in gaveta:
        if carta in countCardsDrawer:
            countCardsDrawer[carta] += 1
        else:
            countCardsDrawer[carta] = 1
    
    countCardsDeck = []
    for carta in baralho:
        if carta not in countCardsDrawer:
            return 0
        countCardsDeck.append(countCardsDrawer.get(carta, 0))
    
    return min(countCardsDeck)
