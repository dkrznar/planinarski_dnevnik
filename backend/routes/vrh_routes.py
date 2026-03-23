from flask import Blueprint, render_template, request, redirect, url_for
from pony.orm import db_session
from models import Planina, Vrh

vrh_bp = Blueprint('vrh', __name__)

@vrh_bp.route('/vrhovi')
@db_session
def vrh():
  svi_vrhovi = Vrh.select()[:]
  return render_template('vrhovi.html', vrhovi = svi_vrhovi)

@vrh_bp.route('/vrhovi/nova', methods = ['GET', 'POST'])
@db_session
def novi_vrh():
  if request.method == 'POST':
    naziv = request.form['naziv']
    visina = request.form['visina']
    planina_id = request.form['planina_id']
    Vrh(
      naziv = naziv,
      visina = int(visina),
      planina = Planina[planina_id]
    )
    return redirect(url_for('vrh.vrh'))
  planine = Planina.select()[:]
  return render_template('novi_vrh.html', planine = planine)

@vrh_bp.route('/vrhovi/<int:id>/uredi', methods = ['GET', 'POST'])
@db_session
def uredi_vrh(id):
  vrh = Vrh[id]

  if request.method == 'POST':
    vrh.naziv = request.form['naziv']
    vrh.visina = int(request.form['visina'])    
    return redirect(url_for('vrh.vrh'))
  planine = Planina.select()[:]
  return render_template('uredi_vrh.html', vrh = vrh, planine = planine)


@vrh_bp.route('/vrhovi/<int:id>/obrisi', methods = ['POST'])
@db_session
def obrisi_vrh(id):
  vrh = Vrh[id]
  vrh.delete()
  return redirect(url_for('vrh.vrh'))