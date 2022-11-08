from models import db
from enum import Enum

class CustomerType(Enum):
  ITS = 'ITS'
  Public = 'Public'

class CustomerStatus(Enum):
  Registered = 'Registered'
  Activated = 'Activated'
  Suspended = 'Suspended'

class Customer(db.Model):
  __tablename__ = 'customers'
  __table_args__ = {
    'mysql_engine': 'InnoDB'
  }
  id = db.Column(db.Integer(), primary_key=True)
  user_id = db.Column(db.Integer(), db.ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
  type = db.Column(db.Enum(CustomerType), default='Public', nullable=False)
  unit_id = db.Column(db.Integer(), db.ForeignKey('units.id', ondelete='CASCADE'), default=None, nullable=True)
  status = db.Column(db.Enum(CustomerStatus), nullable=False, default='Activated')
  created_by = db.Column(db.String(30), nullable=False)
  created_at = db.Column(db.DateTime(), nullable=False)
  updated_at = db.Column(db.DateTime(), nullable=True)

  def __init__(self, id, user_id, type, 
    unit_id, status, created_by,
    created_at, updated_at):
    self.id = id
    self.user_id = user_id
    self.type = type
    self.unit_id = unit_id
    self.status = status
    self.created_by = created_by
    self.created_at = created_at
    self.updated_at = updated_at

class DumpCustomer(db.Model):
  __tablename__ = '__customers'
  __table_args__ = {
    'mysql_engine': 'InnoDB'
  }
  id = db.Column(db.Integer(), primary_key=True)
  source_id = db.Column(db.Integer, db.ForeignKey('customers.id', ondelete='CASCADE'), nullable=False)
  user_id = db.Column(db.Integer(), db.ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
  type = db.Column(db.Enum(CustomerType), nullable=False)
  unit_id = db.Column(db.Integer(), db.ForeignKey('units.id', ondelete='CASCADE'), nullable=True)
  status = db.Column(db.Enum(CustomerStatus), nullable=False, default='Activated')
  remark = db.Column(db.String(50), nullable=False)
  created_at = db.Column(db.DateTime(), nullable=False)
  updated_at = db.Column(db.DateTime(), nullable=False)
  created_by = db.Column(db.String(30), nullable=False)

  def __init__(
    self, source_id, user_id, type,
    unit_id, status, remark, created_at,
    updated_at, created_by
  ) -> None:
    super().__init__()
    self.source_id = source_id
    self.user_id = user_id
    self.type = type
    self.unit_id = unit_id
    self.status = status
    self.remark = remark
    self.created_at = created_at
    self.updated_at = updated_at
    self.created_by = created_by
