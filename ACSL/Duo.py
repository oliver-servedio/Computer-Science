def printResult(face_up, hand, draw_pile):
    def can_match(card1, card2):
        if len(card1) < 3 or len(card2) < 3:
            return False  # Ensure both cards have at least three components
        return (
            (card1[0] == card2[0]) or  # Match color
            (card1[1] == card2[1]) or  # Match number
            (card1[2] == card2[2])     # Match symbol
        )
    
    piles = face_up.split()
    hand = hand.split()    
    for turn in range(2):  # Two turns maximum
        played_any = False
        pile_locked = None  # Resets at the start of each turn
        i = 0
        
        while i < len(hand):
            card = hand[i]
            if len(card) < 3:
                i += 1
                continue  # Skip invalid cards
            
            if pile_locked is None:
                if can_match(card, piles[0]):
                    piles[0] = card
                    hand.pop(i)
                    played_any = True
                    pile_locked = 0  # Lock to pile 1 for this turn
                    i = 0  # Restart from the leftmost card
                    continue
                elif can_match(card, piles[1]):
                    piles[1] = card
                    hand.pop(i)
                    played_any = True
                    pile_locked = 1  # Lock to pile 2 for this turn
                    i = 0  # Restart from the leftmost card
                    continue
            elif pile_locked == 0 and can_match(card, piles[0]):
                piles[0] = card
                hand.pop(i)
                played_any = True
                i = 0  # Restart from the leftmost card
                continue
            elif pile_locked == 1 and can_match(card, piles[1]):
                piles[1] = card
                hand.pop(i)
                played_any = True
                i = 0  # Restart from the leftmost card
                continue
            i += 1
        
        if not played_any:
            break  # End if no plays are possible
        
        if turn == 0:  # Only draw cards at the end of the first turn
            draw_count = min(7 - len(hand), len(draw_pile))
            hand.extend(draw_pile[:draw_count])
            draw_pile = draw_pile[draw_count:]
    
    # Ensure the output is exactly as specified
    print(len(hand), piles[0], piles[1])

# Example usage
face_up = "R4S B3O"
hand = "R3X T B1T R1X B3X B1X Y4O"
draw_pile = "B4X Y3O B4T G2X B B3T"
printResult(face_up, hand, draw_pile)