from models import db
from enum import Enum

class PurposeStatus(Enum):
  Active = 'Active'
  Inactive = 'Inactive'

class Purpose(db.Model):
  __tablename__ = 'purposes'
  __table_args__ = {
    'mysql_engine': 'InnoDB'
  }
  id = db.Column(db.Integer(), primary_key=True)
  purpose = db.Column(db.String(100), nullable=False)
  user_id = db.Column(db.Integer(), db.ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
  order_id = db.Column(db.Integer(), db.ForeignKey('orders.id', ondelete='CASCADE'), nullable=False)
  status = db.Column(db.Enum(PurposeStatus), nullable=False, default='Active')
  created_at = db.Column(db.DateTime(), nullable=False)
  updated_at = db.Column(db.DateTime(), nullable=True)
  created_by = db.Column(db.String(30), nullable=False)

  def __init__(
    self, purpose, user_id, order_id, status, created_at, updated_at, created_by
    ) -> None:
    super().__init__()
    self.purpose = purpose
    self.user_id = user_id
    self.order_id = order_id
    self.status = status
    self.created_at = created_at
    self.updated_at = updated_at
    self.created_by = created_by

class DumpPurpose(db.Model):
  __tablename__ = '__purposes'
  __table_args__ = {
    'mysql_engine': 'InnoDB'
  }
  id = db.Column(db.Integer(), primary_key=True)
  source_id = db.Column(db.Integer(), db.ForeignKey('purposes.id', ondelete='CASCADE'), nullable=False)
  purpose = db.Column(db.String(100), nullable=False)
  user_id = db.Column(db.Integer(), db.ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
  order_id = db.Column(db.Integer(), db.ForeignKey('orders.id', ondelete='CASCADE'), nullable=False)
  status = db.Column(db.Enum(PurposeStatus), nullable=False, default='Active')
  created_at = db.Column(db.DateTime(), nullable=False)
  updated_at = db.Column(db.DateTime(), nullable=True)
  created_by = db.Column(db.String(30), nullable=False)

  def __init__(
    self, source_id, purpose, user_id, order_id, status, created_at, updated_at, created_by
    ) -> None:
    super().__init__()
    self.source_id = source_id
    self.purpose = purpose
    self.user_id = user_id
    self.order_id = order_id
    self.status = status
    self.created_at = created_at
    self.updated_at = updated_at
    self.created_by = created_by
