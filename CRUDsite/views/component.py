from models import db
from django.http import HttpResponse

def create(request):
    cursor = db.connection.cursor()
    # INSERT QUERY HERE
    db.connection.commit()
    # INSERT HTML HERE

def show(request, id):
    cursor = db.connection.cursor()
    # INSERT QUERY HERE
    # INSERT HTML HERE

def index(request):
    cursor = db.connection.cursor()
    # INSERT QUERY HERE
    # INSERT HTML HERE

def delete(request, id):
    cursor = db.connection.cursor()
    # INSERT QUERY HERE
    db.connection.commit()
    # INSERT HTML HERE

def update(request. id):
    cursor = db.connection.cursor()
    # INSERT QUERY HERE
    db.connection.commit()
    # INSERT HTML HERE