task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")
match priority:
    case "high":
        if time_bound == "yes":
            print(
                f"Reminder: {task} is a high priority task that requires immediate attention today!"
            )
        else:
            print(
                f"Note: {task} is a low priority task. Consider completing it when you have free time."
            )
    case "medium":
        if time_bound == "yes":
            print(f"Reminder: {task} should be done soon, but not immediately.")
        else:
            print(f"Note: {task} is of moderate importance and can be scheduled later.")
    case "low":
        if time_bound == "yes":
            print(
                f"Reminder: {task} can be done at your convenience, but should not be delayed too long."
            )
        else:
            print(f"Note: {task} is not urgent and can be done whenever you have time.")
