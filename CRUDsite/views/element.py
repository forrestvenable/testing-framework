from models import db
from django.http import HttpResponse
from forms import element

def create(request):
    if request.method == 'GET':
        return render(request, 'element.html', {'form': element.CreateForm()})

    elif request.method == 'POST':
        cursor = db.connection.cursor()
        cursor.execute("INSERT INTO elements (name, description, selector) VALUES (%s, %s, %s)",
            (request.POST.name, request.POST.description, request.POST.selector))
        db.connection.commit()
        return HttpResponse("Created!")

def show(request, element_id):
    cursor = db.connection.cursor()
    cursor.execute("SELECT * FROM elements WHERE id = %s LIMIT 1",
        (element_id,))
    element = db.element(cursor.fetchone())
    return HttpResponse(element.to_json())

def index(request):
    cursor = db.connection.cursor()
    cursor.execute("SELECT * FROM elements")
    elements = map(db.element, cursor.fetchall())
    return HttpResponse(json.dumps(elements.__dict__))

def delete(request, element_id):
    cursor = db.connection.cursor()
    cursor.execute("DELETE FROM elements WHERE id = %s",
        (element_id,))
    db.connection.commit()
    return HttpResponse("Deleted!")

def update(request. element_id):
    if request.method == 'GET':
        pass

    elif request.method == 'POST':
        cursor = db.connection.cursor()
        cursor.execute("UPDATE elements SET name = %s, description = %s, selector = %s WHERE id = %s",
            (request.POST.name, request.POST.description, request.POST.selector, element_id))
        db.connection.commit()
        return HttpResponse("Updated!")