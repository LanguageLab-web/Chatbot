import json
import time
from datetime import datetime

def load_logs():
    try:
        with open('logs.json', 'r') as file:
            logs = json.load(file)
        return logs
    except Exception as e:
        print(f"Error loading logs: {e}")
        return []

def derive_data_from_logs(logs, date):
    rooms_booked = 0
    rooms_available = None
    airline_messages = 0

    for log in logs:
        timestamp = log.get("timestamp", "")
        message = log.get("message", "").lower()

        if timestamp.startswith(date):
            if "rooms booked" in message:
                try:
                    rooms_booked += int(message.split()[-1]) 
                except ValueError:
                    continue
            elif "override rooms" in message:
                try:
                    rooms_available = int(message.split()[-1]) 
                except ValueError:
                    continue
            elif "airlines" in message:
                airline_messages += 1

    if rooms_available is None:
        rooms_available = 30

    return rooms_booked, rooms_available, airline_messages

def generate_report(logs, date=None):
    if not logs:
        return "No log data available to generate a report."
    
    if date:
        filtered_logs = [log for log in logs if log.get("timestamp", "").startswith(date)]
    else:
        today = datetime.now().strftime("%Y-%m-%d")
        filtered_logs = [log for log in logs if log.get("timestamp", "").startswith(today)]
    
    if not filtered_logs:
        return f"No logs found for {date or 'today'}."

    rooms_booked, rooms_available, messages_from_airlines = derive_data_from_logs(filtered_logs, date or datetime.now().strftime("%Y-%m-%d"))

    report = f"📊 Report for {date or 'today'}\n"
    report += f"- Rooms Booked: {rooms_booked}\n"
    report += f"- Rooms Available: {rooms_available}\n"
    report += f"- Messages from Airlines: {messages_from_airlines}\n"
    
    return report

def royal_plaza_bot(command, logs):
    """Simulate responses from the 'Royal Plaza Singapore' bot"""
    if command.startswith("report"):
        parts = command.split()
        date = parts[1] if len(parts) > 1 else None
        return generate_report(logs, date)
    elif command.startswith("rooms booked"):
        date = command.split()[-1]
        return f"Royal Plaza Singapore: Rooms booked on {date} are 15."
    elif command.startswith("rooms available"):
        date = command.split()[-1]
        return f"Royal Plaza Singapore: Rooms available on {date} are 25."
    elif command == "airlines number":
        return "Royal Plaza Singapore: The airlines number is 12345."
    elif command.startswith("airlines number"):
        number = command.split()[-1]
        return f"Royal Plaza Singapore: Airlines number updated to {number}."
    elif command.startswith("override rooms"):
        parts = command.split()
        date = parts[2]
        rooms = parts[3]
        return f"Royal Plaza Singapore: Rooms available on {date} overridden to {rooms}."
    elif command == "start":
        return "Royal Plaza Singapore: Application started."
    elif command == "shutdown":
        return "Royal Plaza Singapore: Application shutting down."
    elif command.startswith("change hotel employee number"):
        number = command.split()[-1]
        return f"Royal Plaza Singapore: Hotel employee number changed to {number}."
    elif command == "hotel employee number":
        return "Royal Plaza Singapore: Hotel employee number is 9876."
    else:
        return "Royal Plaza Singapore: Command not recognized."

def faisal_mss_bot(command, logs):
    """Simulate responses from the 'Faisal MSS' bot"""
    if command.startswith("report"):
        parts = command.split()
        date = parts[1] if len(parts) > 1 else None
        return generate_report(logs, date)
    elif command.startswith("rooms booked"):
        date = command.split()[-1]
        return f"Faisal MSS: Rooms booked on {date} are 12."
    elif command.startswith("rooms available"):
        date = command.split()[-1]
        return f"Faisal MSS: Rooms available on {date} are 18."
    elif command == "airlines number":
        return "Faisal MSS: The airlines number is 67890."
    elif command.startswith("airlines number"):
        number = command.split()[-1]
        return f"Faisal MSS: Airlines number updated to {number}."
    elif command.startswith("override rooms"):
        parts = command.split()
        date = parts[2]
        rooms = parts[3]
        return f"Faisal MSS: Rooms available on {date} overridden to {rooms}."
    elif command == "start":
        return "Faisal MSS: Application started."
    elif command == "shutdown":
        return "Faisal MSS: Application shutting down."
    elif command.startswith("change hotel employee number"):
        number = command.split()[-1]
        return f"Faisal MSS: Hotel employee number changed to {number}."
    elif command == "hotel employee number":
        return "Faisal MSS: Hotel employee number is 1234."
    else:
        return "Faisal MSS: Command not recognized."

def handle_user_input():
    logs = load_logs()  
    
    print("You can try the following messages to command the bot:\n")
    print("1. Type report")
    print("2. Type rooms booked <yyyy-mm-dd>")
    print("3. Type rooms available <yyyy-mm-dd>")
    print("4. Type airlines number")
    print("5. Type airlines number <65xxxxxxxx>")
    print("6. Type override rooms <yyyy-mm-dd> <xx>")
    print("7. Type start")
    print("8. Type shutdown")
    print("9. Type change hotel employee number <number>")
    print("10. Type hotel employee number")
    print("11. Type report <yyyy-mm-dd>")

    while True:
        user_input = input("\nEnter a command: ").strip()

        if user_input == "exit":
            print("Exiting the bot.")
            break

        if user_input:
            response_royal_plaza = royal_plaza_bot(user_input, logs)
            print(f"\n{response_royal_plaza}")

        if user_input:
            time.sleep(2)
            response_faisal_mss = faisal_mss_bot(user_input, logs)
            print(f"\n{response_faisal_mss}")

if __name__ == "__main__":
    handle_user_input()
