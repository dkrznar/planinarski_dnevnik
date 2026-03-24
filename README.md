# Planinarski dnevnik
Web aplikacija koja omogućuje pregled, unos, uređivanje i brisanje planinarskih izleta. 

## Tehnologije

- Python/Flask
- PonyORM
- SQLite
- Bootstrap 5
- Chart.js
- Docker

## Pokretanje aplikacije

### Bez Dockera

1.Kloniraj repozitorij

```bash
cd ~/Downloads
git clone https://github.com/dkrznar/planinarski_dnevnik
cd planinarski_dnevnik
```

2. Uđi u 'backend/' mapu

```bash
cd backend
```

3. Kreiraj virtualno okruženje i aktiviraj ga:

```bash
python -m venv venv
.\venv\Scripts\activate
```

4. Insaliraj requirements.txt

```bash
pip install -r requirements.txt
```

5. Pokreni aplikaciju 
```bash
python app.py
```

6. Otvori browser na 'http://127.0.0.1:5000'

### S Dockerom

```bash
docker-compose up --build
```

## Funkcionalnosti 

Aplikacija je zamišljena s ciljem unošenja i pregleda planinarskih izleta. 
- Pregled izleta
- Unos novog izleta: sastoji se od unosa planine, vrha, rute, datuma, opisa, trajanja i težine.
- Uređivanje izleta
- Brisanje izleta
- Vizualizacija izleta - grafikon prikazuje izleta po planinama