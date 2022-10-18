from models import db, Group
from datetime import datetime

def groups_migration():
  groups = ['FSAD', 'FTK', 'FTIRS', 'FTEIC', 'FTSPK', 'FDBKD', 'FV', 'MMT', 'Pascasarjana', 'Rektorat', 'Unit ITS', 'Ormawa', 'Lainnya']
  for group in groups:
    group_entry = Group(group, 'Active', datetime.now(), None, 'Migration System')
    db.session.add(group_entry)
    db.session.commit()
    new_group_id = group_entry.id
    new_group = Group.query.get(new_group_id)
    db.session.add(new_group)
    db.session.commit()
    