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
    return HttpResponse(page.to_json())

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
        page = db.page(cursor.fetchone())

    elif request.method == 'POST':
        cursor = db.connection.cursor()
        cursor.execute("UPDATE components SET name = %s, url = %s WHERE id = %s",
            (request.POST.name, request.POST.url, page_id))
        db.connection.commit()
        return HttpResponse("Updated!")
