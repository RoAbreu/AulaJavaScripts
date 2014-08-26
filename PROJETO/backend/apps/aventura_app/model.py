# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from google.appengine.ext import ndb
from gaegraph.model import Node
from gaeforms.ndb import property


class Avenura(Node):
    Titulo = ndb.StringProperty(required=True)
    Autor = ndb.StringProperty(required=True)
    Editora = ndb.StringProperty(required=True)
    Edicao = ndb.DateProperty(required=True)
    Descricao = ndb.StringProperty(required=True)
    Preco = ndb.FloatProperty(required=True)

