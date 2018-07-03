from models import db
from django.http import HttpResponse
from forms import component
import json

def create(request):
    if request.method == 'GET':
        return render(request, 'create.html', {
            'form': component.CreateForm(),
            'type': 'component',
            'action': 'create',
            'method': 'POST'
            })

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
    cursor.execute("SELECT id, name, url FROM pages INNER JOIN pages_components ON pages.id = pages_components.page_id WHERE pages_components.component_id=%s",
        (component_id,))
    parents = db.page(cursor.fetchall())
    cursor.execute("SELECT id, name, description, selector FROM elements WHERE component_id = %s",
        (component_id,))
    children = db.element(cursor.fetchall())
    return render(request, 'show.html', {
        'item': component,
        'keys': component.properties(),
        'relationships': (parents, children),
        })

def index(request):
    cursor = db.connection.cursor()
    cursor.execute("SELECT * FROM components")
    components = map(db.component, cursor.fetchall())
    return render(request, 'index.html'. {
        'type': 'component',
        'item_list': components,
        'keys': list(components[0].keys()),
        })

def delete(request, component_id):
    cursor = db.connection.cursor()
    cursor.execute("DELETE FROM components WHERE id = %s",
        (component_id,))
    db.connection.commit()
    return HttpResponse("Deleted!")

def update(request, component_id):
    if request.method == 'GET':
        cursor = db.connection.cursor()
        cursor.execute("SELECT * FROM components WHERE id = %s",
        (component_id,))
        comp = db.component(cursor.fetchone())   
        form = component.CreateForm(initials={"name": comp.name})
        return render(request, 'create.html', {
            'form': form,
            'type': 'component',
            'action': 'create',
            'method': 'POST'
            }) 

    elif request.method == 'POST':
        cursor = db.connection.cursor()
        cursor.execute("UPDATE components SET name = %s WHERE id = %s",
            (request.POST.name, component_id))
        db.connection.commit()
        return HttpResponse("Updated!")