#!/usr/bin/env python
# encoding: utf-8
from django.shortcuts import render

from tools import render_to


@render_to('index.html')
def index(request):
    return {
        'it_is_main': True,
    }
