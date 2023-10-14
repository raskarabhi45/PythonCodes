import pywhatkit as kit
import datetime
import time

def send_whatsapp_message(phone_number, message, hour, minute):
    try:
        now = datetime.datetime.now()
        scheduled_time = now.replace(hour=hour, minute=minute, second=0, microsecond=0)

        # Calculate the time difference from now to the scheduled time
        time_diff = scheduled_time - now
        seconds_diff = time_diff.total_seconds()

        if seconds_diff > 0:
            # Wait until it's time to send the message
            print(f"Waiting for {seconds_diff} seconds...")
            time.sleep(seconds_diff)

            # Send the message
            kit.sendwhatmsg(phone_number, message, hour, minute)
            print("WhatsApp message sent successfully!")

        else:
            print("Scheduled time should be in the future.")

    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    phone_number = "+919322169689"  # Replace this with the recipient's phone number (include country code)
    message = "Hello, this is an automated message!"
    hour = 11  # Replace with the hour you want to send the message (24-hour format)
    minute = 30 # Replace with the minute you want to send the message

    send_whatsapp_message(phone_number, message, hour, minute)
