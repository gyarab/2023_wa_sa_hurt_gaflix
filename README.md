# 2023_wa_sa_chalupnicek_gaflix

## První inicializace projektu

```bash
# vyklonovat repozitar a vlezt do nej
git clone git@github.com:gyarab/2023_wa_sa_chalupnicek_gaflix.git
cd 2023_wa_sa_chalupnicek_gaflix/

# vytvorit venv a aktivovat
py -3 -m venv venv
source ./venv/Scripts/activate

# nainstalovat zavislosti
pip install -r requirements.txt
```

```
./manage.py migrate
./manage.py createsuperuser
./manage.py runserver
```

## Spuštění projektu

```
git pull
source ./venv/Scripts/activate
./manage.py migrate
./manage.py runserver
```

## Po změně `models.py`

```
./manage.py makemigrations
./manage.py migrate
```