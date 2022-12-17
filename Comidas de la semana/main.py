import xlrd

def export_to_list(excel_file, ingredient_codes = [1, 2, 3]):
  # Open the Excel file
  workbook = xlrd.open_workbook(excel_file)
  
  # Select the first sheet
  worksheet = workbook.sheet_by_index(0)
  
  # Create an empty list to store the data
  data = []

  # Iterate over the rows in the worksheet
  for row_num in range(1, worksheet.nrows):
    # Get the ingredient code for the current row
    ingredient_code = worksheet.cell(row_num, 1).value
    
    # If the ingredient code is in the list of ingredient codes, add the row data to the list
    if ingredient_code in ingredient_codes:
      data.append(worksheet.row_values(row_num))
    
  # Return the data
  return data

# Using food (excel_file)
data = export_to_list('food.xls')

# Use the random module to choose a food option randomly
import random

# Set the number of weeks to choose food options for
num_weeks = 2

# Set the list of days of the week
days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

# Initialize a list to store the chosen food options
chosen_foods = []

# Initialize a variable to store the ingredient code of the previous chosen food
prev_ingredient_code = 0

# Loop through the number of weeks
for week in range(num_weeks):
    # Loop through the days of the week
    for day in days_of_week:
        # If it's Monday, choose a food option with beans
        if day == 'Monday':
            chosen_food = random.choice(export_to_list('food.xls', [3]))
        else:
            # Choose a random food option with a different ingredient than the previous one
            chosen_food = random.choice(export_to_list('food.xls', [1, 2, 3]))
            while chosen_food[1] == prev_ingredient_code:
                chosen_food = random.choice(export_to_list('food.xls', [1, 2, 3]))
        
        # Add the chosen food option to the list of chosen foods
        chosen_foods.append(chosen_food)
        
        # Store the ingredient code of the chosen food
        prev_ingredient_code = chosen_food[1]
        
        # Print the chosen food option to the screen
        print(f'{day}: {chosen_food[0]}')