# Define the production rules
'''rules = [
    {"if": "temperature < 68", "then": "turn_on_heater"},
    {"if": "temperature > 72", "then": "turn_on_air_conditioner"},
    {"if": "68 <= temperature <= 72", "then": "do_nothing"}
]

# Define a function to evaluate the rules
def evaluate_rules(temperature):
    actions = []
    for rule in rules:
        if eval(rule["if"]):
            actions.append(rule["then"])
    return actions

# Define the temperature condition (you can change this value)
current_temperature = 70

# Evaluate the rules based on the current temperature
actions = evaluate_rules(current_temperature)

# Output the current temperature
print(f"Current temperature: {current_temperature}°F")

# Perform the actions
for action in actions:
    if action == "turn_on_heater":
        print("Turning on the heater")
        # Code to turn on the heater goes here
    elif action == "turn_on_air_conditioner":
        print("Turning on the air conditioner")
        # Code to turn on the air conditioner goes here
    elif action == "do_nothing":
        print("Doing nothing")
    else:
        print("Unknown action")
'''

# Define the production rules for the alarm clock system
rules = [
    {"if": "day == 'Weekday' and user_preference == 'EarlyRiser'", "then": "set_alarm('6:00 AM')"},
    {"if": "day == 'Weekday' and user_preference == 'Normal'", "then": "set_alarm('7:30 AM')"},
    {"if": "day == 'Weekend' and user_preference == 'LateRiser'", "then": "set_alarm('9:00 AM')"},
    {"if": "day == 'Weekend' and user_preference == 'Normal'", "then": "set_alarm('8:00 AM')"},
    {"if": "day == 'Weekend' and user_preference == 'EarlyRiser'", "then": "set_alarm('7:00 AM')"},
]

# Define a function to set the alarm time
def set_alarm(time):
    print(f"Alarm set for {time}")

# Define the current day and user preference
day = 'Weekday'  # Can be 'Weekday' or 'Weekend'
user_preference = 'EarlyRiser'  # Can be 'EarlyRiser', 'Normal', or 'LateRiser'

# Evaluate the rules based on the current day and user preference
for rule in rules:
    if eval(rule["if"]):
        exec(rule["then"])

# Output the current day and user preference
print(f"Today is {day}. User preference: {user_preference}")
