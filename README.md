# Residence App

### Requerimientos

Instalar las siguientes herramientas:
- MySQL
- Python
- pip

Ya que tengan pip, correr el siguiente comando en la terminal
```
pip install -r requirements.txt
```
### Para correr la aplicación

Ya que tienen todo instalado, en terminal, ir al folder del proyecto, ahi correr el siguiente comando dependiendo de su sistema operativo.

para Linux o macOS:
```
export FLASK_APP=app.py
```

para Windows:
```
set FLASK_APP=app.py
```

y después:
```
python -m flask run
```

en su browser, ir a `localhost:5000` y ya se puede hacer login

# ¿Qué Funciona?
* Login (User Side)
* Leer Códigos ed Qr y guardar la info

# ¿Que Falta?
* Login (Guardian Side)
* Terminar la base de datos 
* Forms para generar el qr
* Security in Login


