from models import db
from enum import Enum

class AddressStatus(Enum):
  Active = 'Active'
  Inactive = 'Inactive'

class Address(db.Model):
  __tablename__ = 'addresses'
  __table_args__ = {
    'mysql_engine': 'InnoDB'
  }
  id = db.Column(db.Integer(), primary_key=True)
  address = db.Column(db.String(100), nullable=False)
  user_id = db.Column(db.Integer(), db.ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
  order_id = db.Column(db.Integer(), db.ForeignKey('orders.id', ondelete='CASCADE'), nullable=False)
  status = db.Column(db.Enum(AddressStatus), nullable=False, default='Active')
  created_at = db.Column(db.DateTime(), nullable=False)
  updated_at = db.Column(db.DateTime(), nullable=True)
  created_by = db.Column(db.String(30), nullable=False)

  def __init__(
    self, address, user_id, order_id, status, created_at, updated_at, created_by
    ) -> None:
    super().__init__()
    self.address = address
    self.user_id = user_id
    self.order_id = order_id
    self.status = status
    self.created_at = created_at
    self.updated_at = updated_at
    self.created_by = created_by

class DumpAddress(db.Model):
  __tablename__ = '__addresses'
  __table_args__ = {
    'mysql_engine': 'InnoDB'
  }
  id = db.Column(db.Integer(), primary_key=True)
  source_id = db.Column(db.Integer(), db.ForeignKey('addresses.id', ondelete='CASCADE'), nullable=False)
  address = db.Column(db.String(100), nullable=False)
  user_id = db.Column(db.Integer(), db.ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
  order_id = db.Column(db.Integer(), db.ForeignKey('orders.id', ondelete='CASCADE'), nullable=False)
  status = db.Column(db.Enum(AddressStatus), nullable=False, default='Inactive')
  created_at = db.Column(db.DateTime(), nullable=False)
  updated_at = db.Column(db.DateTime(), nullable=True)
  created_by = db.Column(db.String(30), nullable=False)

  def __init__(
    self, source_id, address, user_id, order_id, status, created_at, updated_at, created_by
    ) -> None:
    super().__init__()
    self.source_id = source_id
    self.address = address
    self.user_id = user_id
    self.order_id = order_id
    self.status = status
    self.created_at = created_at
    self.updated_at = updated_at
    self.created_by = created_by

