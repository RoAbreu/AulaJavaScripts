# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaebusiness.gaeutil import SaveCommand, ModelSearchCommand
from gaeforms.ndb.form import ModelForm
from gaegraph.business_base import UpdateNode
from litnacional_app.model import Litnacional

class LitnacionalPublicForm(ModelForm):
    """
    Form used to show properties on app's home
    """
    _model_class = Litnacional
    _include = [Litnacional.autor, 
                Litnacional.preco, 
                Litnacional.edicao, 
                Litnacional.titulo, 
                Litnacional.descricao, 
                Litnacional.editora]


class LitnacionalForm(ModelForm):
    """
    Form used to save and update operations on app's admin page
    """
    _model_class = Litnacional
    _include = [Litnacional.autor, 
                Litnacional.preco, 
                Litnacional.edicao, 
                Litnacional.titulo, 
                Litnacional.descricao, 
                Litnacional.editora]


class LitnacionalDetailForm(ModelForm):
    """
    Form used to show entity details on app's admin page
    """
    _model_class = Litnacional
    _include = [Litnacional.creation, 
                Litnacional.autor, 
                Litnacional.preco, 
                Litnacional.titulo, 
                Litnacional.edicao, 
                Litnacional.descricao, 
                Litnacional.editora]


class LitnacionalShortForm(ModelForm):
    """
    Form used to show entity short version on app's admin page, mainly for tables
    """
    _model_class = Litnacional
    _include = [Litnacional.creation, 
                Litnacional.autor, 
                Litnacional.preco, 
                Litnacional.titulo, 
                Litnacional.edicao, 
                Litnacional.descricao, 
                Litnacional.editora]


class SaveLitnacionalCommand(SaveCommand):
    _model_form_class = LitnacionalForm


class UpdateLitnacionalCommand(UpdateNode):
    _model_form_class = LitnacionalForm


class ListLitnacionalCommand(ModelSearchCommand):
    def __init__(self):
        super(ListLitnacionalCommand, self).__init__(Litnacional.query_by_creation())

