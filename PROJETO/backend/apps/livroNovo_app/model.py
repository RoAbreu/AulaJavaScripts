# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from google.appengine.ext import ndb
from gaegraph.model import Node
from gaeforms.ndb import property


class LivroNovo(Node):
    preco = property.SimpleCurrency(required=True)
    titulo = ndb.StringProperty(required=True)
    autor = ndb.StringProperty(required=True)

