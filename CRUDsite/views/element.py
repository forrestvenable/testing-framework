from models import db
from django.http import HttpResponse
from forms import element
import json

def create(request):
    if request.method == 'GET':
        return render(request, 'create.html', {
            'form': element.CreateForm(),
            'type': 'element',
            'action': 'create',
            'method': 'POST'
            })

    elif request.method == 'POST':
        cursor = db.connection.cursor()
        cursor.execute("INSERT INTO elements (name, description, selector) VALUES (%s, %s, %s)",
            (request.POST.name, request.POST.description, request.POST.selector))
        db.connection.commit()
        cursor.close()
        return HttpResponse("Created!")

def show(request, element_id):
    cursor = db.connection.cursor()
    cursor.execute("SELECT * FROM elements WHERE id = %s LIMIT 1",
        (element_id,))
    element = db.element(cursor.fetchone())
    cursor.execute("SELECT id, name, url FROM pages WHERE id = %s LIMIT 1",
        (element.page_id,))
    pages = map(db.page, cursor.fetchall())
    cursor.execute("SELECT id, name FROM components WHERE id = %s LIMIT 1",
        (element.component_id,))
    components = map(db.component, cursor.fetchall())
    cursor.close()
    return render(request, 'show.html', {
        'item': element,
        'keys': element.properties(),
        'relationships': (pages, components),
        })

def index(request):
    cursor = db.connection.cursor()
    cursor.execute("SELECT * FROM elements")
    elements = map(db.element, cursor.fetchall())
    cursor.close()
    return render(request, 'index.html'. {
        'type': 'element',
        'item_list': elements,
        'keys': list(elements[0].keys()),
        })

def delete(request, element_id):
    cursor = db.connection.cursor()
    cursor.execute("DELETE FROM elements WHERE id = %s",
        (element_id,))
    db.connection.commit()
    cursor.close()
    return HttpResponse("Deleted!")

def update(request, element_id):
    if request.method == 'GET':
        cursor = db.connection.cursor()
        cursor.execute("SELECT * FROM elements WHERE id = %s",
        (element_id,))
        elem = db.element(cursor.fetchone())
        form = element.CreateForm(initials={'name': elem.name, 'description': elem.description, 'selector': elem.selector})
        cursor.close()
        return render(request, 'create.html', {
            'form': form,
            'type': 'element',
            'action': 'update',
            'method': 'POST'
            })

    elif request.method == 'POST':
        cursor = db.connection.cursor()
        cursor.execute("UPDATE elements SET name = %s, description = %s, selector = %s WHERE id = %s",
            (request.POST.name, request.POST.description, request.POST.selector, element_id))
        db.connection.commit()
        cursor.close()
        return HttpResponse("Updated!")