from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .group import Group
from .unit import Unit
from .user import User, DumpUser
from .customer import Customer, DumpCustomer
from .vendor import Vendor, DumpVendor
from .menu import Menu, DumpMenu
from .va_payment import VAPayment
from .va_payment_detail import VAPaymentDetail
from .order import Order, DumpOrder
from .order_detail import OrderDetail, DumpOrderDetail
from .cost import Cost, DumpCost
from .discount import Discount, DumpDiscount
from .admin import Admin, DumpAdmin