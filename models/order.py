from models import db
from enum import Enum

class OrderActivity(Enum):
  Rutin = 'Rutin'
  Pengembangan = 'Pengembangan'

class OrderSourceOfFund(Enum):
  NonPNBP = 'Non-PNBP'
  BPPTNBH = 'BPPTNBH'
  APBNK = 'APBNK'
  Pribadi = 'Pribadi'

class OrderPaymentOption(Enum):
  Cash = 'Cash'
  Transfer = 'Transfer'
  VA = 'VA'

class OrderStatus(Enum):
  Created = 'Created'
  Forwarded = 'Forwarded'
  Processed = 'Processed'
  Completed = 'Completed'
  Billed = 'Billed'
  Paid = 'Paid'
  Cancelled = 'Cancelled'

class Order(db.Model):
  __tablename__ = 'orders'
  __table_args__ = {
    'mysql_engine': 'InnoDB'
  }
  id = db.Column(db.Integer(), primary_key=True)
  ordered_by = db.Column(db.Integer(), db.ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
  ordered_for = db.Column(db.DateTime(), nullable=False)
  ordered_to = db.Column(db.String(30), nullable=False)
  num_of_menus = db.Column(db.Integer(), nullable=False)
  qty_of_menus = db.Column(db.Integer(), nullable=False)
  amount = db.Column(db.Integer(), nullable=False)
  purpose = db.Column(db.String(50), nullable=False)
  activity = db.Column(db.Enum(OrderActivity), nullable=False)
  source_of_fund = db.Column(db.Enum(OrderSourceOfFund), nullable=False)
  payment_option = db.Column(db.Enum(OrderPaymentOption), nullable=False)
  info = db.Column(db.String(100), nullable=True)
  status = db.Column(db.Enum(OrderStatus), nullable=False)
  created_at = db.Column(db.DateTime(), nullable=False)
  updated_at = db.Column(db.DateTime(), nullable=True)
  created_by = db.Column(db.String(30), nullable=False)

  def __init__(
    self, id, ordered_by, ordered_for, ordered_to, num_of_menus, qty_of_menus,
    amount, purpose, activity, source_of_fund, payment_option, info,
    status, created_at, updated_at, created_by
    ) -> None:
    super().__init__()
    self.id = id
    self.ordered_by = ordered_by
    self.ordered_for = ordered_for
    self.ordered_to = ordered_to
    self.num_of_menus = num_of_menus
    self.qty_of_menus = qty_of_menus
    self.amount = amount
    self.purpose = purpose
    self.activity = activity
    self.source_of_fund = source_of_fund
    self.payment_option = payment_option
    self.info = info
    self.status = status
    self.created_at = created_at
    self.updated_at = updated_at
    self.created_by = created_by

class DumpOrder(db.Model):
  __tablename__ = '__orders'
  __table_args__ = {
    'mysql_engine': 'InnoDB'
  }
  id = db.Column(db.Integer(), primary_key=True)
  source_id = db.Column(db.Integer(), db.ForeignKey('orders.id', ondelete='CASCADE'), nullable=False)
  ordered_by = db.Column(db.Integer(), db.ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
  ordered_for = db.Column(db.DateTime(), nullable=False)
  ordered_to = db.Column(db.String(30), nullable=False)
  num_of_menus = db.Column(db.Integer(), nullable=False)
  qty_of_menus = db.Column(db.Integer(), nullable=False)
  amount = db.Column(db.Integer(), nullable=False)
  purpose = db.Column(db.String(50), nullable=False)
  activity = db.Column(db.Enum(OrderActivity), nullable=False)
  source_of_fund = db.Column(db.Enum(OrderSourceOfFund), nullable=False)
  payment_option = db.Column(db.Enum(OrderPaymentOption), nullable=False)
  info = db.Column(db.String(100), nullable=True)
  status = db.Column(db.Enum(OrderStatus), nullable=False)
  created_at = db.Column(db.DateTime(), nullable=False)
  updated_at = db.Column(db.DateTime(), nullable=True)
  created_by = db.Column(db.DateTime(), nullable=False)

  def __init__(
    self, source_id, ordered_by, ordered_for, ordered_to, num_of_menus, qty_of_menus,
    amount, purpose, activity, source_of_fund, payment_option, info,
    status, created_at, updated_at, created_by
    ) -> None:
    super().__init__()
    self.source_id = source_id
    self.ordered_by = ordered_by
    self.ordered_for = ordered_for
    self.ordered_to = ordered_to
    self.num_of_menus = num_of_menus
    self.qty_of_menus = qty_of_menus
    self.amount = amount
    self.purpose = purpose
    self.activity = activity
    self.source_of_fund = source_of_fund
    self.payment_option = payment_option
    self.info = info
    self.status = status
    self.created_at = created_at
    self.updated_at = updated_at
    self.created_by = created_by
