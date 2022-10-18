from models import db, User, Admin
from datetime import datetime
import csv

def import_admin_and_migrate():
  with open('data/admins.csv') as admin_file:
    csv_reader = csv.reader(admin_file, delimiter=',')
    for row in csv_reader:
      name = row[1]
      email = row[2]
      password = row[4]
      phone = row[5]
      created_at = datetime.now()
      updated_at = None
      created_by = 'Migration System'

      user_entry = User(name, email, password, phone, 'Admin', 'Activated', created_by, created_at, updated_at)
      db.session.add(user_entry)
      db.session.commit()
      new_user_id = user_entry.id

      admin_entry = Admin(new_user_id, name, email, phone, 'Active', created_at, updated_at, created_by)
      db.session.add(admin_entry)
      db.session.commit()
      print(row)