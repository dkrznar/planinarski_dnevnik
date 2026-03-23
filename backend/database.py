from models import db

db.bind(
  provider = 'sqlite',
  filename = 'data/baza.db',
  create_db = True
)

db.generate_mapping(create_tables = True)