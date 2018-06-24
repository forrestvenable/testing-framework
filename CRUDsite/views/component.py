from models import db
from django.http import HttpResponse

def create(request):
    cursor = db.connection.cursor()
    cursor.execute("INSERT INTO components (name) VALUES (%s)",
        (request.POST.name,))
    db.connection.commit()
    return HttpResponse("Created!")

def show(request, component_id):
    cursor = db.connection.cursor()
    cursor.execute("SELECT * FROM components WHERE id = %s LIMIT 1",
        (component_id,))
    component = db.component(cursor.fetchone())
    return HttpResponse(component.to_json())

def index(request):
    cursor = db.connection.cursor()
    cursor.execute("SELECT * FROM components")
    components = map(db.component, cursor.fetchall())
    return HttpResponse(json.dumps(components.__dict__))

def delete(request, component_id):
    cursor = db.connection.cursor()
    cursor.execute("DELETE FROM components WHERE id = %s",
        (component_id,))
    db.connection.commit()
    return HttpResponse("Deleted!")

def update(request. component_id):
    cursor = db.connection.cursor()
    cursor.execute("UPDATE components SET name = %s WHERE id = %s",
        (request.POST.name, component_id))
    db.connection.commit()
    return HttpResponse("Updated!")