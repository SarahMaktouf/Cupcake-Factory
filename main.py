import random
# Display a heading in the console.
print("CUPCAKE FACTORY 🧁🍭")

# Initialise the number of days (NOT designed to be changed).
num_days = 7
# Initialise variables for the number of weekly cupcakes produced.
weekly_good_num_cupcakes = 0
weekly_defective_num_cupcakes = 0
weekly_num_cupcakes = 0

# Create "best" and "worst" day variables to store day number.
best_day = 0
worst_day = 0
# Initialise best and worst total cupcakes produced in a day.
# (work our way up from 0 and work our way down from infinity.)
best_total = 0
worst_total = float('inf')

# Every day, repeat the following indented instructions.
for day in range(num_days):

    print(f"\n🍒DAY {day + 1}")
    daily_good_num_cupcakes = 0
    daily_defective_num_cupcakes = 0
    daily_num_cupcakes = 0

    # The factory works 8 hours per day.
    num_hours = 8
    for hour in range (num_hours):

        # Each hour, the factory produces a random number of cupcakes (10 to 100).
        hourly_num_cupcakes = random.randint (10, 100)

        # About 10% of cupcakes are randomly defective.
        hourly_defective_num_cupcakes = round(hourly_num_cupcakes * random.uniform(0.08, 0.12))
        # Defective cupcakes discarded.
        hourly_good_num_cupcakes = hourly_num_cupcakes - hourly_defective_num_cupcakes

        # Hourly cupcakes are added to the daily total.
        daily_good_num_cupcakes += hourly_good_num_cupcakes
        daily_defective_num_cupcakes += hourly_defective_num_cupcakes
        daily_num_cupcakes += hourly_num_cupcakes

    # Daily cupcakes are added to the weekly total.
    weekly_good_num_cupcakes += daily_good_num_cupcakes
    weekly_defective_num_cupcakes += daily_defective_num_cupcakes
    weekly_num_cupcakes += daily_num_cupcakes

    # Display number of cupcakes produced in the console for the day.
    print(f"  😛Good cupcakes produced: {daily_good_num_cupcakes}")
    print(f"  😵Defective cupcakes produced: {daily_defective_num_cupcakes}")
    print(f"  🔹Total cupcakes produced: {daily_num_cupcakes}")

    # Calculate and display the average number of good cupcakes produced in an hour for the day.
    average_num_good_hourly_cupcakes = round(daily_good_num_cupcakes / num_hours)
    print(f"  🔶Average good cupcakes produced per hour: {average_num_good_hourly_cupcakes}")

    # Evaluate if the day's number of cupcakes produced is the highest or lowest achieved yet.
    # If so, make this day the best/worst production day (for now).
    if daily_num_cupcakes > best_total:
        best_total = daily_num_cupcakes
        best_day = day + 1

    if daily_num_cupcakes < worst_total:
        worst_total = daily_num_cupcakes
        worst_day = day + 1
###

# Calculate the average number of good cupcakes produced daily for this week.
average_num_good_daily_cupcakes = round(weekly_good_num_cupcakes / num_days)

# Display the weekly report on the console.
print("\n🍩WEEKLY REPORT")
print(f"  😛Total good cupcakes produced: {weekly_good_num_cupcakes}")
print(f"  😵Total defective cupcakes produced: {weekly_defective_num_cupcakes}")
print(f"  🔹Total cupcakes produced: {weekly_num_cupcakes}")
print(f"  🔶Average good cupcakes produced per day: {average_num_good_daily_cupcakes}")
print(f"  🔋Best production day: Day {best_day} with {best_total} total cupcakes")
print(f"  🪫Worst production day: Day {worst_day} with {worst_total} total cupcakes")