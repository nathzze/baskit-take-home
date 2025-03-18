# SQLite ETL Pipeline

## 🚀 Project Overview
This project implements an **ETL (Extract, Transform, Load) pipeline** that extracts data from a **Google Sheet**, transforms it, and loads it into an **SQLite database**.

## 📌 Features
- **Extract** data directly from Google Sheets using `gspread`.
- **Transform** data (standardize phone numbers, fix date formats, etc.).
- **Load** data into an SQLite database.
- **Verify** successful data loading with SQL queries.

## 🛠 Installation
### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/baskit-take-home.git
cd baskit-take-home
```

### 2️⃣ Create a Virtual Environment (Optional but Recommended)
```bash
python -m venv venv
source venv/bin/activate  # For macOS/Linux
venv\Scripts\activate    # For Windows
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Set Up Google Sheets API Credentials
1. Go to [Google Cloud Console](https://console.cloud.google.com/).
2. Create a new project and enable **Google Sheets API** & **Google Drive API**.
3. Generate a **Service Account JSON key**.
4. Share your Google Sheet with the Service Account email.
5. Save the JSON key as `creds.json` in the project directory.

## 🚀 Usage
### 1️⃣ Run the ETL Pipeline
```bash
python etl.py
```

### 2️⃣ Verify Data in SQLite
To open the database and run queries:
```bash
sqlite3 born_date_data.db
```
Then run:
```sql
SELECT * FROM born_date_data LIMIT 10;
```

## 📂 Project Structure
```
├── creds.json         # Google API credentials
├── etl.py             # Main ETL script
├── requirements.txt   # Required Python libraries
├── born_date_data.db  # SQLite database (auto-created)
├── README.md          # Documentation
```
## 📧 Contact
For any questions, reach out to **nathzjoseph14@gmail.com**

---
🚀 **Happy Coding!** 😊

