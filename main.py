from comunidadeti import app
from comunidadeti import database

with app.app_context():
    if __name__ == '__main__':
        app.run(debug=True)
        database.create_all()
