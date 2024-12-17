import time
import csv
from datetime import datetime
from mfrc522 import SimpleMFRC522  # Install this library for RFID handling

# Initialize the RFID Reader
reader = SimpleMFRC522()

# File to store attendance
ATTENDANCE_FILE = "attendance_log.csv"

# Function to initialize CSV file with headers
def initialize_csv():
    try:
        with open(ATTENDANCE_FILE, mode='x', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["RFID ID", "Name", "Date", "Time"])
            print("Attendance file created successfully.")
    except FileExistsError:
        print("Attendance file already exists. Ready to log attendance.")

# Function to register attendance
def register_attendance(rfid_id, name):
    now = datetime.now()
    date = now.strftime("%Y-%m-%d")
    time_str = now.strftime("%H:%M:%S")

    # Log to CSV file
    with open(ATTENDANCE_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([rfid_id, name, date, time_str])

    print(f"\nAttendance Recorded:\nName: {name}\nRFID ID: {rfid_id}\nDate: {date}\nTime: {time_str}\n")

# Function to map RFID IDs to names
def get_name_from_rfid(rfid_id):
    # Predefined RFID IDs mapped to names
    rfid_mapping = {
        "1234567890": "John Doe",
        "9876543210": "Jane Smith",
        "1122334455": "Brettney Shane M. Francisco",  # Add your ID here
    }

    return rfid_mapping.get(str(rfid_id), "Unknown User")

# Main Program Loop
if __name__ == "__main__":
    print("Welcome to the RFID Attendance System")
    print("Place your RFID card near the reader to register attendance.\n")

    initialize_csv()

    try:
        while True:
            print("Waiting for RFID card...")
            rfid_id, _ = reader.read()  # Read RFID ID
            print("RFID Card Detected!")

            # Get user name from RFID ID
            name = get_name_from_rfid(rfid_id)
            register_attendance(rfid_id, name)

            print("Attendance registered. Please remove your card.\n")
            time.sleep(2)  # Wait to avoid duplicate readings

    except KeyboardInterrupt:
        print("\nProgram terminated. Goodbye!")
