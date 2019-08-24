# template BD universidad

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

en su browser, ir a `localhost:5000` y navegar por los queries desde ahi.

## ¿Cómo esta organizada la aplicación?
```
universidad/
  static/
    styles.css
  templates/
    members.html
  app.py
  db.py
  README.md
  requirements.txt
```

- En `app.py` se encuentran las rutas de la aplicación.
- `db.py` contiene la conexión a la base de datos y algunos queries de ejemplo.
- `README.md` es este documento.
- `requirements.txt` contiene las librerias necesarias para que este proyecto funcione.
- En el folder `templates/`, estan los `html` para ver los resultados de los queries.
- En el folder `static/` se encuentra el css para el html.

Ustedes tendrán que modificar `db.py`, `app.py` y agregar mas templates en el folder de `templates/`