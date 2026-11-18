# 1. Get Ticket ID it the TCK- format
ticket_id = input("Enter the ticket ID: ")
cleaned_id = ticket_id.strip().upper()
prefix = "TCK-"
suffix = cleaned_id[len(prefix):]
is_number_valid = suffix.isdigit()   # Extract the part after the prefix and check if it's all digits

# 2. Priority: high, medium or low
priority = input("What is the ticket priority? ")
cleaned_priority = priority.strip().lower()

# 3. Hours since the ticket was opened (decimals allowed)
raw_hours = input("Enter hours since the ticket was opened: ").strip()

# 4. Has a first response been sent? (yes or no)
response_yet = input("Has a first reponse been sent yet? ")
cleaned_response = response_yet.strip().lower()

# 5. Does the ticket ID start with TCK-, or not full, or not complete with digits.
if not cleaned_id.startswith(prefix):
    print(f"Ticket {cleaned_id} is invalid. Must start with {prefix}.")

elif cleaned_id == prefix:
    print(f"Ticket ID {cleaned_id} is incomplete. Please provide the full ticket ID.")

elif not is_number_valid:
    print(f"Ticket {cleaned_id} has an invalid ID format. Please provide a valid ticket ID.")

# 6. Otherwise, if the priority is not one of the three: say so and list the accepted values.
elif cleaned_priority not in ["low", "medium", "high"]:
    print(f"Ticket {cleaned_id} has an invalid priority. Accepted values are high, medium, or low.")

# 7. Check if input is not a negative number
elif raw_hours.startswith("-") and raw_hours[1:].replace(".", "", 1).isdigit():
    print(f"Hours entered {raw_hours} is invalid. Must be 0 or greater.")

# 8. check if the input is not a valid decimal or whole number
elif not (raw_hours.isdigit() or (raw_hours.count(".") == 1 and raw_hours.replace(".", "").isdigit())):
    print(f"Hours entered ('{raw_hours}') is invalid. Please enter a valid number(digit).")

# 9. Check if the response is acceptable
elif cleaned_response not in ["yes", "no", "y", "n"]:
    print(f"Response {cleaned_response} is invalid. You can only answer yes or no")

else:
    # Convert raw_hours to float after confirming it is valid
    hours_since_opened = float(raw_hours)
    
    # Check if a response has already been sent
    if cleaned_response in ["yes", "y"]:
        print (f"Ticket {cleaned_id}: No action needed. A first response was sent.")
    else:
        # Assign numeric targets
        if cleaned_priority == "high":
            target = 1
        elif cleaned_priority == "medium":
            target = 4
        else:
            target = 24

        # Evaluate the ticket status
        if hours_since_opened > target:
            breached_by = hours_since_opened - target
            print(f"Ticket {cleaned_id} is BREACHED by {breached_by:.2f} hours.")
        elif hours_since_opened >= (0.8 * target):
            remaining = target - hours_since_opened
            print(f"Ticket {cleaned_id} is AT RISK. Time remaining: {remaining:.2f} hours.")
        else:
            remaining = target - hours_since_opened
            print(f"Ticket {cleaned_id} is ON TRACK. Time remaining: {remaining:.2f} hours.")
            