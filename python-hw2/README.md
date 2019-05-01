#####  This small script is written by Kadir Burak Mavzer for the 2nd homework of Advanced Python (ICS0009) course in IT College of TalTech.

It creates a database for the diners in TalTech including two tables: Canteens and Providers. Canteen and provider information has been taken from: https://www.ttu.ee/students/university-facilities/canteen/

The information is inserted into two .csv files and they are converted into an SQL table using the pandas library. After the changes are committed to the database, two queries are constructed. First one is to check the canteens that are open between 16:15 and 18:00 and the second one is to check the canteens that are serviced by the provider Rahva Toit.

NB! No tests have been written for this script.

It can be run by navigating to the folder consisting the .py file and typing:


    python3 database_hw.py

As all the files necessary are included in this folder, no change should be necessary.

When run, it will return two lists each containing one query result.

NB! You can also check both tables by uncommenting the lines 76 and 77.