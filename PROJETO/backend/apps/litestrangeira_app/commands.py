# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaebusiness.gaeutil import SaveCommand, ModelSearchCommand
from gaeforms.ndb.form import ModelForm
from gaegraph.business_base import UpdateNode
from litestrangeira_app.model import Litestrangeira

class LitestrangeiraPublicForm(ModelForm):
    """
    Form used to show properties on app's home
    """
    _model_class = Litestrangeira
    _include = [Litestrangeira.Autor, 
                Litestrangeira.preco, 
                Litestrangeira.edicao, 
                Litestrangeira.titulo, 
                Litestrangeira.descricao, 
                Litestrangeira.editora]


class LitestrangeiraForm(ModelForm):
    """
    Form used to save and update operations on app's admin page
    """
    _model_class = Litestrangeira
    _include = [Litestrangeira.Autor, 
                Litestrangeira.preco, 
                Litestrangeira.edicao, 
                Litestrangeira.titulo, 
                Litestrangeira.descricao, 
                Litestrangeira.editora]


class LitestrangeiraDetailForm(ModelForm):
    """
    Form used to show entity details on app's admin page
    """
    _model_class = Litestrangeira
    _include = [Litestrangeira.creation, 
                Litestrangeira.Autor, 
                Litestrangeira.preco, 
                Litestrangeira.titulo, 
                Litestrangeira.edicao, 
                Litestrangeira.descricao, 
                Litestrangeira.editora]


class LitestrangeiraShortForm(ModelForm):
    """
    Form used to show entity short version on app's admin page, mainly for tables
    """
    _model_class = Litestrangeira
    _include = [Litestrangeira.creation, 
                Litestrangeira.Autor, 
                Litestrangeira.preco, 
                Litestrangeira.titulo, 
                Litestrangeira.edicao, 
                Litestrangeira.descricao, 
                Litestrangeira.editora]


class SaveLitestrangeiraCommand(SaveCommand):
    _model_form_class = LitestrangeiraForm


class UpdateLitestrangeiraCommand(UpdateNode):
    _model_form_class = LitestrangeiraForm


class ListLitestrangeiraCommand(ModelSearchCommand):
    def __init__(self):
        super(ListLitestrangeiraCommand, self).__init__(Litestrangeira.query_by_creation())

