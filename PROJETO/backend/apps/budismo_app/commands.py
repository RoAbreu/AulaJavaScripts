# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaebusiness.gaeutil import SaveCommand, ModelSearchCommand
from gaeforms.ndb.form import ModelForm
from gaegraph.business_base import UpdateNode
from budismo_app.model import Budismo

class BudismoPublicForm(ModelForm):
    """
    Form used to show properties on app's home
    """
    _model_class = Budismo
    _include = [Budismo.autor, 
                Budismo.preco, 
                Budismo.edicao, 
                Budismo.titulo, 
                Budismo.descricao, 
                Budismo.editora]


class BudismoForm(ModelForm):
    """
    Form used to save and update operations on app's admin page
    """
    _model_class = Budismo
    _include = [Budismo.autor, 
                Budismo.preco, 
                Budismo.edicao, 
                Budismo.titulo, 
                Budismo.descricao, 
                Budismo.editora]


class BudismoDetailForm(ModelForm):
    """
    Form used to show entity details on app's admin page
    """
    _model_class = Budismo
    _include = [Budismo.creation, 
                Budismo.autor, 
                Budismo.preco, 
                Budismo.titulo, 
                Budismo.edicao, 
                Budismo.descricao, 
                Budismo.editora]


class BudismoShortForm(ModelForm):
    """
    Form used to show entity short version on app's admin page, mainly for tables
    """
    _model_class = Budismo
    _include = [Budismo.creation, 
                Budismo.autor, 
                Budismo.preco, 
                Budismo.titulo, 
                Budismo.edicao, 
                Budismo.descricao, 
                Budismo.editora]


class SaveBudismoCommand(SaveCommand):
    _model_form_class = BudismoForm


class UpdateBudismoCommand(UpdateNode):
    _model_form_class = BudismoForm


class ListBudismoCommand(ModelSearchCommand):
    def __init__(self):
        super(ListBudismoCommand, self).__init__(Budismo.query_by_creation())

