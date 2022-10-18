from models import db
from enum import Enum

class UserType(Enum):
  Customer = 'Customer'
  Vendor = 'Vendor'
  Admin = 'Admin'

class UserStatus(Enum):
  Registered = 'Registered'
  Activated = 'Activated'
  Suspended = 'Suspended'

class User(db.Model):
  __tablename__ = 'users'
  __table_args__ = {
    'mysql_engine': 'InnoDB'
  }
  id = db.Column(db.Integer(), primary_key=True)
  name = db.Column(db.String(50), nullable=False)
  email = db.Column(db.String(50), nullable=False)
  password = db.Column(db.String(100), nullable=False)
  phone = db.Column(db.String(20), nullable=False)
  type = db.Column(db.Enum(UserType), nullable=False)
  status = db.Column(db.Enum(UserStatus), nullable=False, default='Activated')
  created_by = db.Column(db.String(20), nullable=False)
  created_at = db.Column(db.DateTime(), nullable=False)
  updated_at = db.Column(db.DateTime(), nullable=True)

  def __init__(self, name, email, password, phone, type, status, created_by, created_at, updated_at) -> None:
     super().__init__()
     self.name = name
     self.email = email
     self.password = password
     self.phone = phone
     self.type = type
     self.status = status
     self.created_by = created_by
     self.created_at = created_at
     self.updated_at = updated_at

class DumpUser(db.Model):
  __tablename__ = '__users'
  __table_args__ = {
    'mysql_engine': 'InnoDB'
  }
  id = db.Column(db.Integer(), primary_key=True)
  source_id = db.Column(db.Integer(), db.ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
  name = db.Column(db.String(50), nullable=False)
  email = db.Column(db.String(50), nullable=False)
  password = db.Column(db.String(100), nullable=False)
  phone = db.Column(db.String(20), nullable=False)
  type = db.Column(db.Enum(UserType), nullable=False)
  status = db.Column(db.Enum(UserStatus), nullable=False, default='Activated')
  remark = db.Column(db.String(50), nullable=False)
  created_at = db.Column(db.DateTime(), nullable=False)
  updated_at = db.Column(db.DateTime(), nullable=False)
  created_by = db.Column(db.String(30), nullable=False)

  def __init__(
    self, source_id, name, email, password, phone,
    type, status, remark, created_at, updated_at, created_by
    ) -> None:
    super().__init__()
    self.source_id = source_id
    self.name = name
    self.email = email
    self.password = password
    self.phone = phone
    self.type = type
    self.status = status
    self.remark = remark
    self.created_at = created_at
    self.updated_at = updated_at
    self.created_by = created_by

