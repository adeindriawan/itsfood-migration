from models import db
from enum import Enum

class DiscountStatus(Enum):
  Active = 'Active'
  Cancelled = 'Cancelled'

class Issuer(Enum):
  Vendor = 'Vendor'
  Utama = 'Utama'
  Other = 'Other'

class Discount(db.Model):
  __tablename__ = 'discounts'
  __table_args__ = {
    'mysql_engine': 'InnoDB'
  }
  id = db.Column(db.Integer(), primary_key=True)
  order_detail_id = db.Column(db.Integer(), db.ForeignKey('order_details.id', ondelete='CASCADE'), nullable=False)
  amount = db.Column(db.Integer(), nullable=False)
  reason = db.Column(db.String(50), nullable=False)
  issuer = db.Column(db.Enum(Issuer), nullable=False)
  status = db.Column(db.Enum(DiscountStatus), nullable=True)
  created_at = db.Column(db.DateTime(), nullable=False)
  updated_at = db.Column(db.DateTime(), nullable=True)
  created_by = db.Column(db.String(30), nullable=False)

  def __init__(
    self, order_detail_id, amount, reason, issuer, status, created_at, updated_at, created_by
    ) -> None:
    super().__init__()
    self.order_detail_id = order_detail_id
    self.amount = amount
    self.reason = reason
    self.issuer = issuer
    self.status = status
    self.created_at = created_at
    self.updated_at = updated_at
    self.created_by = created_by

class DumpDiscount(db.Model):
  __tablename__ = '__discounts'
  __table_args__ = {
    'mysql_engine': 'InnoDB'
  }
  id = db.Column(db.Integer(), primary_key=True)
  source_id = db.Column(db.Integer(), db.ForeignKey('discounts.id', ondelete='CASCADE'), nullable=False)
  order_detail_id = db.Column(db.Integer(), db.ForeignKey('order_details.id', ondelete='CASCADE'), nullable=False)
  amount = db.Column(db.Integer(), nullable=False)
  reason = db.Column(db.String(50), nullable=False)
  issuer = db.Column(db.Enum(Issuer), nullable=False)
  status = db.Column(db.Enum(DiscountStatus), nullable=False)
  created_at = db.Column(db.DateTime(), nullable=False)
  updated_at = db.Column(db.DateTime(), nullable=True)
  created_by = db.Column(db.String(30), nullable=False)

  def __init__(
    self, source_id, order_detail_id, amount, reason,
    issuer, status, created_at, updated_at, created_by
    ) -> None:
    super().__init__()
    self.source_id = source_id 
    self.order_detail_id = order_detail_id
    self.amount = amount
    self.reason = reason
    self.issuer = issuer
    self.status = status
    self.created_at = created_at
    self.updated_at = updated_at
    self.created_by = created_by