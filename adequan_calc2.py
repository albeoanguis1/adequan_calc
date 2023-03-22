def calculate_days_supply(amount, frequency):
    total_amount = 2 * 5 # total amount in 1 box
    max_days_supply = 56 # maximum days supply with 1 box
    days_supply = total_amount / (amount * frequency) #to get the weeks

    if days_supply > max_days_supply:
        boxes_needed = days_supply / max_days_supply #how many boxes to cover the days supply
        return f"Days supply exceeds maximum. You would need {boxes_needed} box(es) to cover the days supply."
    else:
        return days_supply * 7

print(calculate_days_supply(4,2))