# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaebusiness.gaeutil import SaveCommand, ModelSearchCommand
from gaeforms.ndb.form import ModelForm
from gaegraph.business_base import UpdateNode
from listaDidaticos_app.model import ListaDidaticos

class ListaDidaticosPublicForm(ModelForm):
    """
    Form used to show properties on app's home
    """
    _model_class = ListaDidaticos
    _include = [ListaDidaticos.autor, 
                ListaDidaticos.preco, 
                ListaDidaticos.edicao, 
                ListaDidaticos.titulo, 
                ListaDidaticos.descricao, 
                ListaDidaticos.editora]


class ListaDidaticosForm(ModelForm):
    """
    Form used to save and update operations on app's admin page
    """
    _model_class = ListaDidaticos
    _include = [ListaDidaticos.autor, 
                ListaDidaticos.preco, 
                ListaDidaticos.edicao, 
                ListaDidaticos.titulo, 
                ListaDidaticos.descricao, 
                ListaDidaticos.editora]


class ListaDidaticosDetailForm(ModelForm):
    """
    Form used to show entity details on app's admin page
    """
    _model_class = ListaDidaticos
    _include = [ListaDidaticos.creation, 
                ListaDidaticos.autor, 
                ListaDidaticos.preco, 
                ListaDidaticos.titulo, 
                ListaDidaticos.edicao, 
                ListaDidaticos.descricao, 
                ListaDidaticos.editora]


class ListaDidaticosShortForm(ModelForm):
    """
    Form used to show entity short version on app's admin page, mainly for tables
    """
    _model_class = ListaDidaticos
    _include = [ListaDidaticos.creation, 
                ListaDidaticos.autor, 
                ListaDidaticos.preco, 
                ListaDidaticos.titulo, 
                ListaDidaticos.edicao, 
                ListaDidaticos.descricao, 
                ListaDidaticos.editora]


class SaveListaDidaticosCommand(SaveCommand):
    _model_form_class = ListaDidaticosForm


class UpdateListaDidaticosCommand(UpdateNode):
    _model_form_class = ListaDidaticosForm


class ListListaDidaticosCommand(ModelSearchCommand):
    def __init__(self):
        super(ListListaDidaticosCommand, self).__init__(ListaDidaticos.query_by_creation())

