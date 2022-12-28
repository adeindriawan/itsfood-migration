from models import db
from enum import Enum

class PaymentDetailStatus(Enum):
  Unpaid = 'Unpaid'
  Paid = 'Paid'
  Cancelled = 'Cancelled'

class PaymentDetail(db.Model):
  __tablename__ = 'payment_details'
  __table_args__ = {
    'mysql_engine': 'InnoDB'
  }
  id = db.Column(db.Integer(), primary_key=True)
  payment_id = db.Column(db.Integer(), db.ForeignKey('payments.id', ondelete='CASCADE'), nullable=False)
  order_id = db.Column(db.Integer(), db.ForeignKey('orders.id', ondelete='CASCADE'), nullable=False)
  status = db.Column(db.Enum(PaymentDetailStatus), nullable=False)
  created_at = db.Column(db.DateTime(), nullable=False)
  updated_at = db.Column(db.DateTime(), nullable=True)
  created_by = db.Column(db.String(30), nullable=False)

  def __init__(
    self, payment_id, order_id,
    status, created_at, updated_at, created_by
    ) -> None:
    super().__init__()
    self.payment_id = payment_id
    self.order_id = order_id
    self.status = status
    self.created_at = created_at
    self.updated_at = updated_at
    self.created_by = created_by

class DumpPaymentDetail(db.Model):
  __tablename__ = '__payment_details'
  __table_args__ = {
    'mysql_engine': 'InnoDB'
  }
  id = db.Column(db.Integer(), primary_key=True)
  source_id = db.Column(db.Integer(), db.ForeignKey('payment_details.id', ondelete='CASCADE'), nullable=False)
  payment_id = db.Column(db.Integer(), db.ForeignKey('payments.id', ondelete='CASCADE'), nullable=False)
  order_id = db.Column(db.Integer(), db.ForeignKey('orders.id', ondelete='CASCADE'), nullable=False)
  status = db.Column(db.Enum(PaymentDetailStatus), nullable=False)
  created_at = db.Column(db.DateTime(), nullable=False)
  updated_at = db.Column(db.DateTime(), nullable=True)
  created_by = db.Column(db.String(30), nullable=False)

  def __init__(
    self, source_id, payment_id, order_id, status,
    created_at, updated_at, created_by
    ) -> None:
    super().__init__()
    self.source_id = source_id
    self.payment_id = payment_id
    self.order_id = order_id
    self.status = status
    self.created_at = created_at
    self.updated_at = updated_at
    self.created_by = created_by


