from datetime import datetime
from twilio.rest import Client
import time

account_sid = 'your id given to you '
auth_token = 'token given to you by twilio'
client = Client(account_sid, auth_token)

def whatsapp_message(recipient_no, message_body):
    try:
        message = client.messages.create(
            from_='whatsapp:no given to you by twilio',
            body=message_body,
            to=f'whatsapp:{recipient_no}'
        )
        print(f'Message sent successfully: {message.sid}')
    except Exception as e:
        print(f"Error sending message: {e}")

name = input('Enter recipient name: ')
recipient_no = input('Enter recipient number (with country code): ')
message_body = input(f'Enter message for {name}: ')
date_str = input('Enter date (yyyy-mm-dd): ')
time_str = input('Enter time (hh:mm:ss): ')


try:
    schedule_datetime = datetime.strptime(f'{date_str} {time_str}', "%Y-%m-%d %H:%M:%S")
    current_datetime = datetime.now()
    time_difference = schedule_datetime - current_datetime
    delay_seconds = time_difference.total_seconds()

    if delay_seconds <= 0:
        print("Error: The specified time is in the past.")
    else:
        print(f'Message scheduled for {name} at {schedule_datetime}.')
        time.sleep(delay_seconds)
        whatsapp_message(recipient_no, message_body)

except ValueError as ve:
    print(f"Invalid date/time format: {ve}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
