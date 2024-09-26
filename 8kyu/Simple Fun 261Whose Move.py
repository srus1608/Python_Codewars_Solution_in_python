def whose_move(last_player, win):
    if win:
        # If the current player won, they continue to move
        return last_player
    else:
        # If the current player lost, the other player moves
        return "white" if last_player == "black" else "black"