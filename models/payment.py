from models import db
from enum import Enum

class PaymentStatus(Enum):
  Unpaid = 'Unpaid'
  NeedsConfirmation = 'Needs confirmation'
  Paid = 'Paid'
  Cancelled = 'Cancelled'

class Payment(db.Model):
  __tablename__ = 'payments'
  __table_args__ = {
    'mysql_engine': 'InnoDB'
  }
  id = db.Column(db.Integer(), primary_key=True)
  transaction_id = db.Column(db.String(30), nullable=False)
  customer_id = db.Column(db.Integer(), db.ForeignKey('customers.id', ondelete='CASCADE'), nullable=False)
  method = db.Column(db.String(20), nullable=False)
  virtual_account = db.Column(db.String(30), nullable=True)
  amount = db.Column(db.Integer(), nullable=False)
  file = db.Column(db.String(100), nullable=True)
  status = db.Column(db.Enum(PaymentStatus), nullable=False)
  created_at = db.Column(db.DateTime(), nullable=False)
  updated_at = db.Column(db.DateTime(), nullable=True)
  created_by = db.Column(db.String(30), nullable=False)

  def __init__(
    self, transaction_id, customer_id, virtual_account, amount, file,
    status, created_at, updated_at, created_by) -> None:
    super().__init__()
    self.transaction_id = transaction_id
    self.customer_id = customer_id
    self.virtual_account = virtual_account
    self.amount = amount 
    self.file = file
    self.status = status 
    self.created_at = created_at 
    self.updated_at = updated_at
    self.created_by = created_by

class DumpPayment(db.Model):
  __tablename__ = '__payments'
  __table_args__ = {
    'mysql_engine': 'InnoDB'
  }
  id = db.Column(db.Integer(), primary_key=True)
  source_id = db.Column(db.Integer(), db.ForeignKey('payments.id', ondelete='CASCADE'), nullable=False)
  transaction_id = db.Column(db.String(30), nullable=False)
  customer_id = db.Column(db.Integer(), db.ForeignKey('customers.id', ondelete='CASCADE'), nullable=False)
  method = db.Column(db.String(20), nullable=False)
  virtual_account = db.Column(db.String(30), nullable=True)
  amount = db.Column(db.Integer(), nullable=False)
  file = db.Column(db.String(100), nullable=True)
  status = db.Column(db.Enum(PaymentStatus), nullable=False)
  created_at = db.Column(db.DateTime(), nullable=False)
  updated_at = db.Column(db.DateTime(), nullable=True)
  created_by = db.Column(db.String(30), nullable=False)

  def __init__(
    self, source_id, transaction_id, user_id, virtual_account, amount,
    status, created_at, updated_at, created_by
    ) -> None:
    super().__init__()
    self.source_id = source_id
    self.transaction_id = transaction_id
    self.user_id = user_id
    self.virtual_account = virtual_account
    self.amount = amount
    self.status = status
    self.created_at = created_at
    self.updated_at = updated_at
    self.created_by = created_by