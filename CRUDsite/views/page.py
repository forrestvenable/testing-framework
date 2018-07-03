from models import db
from django.http import HttpResponse
from forms import page
import json

def create(request):
    if request.method == 'GET':
        return render(request, 'create.html', {
            'form': page.CreateForm(),
            'type': 'page',
            'action': 'create',
            'method': 'POST'
            })

    elif request.method == 'POST':
        cursor = db.connection.cursor()
        cursor.execute("INSERT INTO pages (name, url) VALUES (%s, %s)",
            (request.POST.name, request.POST.url))
        db.connection.commit()
        return HttpResponse(status=201)

def show(request, page_id):
    cursor = db.connection.cursor()
    cursor.execute("SELECT * FROM pages WHERE id = %s LIMIT 1",
        (page_id,))
    page = db.page(cursor.fetchone())
    cursor.execute("SELECT id, name FROM components INNER JOIN pages_components ON component.id = pages_components.component_id WHERE pages_components.page_id=%s",
        (page_id,))
    components = db.component(cursor.fetchall())
    cursor.execute("SELECT id, name, description, selector FROM elements WHERE page_id = %s",
        (page_id,))
    elements = map(db.element, cursor.fetchall())
    return render(request, 'show.html', {
        'item': component,
        'keys': component.properties(),
        'relationships': (components, elements),
        })

def index(request):
    cursor = db.connection.cursor()
    cursor.execute("SELECT * FROM pages")
    pages = map(db.page, cursor.fetchall())
    return render(request, 'index.html'. {
        'type': 'pages',
        'item_list': pages,
        'keys': list(pages[0].keys()),
        })

def delete(request, page_id):
    cursor = db.connection.cursor()
    cursor.execute("DELETE FROM pages WHERE id = %s",
        (page_id,))
    db.connection.commit()
    return HttpResponse("Deleted!")

def update(request, page_id):
    if request.method == 'GET':
        cursor = db.connection.cursor()
        cursor.execute("SELECT * FROM pages WHERE id = %s",
        (page_id,))
        page_db = db.page(cursor.fetchone())
        form = page.CreateForm(initials={'name': page_db.name, 'url': page_db.url})
        return render(request, 'create.html', {
            'form': form,
            'type': 'page',
            'action': 'update',
            'method': 'POST'
            })

    elif request.method == 'POST':
        cursor = db.connection.cursor()
        cursor.execute("UPDATE components SET name = %s, url = %s WHERE id = %s",
            (request.POST.name, request.POST.url, page_id))
        db.connection.commit()
        return HttpResponse("Updated!")
