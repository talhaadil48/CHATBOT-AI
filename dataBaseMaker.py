import pymysql

# Database connection details
DB_HOST = "localhost"       # Change if necessary
DB_USER = "root"   # Replace with your MySQL username
DB_PASSWORD = "X9v@Pq#L3m"  # Replace with your MySQL password
DB_NAME = "chatbotproject"  # Name of your database

# Path to your SQL file
SQL_FILE = "seed.sql"  # Replace with your SQL file path

try:
    # Connect to MySQL
    connection = pymysql.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        autocommit=True  # Ensures execution of multiple statements
    )

    cursor = connection.cursor()

    # Create the database if it doesn't exist
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
    cursor.execute(f"USE {DB_NAME}")

    # Read and execute the SQL file
    with open(SQL_FILE, "r") as file:
        sql_commands = file.read()
    
    for command in sql_commands.split(";"):  # Splitting SQL commands
        command = command.strip()
        if command:
            cursor.execute(command)

    print("SQL script executed successfully!")

except pymysql.Error as e:
    print("Error executing SQL file:", e)

finally:
    cursor.close()
    connection.close()
