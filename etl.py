import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
import sqlite3

# Load credentials from JSON file
SERVICE_ACCOUNT_FILE = "creds.json" 

# Define scope and authenticate
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name(SERVICE_ACCOUNT_FILE, scope)
client = gspread.authorize(creds)

# Open Google Sheet 
SHEET_NAME = "Take Home Test Data Engineer Baskit" 
spreadsheet = client.open(SHEET_NAME)

worksheet = spreadsheet.worksheet("data") # Data is stored in this sheet

# Skip first row and make second row as column names
data = worksheet.get_all_values()
df = pd.DataFrame(data[2:], columns=data[1])

# Function to standardize phone numbers
def standardize_phone(phone):
    phone = str(phone).strip()
    if phone.startswith("62"):
        return phone 
    elif phone.startswith("8"):  
        return "62" + phone[1:]  
    return phone

df["phone_number"] = df["phone_number"].apply(standardize_phone)

def standardize_date(date):
    if pd.isna(date):
        return None  # Handle missing values

    date = str(date).strip().replace("/", "-") 
    
    try:
        return pd.to_datetime(date, errors='coerce').strftime('%Y-%m-%d')
    except:
        return None  # Handle invalid dates
    
df["born_day"] = df["born_day"].apply(standardize_date)

# Define sqlite database
conn = sqlite3.connect("born_date_data.db")

cursor = conn.cursor()

# Create table if not exists
cursor.execute("""
CREATE TABLE IF NOT EXISTS born_date_data (
    id TEXT PRIMARY KEY,
    name TEXT,
    phone_number TEXT,
    born_day DATE
)
""")

# Insert data into SQLite
df.to_sql("born_date_data", conn, if_exists="replace", index=False)

# Verify data was inserted
print(pd.read_sql("SELECT * FROM born_date_data LIMIT 5", conn))
print(pd.read_sql("SELECT COUNT(*) FROM born_date_data", conn))

# Close the connection
conn.close()
