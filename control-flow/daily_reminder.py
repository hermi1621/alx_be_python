# daily_reminder.py

def main():
    # Prompt for task details
    task = input("Enter your task: ")
    priority = input("Enter priority (high/medium/low): ").lower()
    time_bound = input("Is this task time-bound? (yes/no): ").lower()
    
    # Process priority with if-elif-else
    if priority == "high":
        reminder = f"❗ HIGH PRIORITY: {task}"
    elif priority == "medium":
        reminder = f"⚠️ MEDIUM PRIORITY: {task}"
    elif priority == "low":
        reminder = f"🔹 LOW PRIORITY: {task}"
    else:
        print("Invalid priority level. Using default reminder.")
        reminder = f"REMINDER: {task}"
    
    # Check time sensitivity
    if time_bound == "yes":
        reminder += " ⏰ (Time-sensitive! Act now!)"
    elif time_bound != "no":
        print("Assuming task is not time-bound.")
    
    # Print final reminder
    print("\n--- Your Reminder ---")
    print(reminder)

if name == "main":
    main()
