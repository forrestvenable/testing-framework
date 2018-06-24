from models import db
from django.http import HttpResponse
from forms import component

def create(request):
    if request.method == 'GET':
        return render(request, 'component.html', {'form': component.CreateForm()})

    elif request.method == 'POST':
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
    if request.method == 'GET':
        pass

    elif request.method == 'POST':
        cursor = db.connection.cursor()
        cursor.execute("UPDATE components SET name = %s WHERE id = %s",
            (request.POST.name, component_id))
        db.connection.commit()
        return HttpResponse("Updated!")