import csv
import json

compromised_users = []

# Retrieving the inital file of passwords and username of compromised
with open('passwords.csv') as password_file:
  password_csv = csv.DictReader(password_file)
  for password_row in password_csv:
    compromised_users.append(password_row['Username'])

# Writing list of compromised users as a new file
with open('compromised_users.txt', 'w') as compromised_user_file:
  for compromised_user in compromised_users:
     compromised_user_file.write(compromised_user)

# Messaging boss that we have the lsit of users and the mission was succesful
with open('boss_message.json', 'w') as boss_message:
  boss_message_dict = {
    'recipient': 'The Boss',
    'message': 'Mission Success'
    }
  json.dump(boss_message_dict, boss_message)