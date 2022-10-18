from models import db
from enum import Enum

class OrderDetailStatus(Enum):
  Ordered = 'Ordered'
  Processed = 'Processed'
  Delivered = 'Delivered'
  Accepted = 'Accepted'
  Billed = 'Billed'
  Paid = 'Paid'
  Cancelled = 'Cancelled'

class OrderDetail(db.Model):
  __tablename__ = 'order_details'
  __table_args__ = {
    'mysql_engine': 'InnoDB'
  }
  id = db.Column(db.Integer(), primary_key=True)
  order_id = db.Column(db.Integer(), db.ForeignKey('orders.id', ondelete='CASCADE'), nullable=False)
  menu_id = db.Column(db.Integer(), db.ForeignKey('menus.id', ondelete='CASCADE'), nullable=False)
  qty = db.Column(db.Integer(), nullable=False)
  price = db.Column(db.Integer(), nullable=False)
  cogs = db.Column(db.Integer(), nullable=False)
  status = db.Column(db.Enum(OrderDetailStatus), nullable=False)
  created_at = db.Column(db.DateTime(), nullable=False)
  updated_at = db.Column(db.DateTime(), nullable=True)
  created_by = db.Column(db.String(30), nullable=False)

  def __init__(
    self, id, order_id, menu_id, qty, price, cogs, 
    status, created_at, updated_at, created_by
    ) -> None:
    super().__init__()
    self.id = id
    self.order_id = order_id
    self.menu_id = menu_id
    self.qty = qty
    self.price = price
    self.cogs = cogs
    self.status = status
    self.created_at = created_at
    self.updated_at = updated_at
    self.created_by = created_by

class DumpOrderDetail(db.Model):
  __tablename__ = '__order_details'
  __table_args__ = {
    'mysql_engine': 'InnoDB'
  }
  id = db.Column(db.Integer(), primary_key=True)
  source_id = db.Column(db.Integer(), db.ForeignKey('order_details.id', ondelete='CASCADE'), nullable=False)
  order_id = db.Column(db.Integer(), db.ForeignKey('orders.id', ondelete='CASCADE'), nullable=False)
  menu_id = db.Column(db.Integer(), db.ForeignKey('menus.id', ondelete='CASCADE'), nullable=False)
  qty = db.Column(db.Integer(), nullable=False)
  price = db.Column(db.Integer(), nullable=False)
  cogs = db.Column(db.Integer(), nullable=False)
  status = db.Column(db.Enum(OrderDetailStatus), nullable=False)
  created_at = db.Column(db.DateTime(), nullable=False)
  updated_at = db.Column(db.DateTime(), nullable=True)
  created_by = db.Column(db.String(30), nullable=False)

  def __init__(
    self, source_id, order_id, menu_id, qty, price, cogs,
    status, created_at, updated_at, created_by
    ) -> None:
    super().__init__()
    self.source_id = source_id
    self.order_id = order_id
    self.menu_id = menu_id
    self.qty = qty
    self.price = price
    self.cogs = cogs
    self.status = status
    self.created_at = created_at
    self.updated_at = updated_at
    self.created_by = created_by
