from models import db, Menu, DumpMenu
import csv
from datetime import datetime

def import_menu_and_migrate():
  with open('data/products.csv', encoding='utf-8') as new_menu_file:
    csv_reader = csv.reader(new_menu_file, delimiter=',')
    for row in csv_reader:
      # print(row)
      id = row[1]
      name = row[3]
      description = row[4]
      type = row[5]
      image = row[6]
      cogs = row[7]
      retail_price = row[8]
      wholesale_price = row[9] if row[9] != 'NULL' else retail_price
      min_order_qty = row[10]
      max_order_qty = row[11]
      pre_order_days = row[12]
      pre_order_hours = row[13]
      discount = row[14]
      vendor_id = row[15]
      if row[16] == '1':
        status = 'Activated'
      elif row[16] == '2':
        status = 'Locked'
      elif row[16] == '3':
        status = 'Suspended'
      else:
        status = 'Registered'
      created_at = datetime.now()
      updated_at = None
      created_by = 'Migration System'

      menu_entry = Menu(id, name, description, type, cogs, retail_price, wholesale_price,
      min_order_qty, max_order_qty, pre_order_days,
      pre_order_hours, discount, image, vendor_id, status, created_by, created_at,
      updated_at)

      db.session.add(menu_entry)
      db.session.commit()

  with open('data/__products.csv', encoding='utf-8') as menu_file:
    csv_reader = csv.reader(menu_file, delimiter=',')
    for row in csv_reader:
      source_id = row[1]
      name = row[3]
      description = row[4]
      type = row[5]
      image = row[6]
      cogs = row[7]
      retail_price = row[8]
      wholesale_price = row[9] if row[9] != 'NULL' else retail_price
      min_order_qty = row[10]
      max_order_qty = row[11]
      pre_order_days = row[12]
      pre_order_hours = row[13]
      discount = row[14]
      vendor_id = row[15]
      if row[16] == '1':
        status = 'Activated'
      elif row[16] == '2':
        status = 'Locked'
      elif row[16] == '3':
        status = 'Suspended'
      else:
        status = 'Registered'
      created_at = datetime.now()
      updated_at = None
      created_by = 'Migration System'

      menu_entry = DumpMenu(source_id, name, description, type, cogs, retail_price, wholesale_price,
      min_order_qty, max_order_qty, pre_order_days,
      pre_order_hours, discount, image, vendor_id, status, created_at, updated_at,
      created_by)

      db.session.add(menu_entry)
      db.session.commit()
