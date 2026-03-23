from pony.orm import Database, Required, Optional, Set, PrimaryKey
from datetime import datetime

db = Database()

class Planina(db.Entity):
  _table_ = "planina"
  id = PrimaryKey(int, auto = True)
  naziv = Required(str)
  podrucje = Required(str)
  vrhovi = Set('Vrh')


class Vrh(db.Entity):
  _table_ = "vrh"
  id = PrimaryKey(int, auto = True)
  naziv = Required(str)
  planina = Required(Planina, reverse = 'vrhovi')
  visina = Required(int)
  izleti = Set('Izlet')


class Izlet(db.Entity):
  _table_ = "izlet"
  id = PrimaryKey(int, auto = True)
  vrh = Required(Vrh, reverse = 'izleti')
  datum = Required(datetime)
  ruta = Optional(str)
  opis = Optional(str)
  trajanje = Optional(str)
  tezina = Optional(str)