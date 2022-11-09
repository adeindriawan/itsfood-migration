from models import db, OrderDetail, Cost, Discount, vendor
import csv

def import_order_details_and_migrate():
  with open('data/order_details.csv') as order_details_file:
    csv_reader = csv.reader(order_details_file, delimiter=',')
    for row in csv_reader:
      order_detail_id = row[0]
      order_id = row[3]
      menu_id = row[20]
      qty = row[5]
      price = row[6]
      cogs = row[7]
      if row[14] == '1':
        status = 'Ordered'
      elif row[14] == '2':
        status = 'Accepted'
      elif row[14] == '3':
        status = 'Cancelled'
      elif row[14] == '4':
        status = 'Processed'
      elif row[14] == '5':
        status = 'Billed'
      elif row[14] == '6':
        status = 'Paid'
      else:
        status = 'Unknown'
      created_at = row[19]
      updated_at = None
      created_by = 'Migration System'
      cost = row[8]
      cost_reason = row[9]
      service_charge = row[10]
      discount = row[11]
      vendor_discount = row[12]
      note = None

      order_detail_entry = OrderDetail(order_detail_id, order_id, menu_id, qty, price, cogs, note, status, created_at, updated_at, created_by)
      db.session.add(order_detail_entry)
      db.session.commit()

      if status == 'Paid':
        cost_status = 'Paid'
      elif status == 'Cancelled':
        cost_status = 'Cancelled'
      else:
        cost_status = 'Unpaid'

      if cost != '0':
        cost_entry = Cost(order_detail_id, cost, cost_reason, cost_status, created_at, updated_at, created_by)
        db.session.add(cost_entry)
        db.session.commit()

      if service_charge != '0':
        cost_entry = Cost(order_detail_id, service_charge, 'Service charge', cost_status, created_at, updated_at, created_by)
        db.session.add(cost_entry)
        db.session.commit()

      if discount != '0':
        discount_entry = Discount(order_detail_id, discount, 'ITS Food discount', cost_status, created_at, updated_at, created_by)
        db.session.add(discount_entry)
        db.session.commit()

      if vendor_discount != '0':
        discount_entry = Discount(order_detail_id, vendor_discount, 'Vendor discount', cost_status, created_at, updated_at, created_by)
        db.session.add(discount_entry)
        db.session.commit()
      print(row)