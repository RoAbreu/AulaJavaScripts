# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from google.appengine.ext import ndb
from gaegraph.model import Node
from gaeforms.ndb import property


class Preco:float(Node):
    Descricao = ndb.StringProperty(required=True)
    Editora = ndb.StringProperty(required=True)
    Edicao = ndb.StringProperty(required=True)
    Autor = ndb.StringProperty(required=True)
    Titulo = ndb.StringProperty(required=True)

