from models import db
from django.http import HttpResponse

def create(request):
    cursor = db.connection.cursor()
    cursor.execute("INSERT INTO components (name) VALUES (%s)",
        (request.POST.name,))
    db.connection.commit()
    # INSERT HTML HERE

def show(request, component_id):
    cursor = db.connection.cursor()
    cursor.execute("SELECT * FROM components WHERE id = %s LIMIT 1",
        (component_id,))
    component = db.component(cursor.fetchone())
    # INSERT HTML HERE

def index(request):
    cursor = db.connection.cursor()
    cursor.execute("SELECT * FROM components")
    components = map(db.component, cursor.fetchall())
    # INSERT HTML HERE

def delete(request, component_id):
    cursor = db.connection.cursor()
    cursor.execute("DELETE FROM components WHERE id = %s",
        (component_id,))
    db.connection.commit()
    # INSERT HTML HERE

def update(request. component_id):
    cursor = db.connection.cursor()
    cursor.execute("UPDATE components SET name = %s WHERE id = %s",
        (request.POST.name, component_id))
    db.connection.commit()
    # INSERT HTML HERE