# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from google.appengine.ext import ndb
from gaegraph.model import Node
from gaeforms.ndb import property


class Teste(Node):
    preco = ndb.FloatProperty(required=True)
    autor = ndb.StringProperty(required=True)
    editora = ndb.StringProperty(required=True)
    descricao = ndb.StringProperty(required=True)
    edicao = ndb.StringProperty(required=True)
    titulo = ndb.StringProperty(required=True)

