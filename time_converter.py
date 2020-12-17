#!/usr/local/bin/python3
# Made by @swisscoding on Instagram
# Follow now and share!

from colored import stylize, fg

# decoration
print(stylize("\n---- | Convert time units | ----\n", fg("red")))

# options
print(stylize("Options:", fg("green")))
print("> 'd' for days\n> 'h' for hours\n> 'm' for minutes\n> 's' for seconds\n")

# user interaction
user_input = float(input("Enter your value: "))
input_unit = input("What unit is your input?\n").lower()
output_unit = input("What unit do you want for output?\n").lower()

print(stylize("\n------------------------------------", fg("red")))

if input_unit == "d":
    if output_unit == "h":
        print(f"\n{user_input} day/s in hours: {round(user_input*24, 2)}\n")
    if output_unit == "m":
        print(f"\n{user_input} day/s in minutes: {round(user_input*24*60, 2)}\n")
    if output_unit == "s":
        print(f"\n{user_input} day/s in seconds: {round(user_input*24*60*60, 2)}\n")

elif input_unit == "h":
    if output_unit == "d":
        print(f"\n{user_input} hour/s in days: {round(user_input/24, 2)}\n")
    if output_unit == "m":
        print(f"\n{user_input} hour/s in minutes: {round(user_input*60, 2)}\n")
    if output_unit == "s":
        print(f"\n{user_input} hour/s in seconds: {round(user_input*60*60, 2)}\n")

elif input_unit == "m":
    if output_unit == "d":
        print(f"\n{user_input} minute/s in days: {round(user_input/60/24, 2)}\n")
    if output_unit == "h":
        print(f"\n{user_input} minute/s in hours: {round(user_input/24, 2)}\n")
    if output_unit == "s":
        print(f"\n{user_input} minute/s in seconds: {round(user_input*60, 2)}\n")

elif input_unit == "s":
    if output_unit == "d":
        print(f"\n{user_input} second/s in days: {round(user_input/60/60/24, 2)}\n")
    if output_unit == "h":
        print(f"\n{user_input} second/s in hours: {round(user_input/60/60, 2)}\n")
    if output_unit == "m":
        print(f"\n{user_input} second/s in minutes: {round(user_input/60, 2)}\n")

else:
    print("\nInvalid Input\n")

print(stylize("------------------------------------\n", fg("red")))
