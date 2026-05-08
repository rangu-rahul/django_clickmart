import psycopg2
from decouple import config

# Print what decouple reads
db_name = config('DB_NAME')
db_user = config('DB_USER')
db_password = config('DB_PASSWORD')
db_host = config('DB_HOST')
db_port = config('DB_PORT')

print(f"DB_NAME     : {db_name}")
print(f"DB_USER     : {db_user}")
print(f"DB_PASSWORD : {repr(db_password)}")  # repr shows hidden chars
print(f"DB_HOST     : {db_host}")
print(f"DB_PORT     : {db_port}")
print()

# Try direct psycopg2 connection
try:
    conn = psycopg2.connect(
        dbname=db_name,
        user=db_user,
        password=db_password,
        host=db_host,
        port=db_port
    )
    print("✅ Connection SUCCESSFUL!")
    conn.close()
except Exception as e:
    print(f"❌ Connection FAILED: {e}")
