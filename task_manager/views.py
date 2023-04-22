from django.shortcuts import render
from . import settings


def service(request):
    from django.db import connections
    from django.db.utils import OperationalError
    db_conn = connections['default']
    try:
        _ = db_conn.cursor()
    except OperationalError:
        db_connected = False
    else:
        db_connected = True
    return render(
        request,
        'service.html',
        context={
            'who': "Andrey",
            'secret_key': settings.SECRET_KEY,
            'db_connected': db_connected
        }
    )
