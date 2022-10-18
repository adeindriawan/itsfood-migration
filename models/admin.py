from models import db
from enum import Enum

class AdminStatus(Enum):
  Active = 'Active'
  Inactive = 'Inactive'

class Admin(db.Model):
  __tablename__ = 'admins'
  __table_args__ = {
    'mysql_engine': 'InnoDB'
  }
  id = db.Column(db.Integer(), primary_key=True)
  user_id = db.Column(db.Integer(), db.ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
  name = db.Column(db.String(50), nullable=False)
  email = db.Column(db.String(25), nullable=False)
  phone = db.Column(db.String(25), nullable=False)
  status = db.Column(db.Enum(AdminStatus), nullable=False)
  created_at = db.Column(db.DateTime(), nullable=False)
  updated_at = db.Column(db.DateTime(), nullable=True)
  created_by = db.Column(db.String(30), nullable=False)

  def __init__(
    self, user_id, name, email, phone, status,
    created_at, updated_at, created_by
    ) -> None:
    super().__init__()
    self.user_id = user_id
    self.name = name
    self.email = email
    self.phone = phone
    self.status = status
    self.created_at = created_at
    self.updated_at = updated_at
    self.created_by = created_by

class DumpAdmin(db.Model):
  __tablename__ = '__admins'
  __table_args__ = {
    'mysql_engine': 'InnoDB'
  }
  id = db.Column(db.Integer(), primary_key=True)
  source_id = db.Column(db.Integer(), db.ForeignKey('admins.id', ondelete='CASCADE'), nullable=False)
  user_id = db.Column(db.Integer(), db.ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
  name = db.Column(db.String(50), nullable=False)
  email = db.Column(db.String(25), nullable=False)
  phone = db.Column(db.String(25), nullable=False)
  status = db.Column(db.Enum(AdminStatus), nullable=False)
  created_at = db.Column(db.DateTime(), nullable=False)
  updated_at = db.Column(db.DateTime(), nullable=False)
  created_by = db.Column(db.String(30), nullable=False)

  def __init__(
    self, source_id, user_id, name, email, phone, status,
    created_at, updated_at, created_by
    ) -> None:
    super().__init__()
    self.source_id = source_id
    self.user_id = user_id
    self.name = name
    self.email = email
    self.phone = phone
    self.status = status
    self.created_at = created_at
    self.updated_at = updated_at
    self.created_by = created_by

