# Prompt for a single task
task = input("Enter your task: ")

# Prompt for the task's priority
priority = input("Priority (high/medium/low): ").lower()

# Prompt to check if the task is time-bound
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Use match case to handle different priorities and time sensitivity
match priority:
    case "high":
        reminder = f"'{task}' is a high priority task"
    case "medium":
        reminder = f"'{task}' is a medium priority task"
    case "low":
        reminder = f"'{task}' is a low priority task"
    case _:
        reminder = f"'{task}' has an invalid priority"

# Modify reminder based on whether the task is time-bound
if time_bound == "yes":
    reminder += " that requires immediate attention today!"
elif time_bound == "no":
    reminder += ". Consider completing it when you have free time."
else:
    reminder = "Invalid input for time-bound question."

# Print the final reminder
print(f"Reminder: {reminder}")
