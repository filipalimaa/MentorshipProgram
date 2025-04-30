<<<<<<< HEAD
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

    return min_decks


## Alternative solution
def counting_Cards(deck, drawer):
    count_Cards_Drawer = {card: 0 for card in deck}

    for card in drawer:
        if card in count_Cards_Drawer:
            count_Cards_Drawer[card] += 1

    if 0 in count_Cards_Drawer.values():
        return 0

    return min(count_Cards_Drawer.values())
=======
def countingCards(baralho, gaveta):
    # Count the cards in the drawer
    countCardsDrawer = {}
    for carta in gaveta:
        if carta in countCardsDrawer:
            countCardsDrawer[carta] += 1
        else:
<<<<<<< HEAD
            countCards[carta] = 1
>>>>>>> f98f259 (feat: count the cards in the drawer)
=======
            countCardsDrawer[carta] = 1
    
    # count the cards in the deck, check that each one is in the drawer and then count as few decks as possible.
    countCardsDeck = []
    for carta in baralho:
        if carta not in countCardsDrawer:
            return 0
        countCardsDeck.append(countCardsDrawer.get(carta, 0))
    
    return min(countCardsDeck)
>>>>>>> a5b7589 (feat: count the number of possible decks)
