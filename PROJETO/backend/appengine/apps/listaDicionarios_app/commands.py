# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaebusiness.gaeutil import SaveCommand, ModelSearchCommand
from gaeforms.ndb.form import ModelForm
from gaegraph.business_base import UpdateNode
from listaDicionarios_app.model import ListaDicionarios

class ListaDicionariosPublicForm(ModelForm):
    """
    Form used to show properties on app's home
    """
    _model_class = ListaDicionarios
    _include = [ListaDicionarios.autor, 
                ListaDicionarios.preco, 
                ListaDicionarios.edicao, 
                ListaDicionarios.titulo, 
                ListaDicionarios.descricao, 
                ListaDicionarios.editora]


class ListaDicionariosForm(ModelForm):
    """
    Form used to save and update operations on app's admin page
    """
    _model_class = ListaDicionarios
    _include = [ListaDicionarios.autor, 
                ListaDicionarios.preco, 
                ListaDicionarios.edicao, 
                ListaDicionarios.titulo, 
                ListaDicionarios.descricao, 
                ListaDicionarios.editora]


class ListaDicionariosDetailForm(ModelForm):
    """
    Form used to show entity details on app's admin page
    """
    _model_class = ListaDicionarios
    _include = [ListaDicionarios.creation, 
                ListaDicionarios.autor, 
                ListaDicionarios.preco, 
                ListaDicionarios.titulo, 
                ListaDicionarios.edicao, 
                ListaDicionarios.descricao, 
                ListaDicionarios.editora]


class ListaDicionariosShortForm(ModelForm):
    """
    Form used to show entity short version on app's admin page, mainly for tables
    """
    _model_class = ListaDicionarios
    _include = [ListaDicionarios.creation, 
                ListaDicionarios.autor, 
                ListaDicionarios.preco, 
                ListaDicionarios.titulo, 
                ListaDicionarios.edicao, 
                ListaDicionarios.descricao, 
                ListaDicionarios.editora]


class SaveListaDicionariosCommand(SaveCommand):
    _model_form_class = ListaDicionariosForm


class UpdateListaDicionariosCommand(UpdateNode):
    _model_form_class = ListaDicionariosForm


class ListListaDicionariosCommand(ModelSearchCommand):
    def __init__(self):
        super(ListListaDicionariosCommand, self).__init__(ListaDicionarios.query_by_creation())

