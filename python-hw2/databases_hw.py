"""
    This small script is written by Kadir Burak Mavzer for the
    2nd homework of Advanced Python (ICS0009) course in IT College of
    TalTech.

    It creates a database for the diners in TalTech including two tables:
    Canteens and Providers. Canteen and provider information has been
    taken from: https://www.ttu.ee/students/university-facilities/canteen/

    The information is inserted into two .csv files and they are converted
    into an SQL table using the pandas library. After the changes are committed
    to the database, two queries are constructed. First one is to check the
    canteens that are open between 16:15 and 18:00 and the second one is to
    check the canteens that are serviced by the provider Rahva Toit.

    NB! No tests have been written for this script.

    It can be run by navigating to the folder consisting the .py file and
    typing:

        python3 database_hw.py

    As all the files necessary are included in this folder, no change should
    be necessary.

    When run, it will return two lists each containing one query result.

    NB! You can also check both tables by uncommenting the lines 76 and 77.

"""

import sqlite3
import pandas as pd


def read_to_sql(csv_file, name, conn):
    read_file = pd.read_csv(csv_file)
    read_file.to_sql(name, conn, if_exists='replace', index=False)


def print_result(curs, query):
    curs.execute(query)
    print(curs.fetchall())


connection = sqlite3.connect("diners.db")
cursor = connection.cursor()

# Create empty tables
cursor.execute('''CREATE TABLE IF NOT EXISTS CANTEENS
             ([generated_id] INTEGER PRIMARY KEY, [name] text, [provider_id] integer, [location] text, [time_open] time, [time_closed] time)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS PROVIDERS
             ([provider_id] INTEGER,[provider_name] text)''')

read_to_sql(r"canteens.csv", 'CANTEENS', connection)
read_to_sql(r"providers.csv", 'PROVIDERS', connection)

# Adding bitStop kohvik manually to the table of providers
cursor.execute('''
    INSERT INTO PROVIDERS (provider_id, provider_name)
    VALUES (4, 'bitStop kohvik')
''')


# Adding bitStop kohvik manually to the table of canteens
cursor.execute('''
    INSERT INTO CANTEENS (name, provider_id, location, time_open, time_closed)
    VALUES ('bitStop Kohvik', 4, 'IT College of TalTech 1st Floor', '09:30:00 AM', '16:00:00 PM')
''')

# Committing changes to the database
connection.commit()

# # Print the tables in the database
# print_result(cursor, "SELECT * FROM CANTEENS")
# print_result(cursor, "SELECT * FROM PROVIDERS")


# First query to check canteens that are open between 16:15 - 18:00
query_one = """SELECT name FROM CANTEENS 
            WHERE time_closed BETWEEN '04:15:00 PM'
            AND '06:00:00 PM'"""

# Second query to check the canteens serviced by Rahva Toit
query_two = """SELECT name FROM CANTEENS
            WHERE provider_id = (SELECT provider_id FROM PROVIDERS
            WHERE provider_name = 'Rahva Toit')"""

# Check query results by printing them to the console
print_result(cursor, query_one)
print_result(cursor, query_two)

