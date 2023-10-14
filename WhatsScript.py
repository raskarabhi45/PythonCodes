import pywhatkit as kit
import schedule
import time

# Define a list of phone numbers
phone_numbers = ["+919322169689", "+919112785366", "+919325961017"]  # Add more numbers as needed

# Define the message you want to send
message = "Good Morning"

# Define the time (in 24-hour format) when you want to send the message
hour = 13
minute = 22

# Function to send the message to multiple numbers
def send_messages():
    for phone_number in phone_numbers:
        kit.sendwhatmsg(phone_number, message, hour, minute)
        time.sleep(2)  # Add a delay between sending messages to avoid rate limiting

# Schedule the message sending every 5 minutes
schedule.every(5).minutes.do(send_messages)

# Infinite loop to run the scheduler
while True:
    schedule.run_pending()
    time.sleep(1)
