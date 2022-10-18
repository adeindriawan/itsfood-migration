from flask import Flask
import json
from models import db
from controllers import groups_migration, units_migrations, import_customer_and_migrate, \
  import_vendor_and_migrate, import_menu_and_migrate, import_orders_and_migrate, import_order_details_and_migrate, \
  import_admin_and_migrate

app = Flask(__name__)
app.config.from_file('config.json', load=json.load)
app.config['SQLALCHEMY_DATABASE_URI'] = app.config['DB_CONN']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.route('/')
def main():
  return 'should be okay (6)'

@app.route('/groups/migrate')
def run_groups_migration():
  groups_migration()
  return 'Groups have been successfully migrated'

@app.route('/units/migrate')
def run_units_migration():
  units_migrations()
  return 'Units have been successfully migrated'

@app.route('/customers/import-and-migrate')
def run_customers_migration():
  import_customer_and_migrate()
  return 'Customers have been successfully migrated'

@app.route('/vendors/import-and-migrate')
def run_vendors_migration():
  import_vendor_and_migrate()
  return 'Vendors have been successfully migrated'

@app.route('/menus/import-and-migrate')
def run_menus_migration():
  import_menu_and_migrate()
  return 'Menus have been successfully migrated'

@app.route('/orders/import-and-migrate')
def run_orders_migration():
  import_orders_and_migrate()
  return 'Orders have been successfully migrated'

@app.route('/order-details/import-and-migrate')
def run_order_details_migration():
  import_order_details_and_migrate()
  return 'Order details have been successfully migrated'

@app.route('/admins/import-and-migrate')
def run_admins_migration():
  import_admin_and_migrate()
  return 'Admins have been successfully migrated'

# open SSH
# activate the env
# run python migration.py
if __name__ == '__main__':
  # https://stackoverflow.com/questions/46540664/no-application-found-either-work-inside-a-view-function-or-push-an-application
  with app.app_context():
    db.create_all()
  app.run(debug=True)
