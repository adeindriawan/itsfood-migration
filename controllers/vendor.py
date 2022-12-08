from models import db, Vendor, User
import csv
from datetime import datetime

def import_vendor_and_migrate():
  with open('data/suppliers.csv') as vendor_file:
    csv_reader = csv.reader(vendor_file, delimiter=',')
    for row in csv_reader:
      print(row)
      id = row[0]
      name = row[3]
      company_name = None if row[4] == '' or row[4] == 'NULL' else row[4]
      company_type = None if row[5] == '' or row[5] == 'NULL' else row[5]
      address = None if row[6] == '' or row[6] == 'NULL' else row[6]
      village = None
      district = None
      regency = None
      province = None
      postal_code = None
      phone = row[9]
      cellphone = row[10]
      email = row[13]
      password = row[15]
      npwp_number = None if row[16] == '' or row[16] == 'NULL' else row[16]
      npwp_name = None if row[17] == '' or row[17] == 'NULL' else row[17]
      npwp_address = None if row[18] == '' or row[18] == 'NULL' else row[18]
      officer_name = None if row[19] == '' or row[19] == 'NULL' else row[19]
      officer_position = None if row[20] == '' or row[20] == 'NULL' else row[20]
      officer_phone = None if row[21] == '' or row[21] == 'NULL' else row[21]
      officer_id_number = None if row[22] == '' or row[22] == 'NULL' else row[22]
      officer_address = None if row[23] == '' or row[23] == 'NULL' else row[23]
      pkp_number = None if row[24] == '' or row[24] == 'NULL' else row[24]
      pkp_expiry_date = None if row[25] == '' or row[25] == 'NULL' else row[25]
      bank_name = None if row[34] == '' or row[34] == 'NULL' else row[34]
      bank_branch = None if row[35] == '' or row[35] == 'NULL' else row[35]
      bank_account_number = None if row[37] == '' or row[37] == 'NULL' else row[37]
      bank_account_name = None if row[38] == '' or row[38] == 'NULL' else row[38]
      vendor_min_order_amount = row[39]
      vendor_min_order_qty = row[40]
      vendor_delivery_cost = row[41]
      vendor_service_charge = row[42]
      vendor_margin = row[43]
      vendor_note_for_menus = None if row[44] == '' or row[44] == 'NULL' else row[44]
      vendor_telegram_id = None if row[45] == '' or row[45] == 'NULL' else row[45]
      if row[46] == '1':
        status = 'Registered'
      elif row[46] == '2':
        status = 'Activated'
      else:
        status = 'Suspended'
      created_by = 'Migration System'
      created_at = datetime.now()
      updated_at = None

      user_entry = User(name, email, password, cellphone, 'Vendor', status, created_by, created_at, updated_at)
      db.session.add(user_entry)
      db.session.commit()
      new_user_id = user_entry.id

      vendor_entry =  Vendor(
        id, new_user_id, company_name,
        company_type, phone, address, village, district,
        regency, province, postal_code, npwp_number, npwp_name,
        npwp_address, officer_name, officer_phone, officer_position, officer_address, officer_id_number,
        pkp_number, pkp_expiry_date, bank_name, bank_branch, bank_account_number,
        bank_account_name, vendor_min_order_amount, vendor_min_order_qty,
        vendor_delivery_cost, vendor_service_charge, vendor_margin,
        vendor_note_for_menus, vendor_telegram_id, status, created_by, created_at, updated_at
      )
      db.session.add(vendor_entry)
      db.session.commit()
