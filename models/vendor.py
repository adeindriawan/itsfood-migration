from models import db
from enum import Enum

class VendorStatus(Enum):
  Registered = 'Registered'
  Activated = 'Activated'
  Suspended = 'Suspended'

class Vendor(db.Model):
  __tablename__ = 'vendors'
  __table_args__ = {
    'mysql_engine': 'InnoDB'
  }
  id = db.Column(db.Integer(), primary_key=True)
  user_id = db.Column(db.Integer(), db.ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
  company_name = db.Column(db.String(50), nullable=False)
  company_type = db.Column(db.String(20), nullable=False)
  phone = db.Column(db.String(15), nullable=True)
  address = db.Column(db.String(100), nullable=False)
  village = db.Column(db.String(20), nullable=True)
  district = db.Column(db.String(20), nullable=True)
  regency = db.Column(db.String(10), nullable=True)
  province = db.Column(db.String(10), nullable=True)
  postal_code = db.Column(db.String(8), nullable=True)
  npwp_number = db.Column(db.String(25), nullable=True)
  npwp_name = db.Column(db.String(50), nullable=True)
  npwp_address = db.Column(db.String(50), nullable=True)
  officer_name = db.Column(db.String(50), nullable=True)
  officer_phone = db.Column(db.String(20), nullable=True)
  officer_position = db.Column(db.String(20), nullable=True)
  officer_address = db.Column(db.String(100), nullable=True)
  officer_id_number = db.Column(db.String(20), nullable=True)
  pkp_number = db.Column(db.String(20), nullable=True)
  pkp_expiry_date = db.Column(db.DateTime(), nullable=True)
  bank_name = db.Column(db.String(20), nullable=False)
  bank_branch = db.Column(db.String(20), nullable=False)
  bank_account_number = db.Column(db.String(20), nullable=False)
  bank_account_name = db.Column(db.String(20), nullable=False)
  vendor_min_order_amount = db.Column(db.Integer(), nullable=False, default=0)
  vendor_min_order_qty = db.Column(db.Integer(), nullable=False, default=1)
  vendor_delivery_cost = db.Column(db.Integer(), nullable=False, default=0)
  vendor_service_charge = db.Column(db.Integer(), nullable=False, default=0)
  vendor_margin = db.Column(db.Float(), nullable=False, default=10)
  vendor_note_for_menus = db.Column(db.String(100), nullable=True)
  vendor_telegram_id = db.Column(db.String(10), nullable=True)
  status = db.Column(db.Enum(VendorStatus), nullable=False, default='Activated')
  created_by = db.Column(db.String(30), nullable=False)
  created_at = db.Column(db.DateTime(), nullable=False)
  updated_at = db.Column(db.DateTime(), nullable=True)

  def __init__(
    self, id, user_id, company_name,
    company_type, phone, address, village, district,
    regency, province, postal_code, npwp_number, npwp_name,
    npwp_address, officer_name, officer_phone, officer_position, officer_address, officer_id_number,
    pkp_number, pkp_expiry_date, bank_name, bank_branch, bank_account_number,
    bank_account_name, vendor_min_order_amount, vendor_min_order_qty,
    vendor_delivery_cost, vendor_service_charge, vendor_margin,
    vendor_note_for_menus, vendor_telegram_id, status, created_by, created_at, updated_at
  ) -> None:
    super().__init__()
    self.id = id
    self.user_id = user_id
    self.company_name = company_name
    self.company_type = company_type
    self.phone = phone
    self.address = address
    self.village = village
    self.district = district
    self.regency = regency
    self.province = province
    self.postal_code = postal_code
    self.npwp_number = npwp_number
    self.npwp_name = npwp_name
    self.npwp_address = npwp_address
    self.officer_name = officer_name
    self.officer_phone = officer_phone
    self.officer_position = officer_position
    self.officer_address = officer_address
    self.officer_id_number = officer_id_number
    self.pkp_number = pkp_number
    self.pkp_expiry_date = pkp_expiry_date
    self.bank_name = bank_name
    self.bank_branch = bank_branch
    self.bank_account_number = bank_account_number
    self.bank_account_name = bank_account_name
    self.vendor_min_order_amount = vendor_min_order_amount
    self.vendor_min_order_qty = vendor_min_order_qty
    self.vendor_delivery_cost = vendor_delivery_cost
    self.vendor_service_charge = vendor_service_charge
    self.vendor_margin = vendor_margin
    self.vendor_note_for_menus = vendor_note_for_menus
    self.vendor_telegram_id = vendor_telegram_id
    self.status = status
    self.created_by = created_by
    self.created_at = created_at
    self.updated_at = updated_at

class DumpVendor(db.Model):
  __tablename__ = '__vendors'
  __table_args__ = {
    'mysql_engine': 'InnoDB'
  }
  id = db.Column(db.Integer(), primary_key=True)
  source_id = db.Column(db.Integer(), db.ForeignKey('vendors.id', ondelete='CASCADE'), nullable=False)
  user_id = db.Column(db.Integer(), db.ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
  company_name = db.Column(db.String(50), nullable=False)
  company_type = db.Column(db.String(20), nullable=False)
  phone = db.Column(db.String(15), nullable=True)
  address = db.Column(db.String(100), nullable=False)
  village = db.Column(db.String(20), nullable=True)
  district = db.Column(db.String(20), nullable=True)
  regency = db.Column(db.String(10), nullable=True)
  province = db.Column(db.String(10), nullable=True)
  postal_code = db.Column(db.String(8), nullable=True)
  npwp_number = db.Column(db.String(25), nullable=True)
  npwp_name = db.Column(db.String(50), nullable=True)
  npwp_address = db.Column(db.String(50), nullable=True)
  officer_name = db.Column(db.String(50), nullable=True)
  officer_phone = db.Column(db.String(20), nullable=True)
  officer_position = db.Column(db.String(20), nullable=True)
  officer_address = db.Column(db.String(100), nullable=True)
  officer_id_number = db.Column(db.String(20), nullable=True)
  pkp_number = db.Column(db.String(20), nullable=True)
  pkp_expiry_date = db.Column(db.DateTime(), nullable=True)
  bank_name = db.Column(db.String(20), nullable=False)
  bank_branch = db.Column(db.String(20), nullable=False)
  bank_account_number = db.Column(db.String(20), nullable=False)
  bank_account_name = db.Column(db.String(20), nullable=False)
  vendor_min_order_amount = db.Column(db.Integer(), nullable=False, default=0)
  vendor_min_order_qty = db.Column(db.Integer(), nullable=False, default=1)
  vendor_delivery_cost = db.Column(db.Integer(), nullable=False, default=0)
  vendor_service_charge = db.Column(db.Integer(), nullable=False, default=0)
  vendor_margin = db.Column(db.Float(), nullable=False, default=10)
  vendor_note_for_menus = db.Column(db.String(100), nullable=True)
  vendor_telegram_id = db.Column(db.String(10), nullable=True)
  status = db.Column(db.Enum(VendorStatus), nullable=False, default='Activated')
  remark = db.Column(db.String(50), nullable=False)
  created_at = db.Column(db.DateTime(), nullable=False)
  created_by = db.Column(db.String(30), nullable=False)

  def __init__(
    self, source_id, user_id, company_name,
    company_type, phone, address, village, district,
    regency, province, postal_code, npwp_number, npwp_name,
    npwp_address, officer_name, officer_phone, officer_position, officer_address, officer_id_number,
    pkp_number, pkp_expiry_date, bank_name, bank_branch, bank_account_number,
    bank_account_name, vendor_min_order_amount, vendor_min_order_qty,
    vendor_delivery_cost, vendor_service_charge, vendor_margin,
    vendor_note_for_menus, vendor_telegram_id, status, remark, created_at, created_by
  ) -> None:
    super().__init__()
    self.source_id = source_id
    self.user_id = user_id
    self.company_name = company_name
    self.company_type = company_type
    self.phone = phone
    self.address = address
    self.village = village
    self.district = district
    self.regency = regency
    self.province = province
    self.postal_code = postal_code
    self.npwp_number = npwp_number
    self.npwp_name = npwp_name
    self.npwp_address = npwp_address
    self.officer_name = officer_name
    self.officer_phone = officer_phone
    self.officer_position = officer_position
    self.officer_address = officer_address
    self.officer_id_number = officer_id_number
    self.pkp_number = pkp_number
    self.pkp_expiry_date = pkp_expiry_date
    self.bank_name = bank_name
    self.bank_branch = bank_branch
    self.bank_account_number = bank_account_number
    self.bank_account_name = bank_account_name
    self.vendor_min_order_amount = vendor_min_order_amount
    self.vendor_min_order_qty = vendor_min_order_qty
    self.vendor_delivery_cost = vendor_delivery_cost
    self.vendor_service_charge = vendor_service_charge
    self.vendor_margin = vendor_margin
    self.vendor_note_for_menus = vendor_note_for_menus
    self.vendor_telegram_id = vendor_telegram_id
    self.status = status
    self.remark = remark
    self.created_at = created_at
    self.created_by = created_by
