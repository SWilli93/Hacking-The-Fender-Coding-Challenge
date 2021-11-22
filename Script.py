import csv

compromised_users = []

# Retrieving the inital file of passwords and username of compromised
with open('passwords.csv') as password_file:
  password_csv = csv.DictReader(password_file)
  for password_row in password_csv:
    compromised_users.append(password_row['Username'])