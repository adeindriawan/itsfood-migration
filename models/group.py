from models import db
from enum import Enum

class GroupStatus(Enum):
  Active = 'Active'
  Inactive = 'Inactive'

class Group(db.Model):
  __tablename__ = 'groups'
  __table_args__ = {
    'mysql_engine': 'InnoDB'
  }
  id = db.Column(db.Integer(), primary_key=True)
  name = db.Column(db.String(20), nullable=False)
  status = db.Column(db.Enum(GroupStatus), nullable=False, default='Active')
  created_at = db.Column(db.DateTime(), nullable=False)
  updated_at = db.Column(db.DateTime(), nullable=True)
  created_by = db.Column(db.String(30), nullable=False)

  def __init__(self, name, status, created_at, updated_at, created_by) -> None:
    super().__init__()
    self.name = name
    self.status = status
    self.created_at = created_at
    self.updated_at = updated_at
    self.created_by = created_by

class DumpGroup(db.Model):
  __tablename__ = '__groups'
  __table_args__ = {
    'mysql_engine': 'InnoDB'
  }
  id = db.Column(db.Integer(), primary_key=True)
  source_id = db.Column(db.Integer(), db.ForeignKey('groups.id', ondelete='CASCADE'), nullable=False)
  name = db.Column(db.String(20), nullable=False)
  status = db.Column(db.Enum(GroupStatus), nullable=False, default='Inactive')
  created_at = db.Column(db.DateTime(), nullable=False)
  updated_at = db.Column(db.DateTime(), nullable=True)
  created_by = db.Column(db.String(30), nullable=False)

  def __init__(
    self, source_id, name, status, created_at, updated_at, created_by
    ) -> None:
    super().__init__()
    self.source_id = source_id
    self.name = name
    self.status = status
    self.created_at = created_at
    self.updated_at = updated_at
    self.created_by = created_by
