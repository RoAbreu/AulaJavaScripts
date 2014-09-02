# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaebusiness.gaeutil import SaveCommand, ModelSearchCommand
from gaeforms.ndb.form import ModelForm
from gaegraph.business_base import UpdateNode
from didaticos_app.model import Didaticos

class DidaticosPublicForm(ModelForm):
    """
    Form used to show properties on app's home
    """
    _model_class = Didaticos
    _include = [Didaticos.Autor, 
                Didaticos.preco, 
                Didaticos.edicao, 
                Didaticos.titulo, 
                Didaticos.descricao, 
                Didaticos.editora]


class DidaticosForm(ModelForm):
    """
    Form used to save and update operations on app's admin page
    """
    _model_class = Didaticos
    _include = [Didaticos.Autor, 
                Didaticos.preco, 
                Didaticos.edicao, 
                Didaticos.titulo, 
                Didaticos.descricao, 
                Didaticos.editora]


class DidaticosDetailForm(ModelForm):
    """
    Form used to show entity details on app's admin page
    """
    _model_class = Didaticos
    _include = [Didaticos.creation, 
                Didaticos.Autor, 
                Didaticos.preco, 
                Didaticos.titulo, 
                Didaticos.edicao, 
                Didaticos.descricao, 
                Didaticos.editora]


class DidaticosShortForm(ModelForm):
    """
    Form used to show entity short version on app's admin page, mainly for tables
    """
    _model_class = Didaticos
    _include = [Didaticos.creation, 
                Didaticos.Autor, 
                Didaticos.preco, 
                Didaticos.titulo, 
                Didaticos.edicao, 
                Didaticos.descricao, 
                Didaticos.editora]


class SaveDidaticosCommand(SaveCommand):
    _model_form_class = DidaticosForm


class UpdateDidaticosCommand(UpdateNode):
    _model_form_class = DidaticosForm


class ListDidaticosCommand(ModelSearchCommand):
    def __init__(self):
        super(ListDidaticosCommand, self).__init__(Didaticos.query_by_creation())

