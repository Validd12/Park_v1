import sqlite3

# Connect to the database
conn = sqlite3.connect("users.db")
cursor = conn.cursor()

# Fetch and display all user records
cursor.execute("SELECT * FROM users")
users = cursor.fetchall()

# Print user data
print("User records:")
for user in users:
    print(user)

# Close the database connection
conn.close()