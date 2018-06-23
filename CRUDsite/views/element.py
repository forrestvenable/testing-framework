from models import db
from django.http import HttpResponse

def create(request):
    cursor = db.connection.cursor()
    cursor.execute("INSERT INTO elements (name, description, selector) VALUES (%s, %s, %s)",
        (request.POST.name, request.POST.description, request.POST.selector))
    db.connection.commit()
    # INSERT HTML HERE

def show(request, element_id):
    cursor = db.connection.cursor()
    cursor.execute("SELECT * FROM elements WHERE id = %s LIMIT 1",
        (element_id,))
    element = db.element(cursor.fetchone())
    # INSERT HTML HERE

def index(request):
    cursor = db.connection.cursor()
    cursor.execute("SELECT * FROM elements")
    elements = map(db.element, cursor.fetchall())
    # INSERT HTML HERE

def delete(request, element_id):
    cursor = db.connection.cursor()
    cursor.execute("DELETE FROM elements WHERE id = %s",
        (element_id,))
    db.connection.commit()
    # INSERT HTML HERE

def update(request. element_id):
    cursor = db.connection.cursor()
    cursor.execute("UPDATE elements SET name = %s, description = %s, selector = %s WHERE id = %s",
        (request.POST.name, request.POST.description, request.POST.selector, element_id))
    db.connection.commit()
    # INSERT HTML HERE