from pony.orm import Database, Required, Optional, PrimaryKey
from datetime import datetime

db = Database()

class Izlet(db.Entity):
  _table_ = "izlet"
  id = PrimaryKey(int, auto = True)
  planina = Required(str)
  vrh = Required(str)
  datum = Required(datetime)
  ruta = Optional(str)
  opis = Optional(str)
  trajanje = Optional(str)
  tezina = Optional(str)