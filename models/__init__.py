from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .group import Group
from .unit import Unit
from .user import User, DumpUser
from .customer import Customer, DumpCustomer
from .vendor import Vendor, DumpVendor
from .menu import Menu, DumpMenu
from .payment import Payment
from .payment_detail import PaymentDetail
from .order import Order, DumpOrder
from .order_detail import OrderDetail, DumpOrderDetail
from .cost import Cost, DumpCost
from .discount import Discount, DumpDiscount
from .admin import Admin, DumpAdmin
from .addresses import Address, DumpAddress
from .purposes import Purpose, DumpPurpose