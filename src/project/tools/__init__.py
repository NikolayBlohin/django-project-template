#!/usr/bin/env python
# encoding: utf-8
import pymongo
from functools import wraps
from django.conf import settings
from django.template import RequestContext
from django.shortcuts import render_to_response





def render_to(template):
    def renderer(func):
        @wraps(func)
        def wrapper(request, *args, **kw):
            output = func(request, *args, **kw)
            if isinstance(output, (list, tuple)):
                data = output[0]
                return render_to_response(output[1], data, RequestContext(request))
            elif isinstance(output, dict):
                data = output
                return render_to_response(template, data, RequestContext(request))
            else:
                return output
        return wrapper
    return renderer



# MongoDB stuff ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def get_db(db_name):
    connection = pymongo.MongoClient(
        settings.MONGO_DB_SETTINGS.host,
        settings.MONGO_DB_SETTINGS.port
    )
    return connection[db_name]


def get_collection(db_name, collection_name):
    DB = get_db(db_name)
    collection = DB[collection_name]
    return collection

