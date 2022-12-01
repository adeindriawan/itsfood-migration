from models import db
from enum import Enum

class UnitStatus(Enum):
  Active = 'Active'
  Inactive = 'Inactive'

class Unit(db.Model):
  __tablename__ = 'units'
  __table_args__ = {
    'mysql_engine': 'InnoDB'
  }
  id = db.Column(db.Integer(), primary_key=True)
  name = db.Column(db.String(30), nullable=False)
  group_id = db.Column(db.Integer(), db.ForeignKey('groups.id', ondelete='CASCADE'), nullable=False)
  status = db.Column(db.Enum(UnitStatus), nullable=False, default='Active')
  created_at = db.Column(db.DateTime(), nullable=False)
  updated_at = db.Column(db.DateTime(), nullable=True)
  created_by = db.Column(db.String(30), nullable=False)

  def __init__(self, id, name, group_id, status, created_at, updated_at, created_by) -> None:
    super().__init__()
    self.id = id
    self.name = name
    self.group_id = group_id
    self.status = status
    self.created_at = created_at
    self.updated_at = updated_at
    self.created_by = created_by

class DumpUnit(db.Model):
  __tablename__ = '__units'
  __table_args__ = {
    'mysql_engine': 'InnoDB'
  }
  id = db.Column(db.Integer(), primary_key=True)
  source_id = db.Column(db.Integer(), db.ForeignKey('units.id', ondelete='CASCADE'), nullable=False)
  name = db.Column(db.String(30), nullable=False)
  group_id = db.Column(db.Integer(), db.ForeignKey('groups.id', ondelete='CASCADE'), nullable=False)
  status = db.Column(db.Enum(UnitStatus), nullable=False, default='Inactive')
  created_at = db.Column(db.DateTime(), nullable=False)
  updated_at = db.Column(db.DateTime(), nullable=True)
  created_by = db.Column(db.String(30), nullable=False)

  def __init__(
    self, source_id, name, group_id, status, created_at, updated_at, created_by
    ) -> None:
    super().__init__()
    self.source_id = source_id
    self.name = name
    self.group_id = group_id
    self.status = status
    self.created_at = created_at
    self.updated_at = updated_at
    self.created_by = created_by