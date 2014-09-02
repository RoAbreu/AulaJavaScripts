# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaebusiness.gaeutil import SaveCommand, ModelSearchCommand
from gaeforms.ndb.form import ModelForm
from gaegraph.business_base import UpdateNode
from dicionarios_app.model import Dicionarios

class DicionariosPublicForm(ModelForm):
    """
    Form used to show properties on app's home
    """
    _model_class = Dicionarios
    _include = [Dicionarios.Autor, 
                Dicionarios.preco, 
                Dicionarios.edicao, 
                Dicionarios.titulo, 
                Dicionarios.descricao, 
                Dicionarios.editora]


class DicionariosForm(ModelForm):
    """
    Form used to save and update operations on app's admin page
    """
    _model_class = Dicionarios
    _include = [Dicionarios.Autor, 
                Dicionarios.preco, 
                Dicionarios.edicao, 
                Dicionarios.titulo, 
                Dicionarios.descricao, 
                Dicionarios.editora]


class DicionariosDetailForm(ModelForm):
    """
    Form used to show entity details on app's admin page
    """
    _model_class = Dicionarios
    _include = [Dicionarios.creation, 
                Dicionarios.Autor, 
                Dicionarios.preco, 
                Dicionarios.titulo, 
                Dicionarios.edicao, 
                Dicionarios.descricao, 
                Dicionarios.editora]


class DicionariosShortForm(ModelForm):
    """
    Form used to show entity short version on app's admin page, mainly for tables
    """
    _model_class = Dicionarios
    _include = [Dicionarios.creation, 
                Dicionarios.Autor, 
                Dicionarios.preco, 
                Dicionarios.titulo, 
                Dicionarios.edicao, 
                Dicionarios.descricao, 
                Dicionarios.editora]


class SaveDicionariosCommand(SaveCommand):
    _model_form_class = DicionariosForm


class UpdateDicionariosCommand(UpdateNode):
    _model_form_class = DicionariosForm


class ListDicionariosCommand(ModelSearchCommand):
    def __init__(self):
        super(ListDicionariosCommand, self).__init__(Dicionarios.query_by_creation())

