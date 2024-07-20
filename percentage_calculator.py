print("Instructions:\n-- Enter a number.\n-- Then enter a number to determine what percentage it is of the total number")

def calculate_percentage(total, part):
    
    if total == 0:
        return 0
    percentage = (part / total) * 100
    return percentage

#total_amount you want to calculate for
total_number = float(input("Enter total number: "))

# What part of the total number you want to determine what percentage of the total number it is
part_amount = float(input("Enter part amount: "))

result = calculate_percentage(total_number, part_amount)
print(f"{part_amount} is {round(result, 2)}% of {total_number}")
