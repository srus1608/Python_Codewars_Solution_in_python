def guess_blue(blue_start, red_start, blue_pulled, red_pulled):
    # Calculate the number of blue and red marbles remaining
    remaining_blue = blue_start - blue_pulled
    remaining_red = red_start - red_pulled
    
    # Calculate the total number of marbles remaining
    total_remaining = remaining_blue + remaining_red
    
    # Calculate the probability of drawing a blue marble
    probability_blue = remaining_blue / total_remaining
    
    return probability_blue