# Name: Yash Jorwekar
# Project: Personal Information Manager
# Description: A beginner Python program that stores static personal
# information and collects user input to display formatted output.

# Welcome header
print("=" * 40)
print("   PERSONAL INFORMATION MANAGER")
print("=" * 40)
print()

# Static personal information
name = "Yash Jorwekar"
age = 20
city = "Pune"
hobby = "Playing Badminton"

# Introduction section
print("Tell us a little about yourself:")
print("-" * 32)

# Get user's favorite food with validation
while True:
    favorite_food = input("What is your favorite food? ").strip()
    if favorite_food:
        break
    print("Input cannot be empty. Please try again.")

# Get user's favorite color with validation
while True:
    favorite_color = input("What is your favorite color? ").strip()
    if favorite_color:
        break
    print("Input cannot be empty. Please try again.")

# Calculate age in months
age_in_months = age * 12

# Display user information
print("\n" + "=" * 40)
print("        YOUR INFORMATION")
print("=" * 40)
print()
print(f"Name: {name}")
print(f"Age: {age} years ({age_in_months} months old)")
print(f"City: {city}")
print(f"Hobby: {hobby}\n")
print(f"Favorite Food: {favorite_food}")
print(f"Favorite Color: {favorite_color}")
print()
print("=" * 40)
print("Thank you for using this program!")

