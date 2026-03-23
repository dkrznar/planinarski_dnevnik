from flask import Blueprint, render_template, request, redirect, url_for
from pony.orm import db_session
from models import Planina

planina_bp = Blueprint('planina', __name__)

@planina_bp.route('/planine')
@db_session
def planine():
  sve_planine = Planina.select()[:]
  return render_template('planine.html', planine = sve_planine)

@planina_bp.route('/planina/nova', methods = ['GET', 'POST'])
@db_session
def nova_planina():
  if request.method == 'POST':
    naziv = request.form['naziv']
    podrucje = request.form['podrucje']
    Planina(
      naziv = naziv,
      podrucje = podrucje
    )
    return redirect(url_for('planina.planine'))
  return render_template('nova_planina.html')

@planina_bp.route('/planina/<int:id>/uredi', methods = ['GET', 'POST'])
@db_session
def uredi_planinu(id):
  planina = Planina[id]

  if request.method == 'POST':
    planina.naziv = request.form['naziv']
    planina.podrucje = request.form['podrucje']
    
    return redirect(url_for('planina.planine'))
  return render_template('uredi_planinu.html', planina = planina)


@planina_bp.route('/planina/<int:id>/obrisi', methods = ['POST'])
@db_session
def obrisi_planinu(id):
  planina = Planina[id]
  planina.delete()
  return redirect(url_for('planina.planine'))