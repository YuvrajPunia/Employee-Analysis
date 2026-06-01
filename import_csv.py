import sys
import mysql.connector          # ← import BEFORE pandas
import pandas as pd

print("All libraries loaded.", flush=True)

df = pd.read_csv("Employee.csv")
df.columns = df.columns.str.strip()

print(f"CSV loaded: {len(df)} rows", flush=True)
print(df.head(2).to_string(), flush=True)

conn = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="Ctmz2020@",
    database="employee_db",
    connection_timeout=30
)
cursor = conn.cursor()
print("Connected to MySQL.", flush=True)

# Clear any previous test data first
cursor.execute("TRUNCATE TABLE employees")
conn.commit()
print("Table cleared.", flush=True)

# Build all rows as a list of tuples
rows = [
    (
        str(row["Education"]),
        int(row["JoiningYear"]),
        str(row["City"]),
        int(row["PaymentTier"]),
        int(row["Age"]),
        str(row["Gender"]),
        str(row["EverBenched"]),
        int(row["ExperienceInCurrentDomain"]),
        int(row["LeaveOrNot"])
    )
    for _, row in df.iterrows()
]

print(f"Rows prepared: {len(rows)}", flush=True)

cursor.executemany("""
    INSERT INTO employees
    (Education, JoiningYear, City, PaymentTier, Age,
     Gender, EverBenched, ExperienceInCurrentDomain, LeaveOrNot)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
""", rows)

conn.commit()
print(f"Done. Rows inserted: {cursor.rowcount}", flush=True)

cursor.close()
conn.close()