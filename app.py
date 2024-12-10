import sys
import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from enum import Enum

# Ensure `main.py` is importable
sys.path.append(os.getcwd())  # Adds current directory to the system path

# Import relevant logic and data models from `main.py`
from main import (
    load_logs,
    generate_report,
    BookingResponse,
    NumberOfRooms,
    ConfirmationResponse,
    OverrideResponse,
    PhoneNumberResponse,
    BasicExtraction,
    royal_plaza_bot,  # Example function, adjust based on your main.py
)

app = FastAPI()


@app.get("/")
async def root():
    """
    Root endpoint for testing server availability.
    """
    return {"message": "Server is running!"}


@app.post("/extract_info")
async def extract_info(data: BasicExtraction):
    """
    Extracts information from the provided request data.

    **Expected request body format:**

    ```json
    {
        "text": "Your text data containing information to be extracted"
    }
    ```

    **Response format:**

    ```json
    {
        "message": "Information extracted successfully",
        "extracted_data": {}
    }
    ```
    """
    try:
        # Placeholder logic for information extraction
        extracted_data = {
            "text_length": len(data.text),  # Example of processing the input text
            "uppercase_count": sum(1 for c in data.text if c.isupper())
        }
        return {"message": "Information extracted successfully", "extracted_data": extracted_data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/generate_report/{date}")
async def get_report(date: str):
    """
    Generates a report for the given date.

    **Path Parameter:**
    - `date`: Date in `yyyy-mm-dd` format.

    **Response format:**

    ```json
    {
        "report": "Generated report string"
    }
    ```
    """
    try:
        logs = load_logs()  # Load logs from the existing function
        report = generate_report(logs, date)  # Generate report based on the logs
        return {"report": report}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/rooms/booked")
async def booked_rooms(response: BookingResponse):
    """
    Handles booking data sent by clients.

    **Request Body:**
    ```json
    {
        "date": "yyyy-mm-dd",
        "rooms_booked": 15
    }
    ```
    """
    # Example placeholder for booking logic
    message = f"Rooms booked for {response.date}: {response.rooms_booked}"
    return {"message": message}


@app.post("/rooms/override")
async def override_rooms(data: OverrideResponse):
    """
    Override room availability for a specific date.

    **Request Body:**
    ```json
    {
        "date": "yyyy-mm-dd",
        "rooms": 20,
        "message": "Override request by admin."
    }
    ```
    """
    try:
        # Example override logic
        message = f"Room availability for {data.date} overridden to {data.rooms}. {data.message}"
        return {"message": message}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/airlines/phone_number")
async def get_phone_number():
    """
    Retrieves the airline's phone number.

    **Response format:**

    ```json
    {
        "phone_number": "12345"
    }
    ```
    """
    return {"phone_number": "12345"}  # Replace with dynamic logic if needed}
