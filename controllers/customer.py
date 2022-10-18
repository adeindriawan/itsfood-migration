from models import db, User, Customer
import csv
from datetime import datetime

def import_customer_and_migrate():
  with open('data/users.csv') as user_file:
    csv_reader = csv.reader(user_file, delimiter=',')
    for row in csv_reader:
      original_user_id = row[0]
      user_name = row[1]
      user_email = row[2]
      user_password = row[4]
      user_phone = row[5]
      user_unit_id = 1
      user_type = 'Customer'
      user_status = 'Activated' if row[9] == '1' else 'Suspended'
      created_by = 'Migration System'
      created_at = datetime.now()
      updated_at = None
      print(row)
      
      user_entry = User(
        user_name, user_email, user_password, user_phone, 
        user_type, user_status, created_by, created_at, updated_at)
      db.session.add(user_entry)
      db.session.commit()
      new_user_id = user_entry.id

      customer_entry = Customer(original_user_id, new_user_id, 'ITS', user_unit_id, user_status, created_by, created_at, updated_at)
      db.session.add(customer_entry)
      db.session.commit()