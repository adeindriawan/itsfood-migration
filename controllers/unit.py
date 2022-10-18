from models import db, Unit
import json
from datetime import datetime

def units_migrations():
  f = open('data/units.json')
  data = json.load(f)
  f.close()
  units = data[2]['data']
  for unit in units:
    unit_entry = Unit(unit['name'], unit['group_id'], 'Active', datetime.now(), None, 'Migration System')
    db.session.add(unit_entry)
    db.session.commit()
    new_unit_id = unit_entry.id
    new_unit = Unit.query.get(new_unit_id)
    new_unit.source_id = new_unit_id
    new_unit.incremental_id = new_unit_id
    db.session.add(new_unit)
    db.session.commit()
    