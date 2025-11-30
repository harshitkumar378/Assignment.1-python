# -----------------------------------------------------------
# Name: Harshit Kumar
# Date: 30 Nov 2025
# Project: Daily Calorie Tracker CLI
# -----------------------------------------------------------

import datetime

print("\n==============================================")
print("     Welcome to the Daily Calorie Tracker!")
print("Easily track your meals, calories, and limits.")
print("==============================================\n")

# ------------------------ Task 2 ---------------------------
# Input & Data Collection

meal_names = []
calorie_values = []

num_meals = int(input("How many meals do you want to enter today? "))

for i in range(num_meals):
    print(f"\nMeal {i+1}:")
    meal = input("Enter meal name: ")
    calories = float(input("Enter calories for this meal: "))
    
    meal_names.append(meal)
    calorie_values.append(calories)

# ------------------------ Task 3 ---------------------------
# Total, average & daily limit comparison

total_calories = sum(calorie_values)
average_calories = total_calories / len(calorie_values)

daily_limit = float(input("\nEnter your daily calorie limit: "))

# ------------------------ Task 4 ---------------------------
# Exceed warning system

if total_calories > daily_limit:
    status_msg = "⚠️ WARNING: You have exceeded your daily calorie limit!"
else:
    status_msg = "✅ Good job! You are within your daily calorie limit."

# ------------------------ Task 5 ---------------------------
# Neatly formatted output

print("\n\n=========== DAILY CALORIE REPORT ===========\n")
print("Meal Name\tCalories")
print("--------------------------------------------")

for meal, cal in zip(meal_names, calorie_values):
    print(f"{meal}\t\t{cal}")

print("--------------------------------------------")
print(f"Total:\t\t{total_calories}")
print(f"Average:\t{average_calories:.2f}")
print("\n" + status_msg)
print("\n============================================\n")

# ------------------------ Task 6 (Bonus) -------------------
# Save session log

save_option = input("Do you want to save this report to a file? (yes/no): ").strip().lower()

if save_option == "yes":
    filename = "calorie_log.txt"
    with open(filename, "w", encoding="utf-8") as file:
        file.write("===== DAILY CALORIE TRACKER LOG =====\n")
        file.write(f"Timestamp: {datetime.datetime.now()}\n\n")
        
        for meal, cal in zip(meal_names, calorie_values):
            file.write(f"{meal}: {cal} calories\n")
        
        file.write("\n")
        file.write(f"Total Calories: {total_calories}\n")
        file.write(f"Average Calories: {average_calories:.2f}\n")
        file.write(f"Daily Limit: {daily_limit}\n")
        file.write(f"Status: {status_msg}\n")
        file.write("=====================================\n")

    print(f"\nReport saved to {filename} successfully!\n")
else:
    print("\nReport not saved.\n")
