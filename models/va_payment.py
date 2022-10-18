from models import db
from enum import Enum

class VAPaymentStatus(Enum):
  Unpaid = 'Unpaid'
  Paid = 'Paid'
  Cancelled = 'Cancelled'

class VAPayment(db.Model):
  __tablename__ = 'va_payments'
  __table_args__ = {
    'mysql_engine': 'InnoDB'
  }
  id = db.Column(db.Integer(), primary_key=True)
  transaction_id = db.Column(db.String(30), nullable=False)
  user_id = db.Column(db.Integer(), db.ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
  virtual_account = db.Column(db.String(30), nullable=False)
  amount = db.Column(db.Integer(), nullable=False)
  status = db.Column(db.Enum(VAPaymentStatus), nullable=False)
  created_at = db.Column(db.DateTime(), nullable=False)
  updated_at = db.Column(db.DateTime(), nullable=True)
  created_by = db.Column(db.String(30), nullable=False)

  def __init__(
    self, transaction_id, user_id, virtual_account, amount, 
    status, created_at, updated_at, created_by) -> None:
    super().__init__()
    self.transaction_id = transaction_id
    self.user_id = user_id
    self.virtual_account = virtual_account
    self.amount = amount 
    self.status = status 
    self.created_at = created_at 
    self.updated_at = updated_at
    self.created_by = created_by

class DumpVAPayment(db.Model):
  __tablename__ = '__va_payments'
  __table_args__ = {
    'mysql_engine': 'InnoDB'
  }
  id = db.Column(db.Integer(), primary_key=True)
  source_id = db.Column(db.Integer(), db.ForeignKey('va_payments.id', ondelete='CASCADE'), nullable=False)
  transaction_id = db.Column(db.String(30), nullable=False)
  user_id = db.Column(db.Integer(), db.ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
  virtual_account = db.Column(db.String(30), nullable=False)
  amount = db.Column(db.Integer(), nullable=False)
  status = db.Column(db.Enum(VAPaymentStatus), nullable=False)
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