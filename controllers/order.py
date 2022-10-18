from models import db, Order, DumpOrder
import csv
from datetime import datetime

def import_orders_and_migrate():
  with open('data/orders.csv') as order_file:
    csv_reader = csv.reader(order_file, delimiter=',')
    for row in csv_reader:
      id = row[0]
      ordered_by = row[1]
      created_at = row[2]
      ordered_for = row[4]
      ordered_to = row[3]
      num_of_menus = row[8]
      qty_of_menus = row[9]
      amount = row[10]
      discount = row[16]
      purpose = row[18]
      activity = row[20]
      source_of_fund = row[21]
      info = row[22]
      payment_option = row[31]
      if row[11] == '1':
        status = 'Created'
      elif row[11] == '2':
        status = 'Processed'
      elif row[11] == '3':
        status = 'Completed'
      elif row[11] == '4':
        status = 'Cancelled'
      elif row[11] == '5':
        status = 'Billed'
      elif row[11] == '6':
        status = 'Paid'
      else:
        status = 'Unknown'
      updated_at = None
      created_by = 'Migration System'
      
      processed_at = row[6]
      accepted_at = row[7]

      order_entry = Order(id, ordered_by, ordered_for, ordered_to, num_of_menus, qty_of_menus,
        amount, purpose, activity, source_of_fund, payment_option, info,
        status, created_at, updated_at, created_by)
      db.session.add(order_entry)
      db.session.commit()
      new_order_id = order_entry.id

      if processed_at != '' or processed_at != 'NULL':
        created_at = processed_at
        status = 'Processed'
        dump_order_entry = DumpOrder(new_order_id, ordered_by, ordered_for, ordered_to, num_of_menus, qty_of_menus,
        amount, purpose, activity, source_of_fund, payment_option, info,
        status, created_at, updated_at, created_by)
        db.session.add(dump_order_entry)
        db.session.commit()

      if accepted_at != '' or accepted_at != 'NULL':
        created_at = accepted_at
        status = 'Completed'
        dump_order_entry = DumpOrder(new_order_id, ordered_by, ordered_for, ordered_to, num_of_menus, qty_of_menus,
        amount, purpose, activity, source_of_fund, payment_option, info,
        status, created_at, updated_at, created_by)
        db.session.add(dump_order_entry)
        db.session.commit()
      print(row)