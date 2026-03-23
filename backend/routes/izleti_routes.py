from flask import Blueprint, render_template, request, redirect, url_for
from pony.orm import db_session
from models import Planina, Vrh, Izlet
from datetime import datetime

izlet_bp = Blueprint('izlet', __name__)

@izlet_bp.route('/izleti')
@db_session
def izlet():
  svi_izleti = Izlet.select()[:]
  return render_template('izleti.html', izleti = svi_izleti)

@izlet_bp.route('/izleti/novi', methods = ['GET', 'POST'])
@db_session
def novi_izlet():
  if request.method == 'POST':
    vrh_id = request.form['vrh_id']
    datum = request.form['datum']
    ruta = request.form.get('ruta')
    opis = request.form.get('opis')
    trajanje = request.form.get('trajanje')
    tezina = request.form.get('tezina')

    Izlet(
      vrh = Vrh[vrh_id],
      datum = datetime.strptime(datum, '%Y-%m-%d'),
      ruta = ruta,
      opis = opis,
      trajanje = trajanje,
      tezina = tezina
    )
    return redirect(url_for('izlet.izlet'))
  vrhovi = Vrh.select()[:]
  return render_template('novi_izlet.html', vrhovi = vrhovi)

@izlet_bp.route('/izleti/<int:id>/uredi', methods = ['GET', 'POST'])
@db_session
def uredi_izlet(id):
  izlet = Izlet[id]

  if request.method == 'POST':
    vrh_id = request.form['vrh_id']
    datum = request.form['datum']
    ruta = request.form.get('ruta')
    opis = request.form.get('opis')
    trajanje = request.form.get('trajanje')
    tezina = request.form.get('tezina')
    izlet.vrh = Vrh[vrh_id]
    izlet.datum = datetime.strptime(datum, '%Y-%m-%d')
    izlet.ruta = ruta
    izlet.opis = opis
    izlet.trajanje = trajanje
    izlet.tezina = tezina

    return redirect(url_for('izlet.izlet'))
  vrhovi = Vrh.select()[:]
  return render_template('uredi_izlet.html', izlet = izlet, vrhovi = vrhovi)


@izlet_bp.route('/izleti/<int:id>/obrisi', methods = ['POST'])
@db_session
def obrisi_izlet(id):
  izlet = Izlet[id]
  izlet.delete()
  return redirect(url_for('izlet.izlet'))