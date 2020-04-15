def black_jack(player, dealer):
    if (total_hand(player) == 21):
        print("BLACKJACK! YOU WIN!")
    if (total_hand(player) > 21):
        print("BUSTED! You Lose")
    if (total_hand(dealer) == 21):
        print("BLACKJACK! Sorry You Lose! Dealer Wins")
    if (total_hand(dealer) > 21):
        print("Dealer Busted! You Win!")
    if (total_hand(player) == 21) and (total_hand(dealer) == 21):         
        print("Player And Dealer Tie! Game Goes To Dealer")
    
    return True