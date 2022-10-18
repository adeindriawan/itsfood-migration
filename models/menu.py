from models import db
from enum import Enum

class MenuType(Enum):
  Food = 'Food'
  Beverage = 'Beverage'
  Snack = 'Snack'
  Grocery = 'Grocery'
  Fruit = 'Fruit'
  Others = 'Others'

class MenuStatus(Enum):
  Registered = 'Registered'
  Activated = 'Activated'
  Locked = 'Locked'
  Suspended = 'Suspended'

class Menu(db.Model):
  __tablename__ = 'menus'
  __table_args__ = {
    'mysql_engine': 'InnoDB'
  }
  id = db.Column(db.Integer(), primary_key=True)
  name = db.Column(db.String(100), nullable=False)
  description = db.Column(db.String(255), nullable=False)
  type = db.Column(db.Enum(MenuType), nullable=False)
  cogs = db.Column(db.Integer(), nullable=False)
  retail_price = db.Column(db.Integer(), nullable=False)
  wholesale_price = db.Column(db.Integer(), nullable=False)
  min_order_qty = db.Column(db.Integer(), nullable=False, default=1)
  max_order_qty = db.Column(db.Integer(), nullable=True)
  pre_order_days = db.Column(db.Integer(), nullable=False, default=0)
  pre_order_hours = db.Column(db.Integer(), nullable=False, default=0)
  discount = db.Column(db.Float(), nullable=True)
  image = db.Column(db.String(20), nullable=False)
  vendor_id = db.Column(db.Integer(), db.ForeignKey('vendors.id', ondelete='CASCADE'), nullable=False)
  status = db.Column(db.Enum(MenuStatus), nullable=False, default='Activated')
  created_by = db.Column(db.String(30), nullable=False)
  created_at = db.Column(db.DateTime(), nullable=False)
  updated_at = db.Column(db.DateTime(), nullable=True)

  def __init__(
    self, id, name, description, type, cogs, retail_price, wholesale_price,
    min_order_qty, max_order_qty, pre_order_days,
    pre_order_hours, discount, image, vendor_id, status, created_by, created_at,
    updated_at) -> None:
    super().__init__()
    self.id = id
    self.name = name
    self.description = description
    self.type = type
    self.cogs = cogs
    self.retail_price = retail_price
    self.wholesale_price = wholesale_price
    self.min_order_qty = min_order_qty
    self.max_order_qty = max_order_qty
    self.pre_order_days = pre_order_days
    self.pre_order_hours = pre_order_hours
    self.discount = discount
    self.image = image
    self.vendor_id = vendor_id
    self.status = status
    self.created_by = created_by
    self.created_at = created_at
    self.updated_at = updated_at

class DumpMenu(db.Model):
  __tablename__ = '__menus'
  __table_args__ = {
    'mysql_engine': 'InnoDB'
  }
  id = db.Column(db.Integer(), primary_key=True)
  # Pada production, harusnya source_id ini memiliki relasi ke primary key di menus, tapi karena
  # pada proses migration terdapat menu yang sudah didump namun tidak ada di tabel asli,
  # maka relasi tersebut untuk sementara dihilangkan
  # source_id = db.Column(db.Integer(), db.ForeignKey('menus.id', ondelete='CASCADE'), nullable=False)
  source_id = db.Column(db.Integer(), nullable=False)
  name = db.Column(db.String(100), nullable=False)
  description = db.Column(db.String(255), nullable=False)
  type = db.Column(db.Enum(MenuType), nullable=False)
  cogs = db.Column(db.Integer(), nullable=False)
  retail_price = db.Column(db.Integer(), nullable=False)
  wholesale_price = db.Column(db.Integer(), nullable=False)
  min_order_qty = db.Column(db.Integer(), nullable=False, default=1)
  max_order_qty = db.Column(db.Integer(), nullable=True)
  pre_order_days = db.Column(db.Integer(), nullable=False, default=0)
  pre_order_hours = db.Column(db.Integer(), nullable=False, default=0)
  discount = db.Column(db.Float(), nullable=True)
  image = db.Column(db.String(20), nullable=False)
  vendor_id = db.Column(db.Integer(), db.ForeignKey('vendors.id', ondelete='CASCADE'), nullable=False)
  status = db.Column(db.Enum(MenuStatus), nullable=False, default='Suspended')
  created_at = db.Column(db.DateTime(), nullable=False)
  updated_at = db.Column(db.DateTime(), nullable=True)
  created_by = db.Column(db.String(30), nullable=False)

  def __init__(
    self, source_id, name, description, type, cogs, retail_price, wholesale_price,
    min_order_qty, max_order_qty, pre_order_days,
    pre_order_hours, discount, image, vendor_id, status, created_at, updated_at,
    created_by) -> None:
    super().__init__()
    self.source_id = source_id
    self.name = name
    self.description = description
    self.type = type
    self.cogs = cogs
    self.retail_price = retail_price
    self.wholesale_price = wholesale_price
    self.min_order_qty = min_order_qty
    self.max_order_qty = max_order_qty
    self.pre_order_days = pre_order_days
    self.pre_order_hours = pre_order_hours
    self.discount = discount
    self.image = image
    self.vendor_id = vendor_id
    self.status = status
    self.created_at = created_at
    self.updated_at = updated_at
    self.created_by = created_by
