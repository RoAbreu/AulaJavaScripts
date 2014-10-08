# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaebusiness.gaeutil import SaveCommand, ModelSearchCommand
from gaeforms.ndb.form import ModelForm
from gaegraph.business_base import UpdateNode
from biblias_app.model import Biblias

class BibliasPublicForm(ModelForm):
    """
    Form used to show properties on app's home
    """
    _model_class = Biblias
    _include = [Biblias.autor, 
                Biblias.preco, 
                Biblias.edicao, 
                Biblias.titulo, 
                Biblias.descricao, 
                Biblias.editora]


class BibliasForm(ModelForm):
    """
    Form used to save and update operations on app's admin page
    """
    _model_class = Biblias
    _include = [Biblias.autor, 
                Biblias.preco, 
                Biblias.edicao, 
                Biblias.titulo, 
                Biblias.descricao, 
                Biblias.editora]


class BibliasDetailForm(ModelForm):
    """
    Form used to show entity details on app's admin page
    """
    _model_class = Biblias
    _include = [Biblias.creation, 
                Biblias.autor, 
                Biblias.preco, 
                Biblias.titulo, 
                Biblias.edicao, 
                Biblias.descricao, 
                Biblias.editora]


class BibliasShortForm(ModelForm):
    """
    Form used to show entity short version on app's admin page, mainly for tables
    """
    _model_class = Biblias
    _include = [Biblias.creation, 
                Biblias.autor, 
                Biblias.preco, 
                Biblias.titulo, 
                Biblias.edicao, 
                Biblias.descricao, 
                Biblias.editora]


class SaveBibliasCommand(SaveCommand):
    _model_form_class = BibliasForm


class UpdateBibliasCommand(UpdateNode):
    _model_form_class = BibliasForm


class ListBibliasCommand(ModelSearchCommand):
    def __init__(self):
        super(ListBibliasCommand, self).__init__(Biblias.query_by_creation())

