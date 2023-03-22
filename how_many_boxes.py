from math import ceil

def calculate_boxes_needed(initial_dose, frequency):
    total_amount = 2 * 5 # total amount in 1 box
    amount_per_week = initial_dose * frequency
    weeks_supply_per_box = total_amount / amount_per_week
    boxes_needed = ceil(4 / weeks_supply_per_box)
    
    return f"You need {boxes_needed} boxes to cover the 1st month."

print(calculate_boxes_needed(4,2))