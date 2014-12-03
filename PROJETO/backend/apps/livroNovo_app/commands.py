# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaebusiness.gaeutil import SaveCommand, ModelSearchCommand
from gaeforms.ndb.form import ModelForm
from gaegraph.business_base import UpdateNode
from livroNovo_app.model import LivroNovo

class LivroNovoPublicForm(ModelForm):
    """
    Form used to show properties on app's home
    """
    _model_class = LivroNovo
    _include = [LivroNovo.autor, 
                LivroNovo.titulo, 
                LivroNovo.preco]


class LivroNovoForm(ModelForm):
    """
    Form used to save and update operations on app's admin page
    """
    _model_class = LivroNovo
    _include = [LivroNovo.autor, 
                LivroNovo.titulo, 
                LivroNovo.preco]


class LivroNovoDetailForm(ModelForm):
    """
    Form used to show entity details on app's admin page
    """
    _model_class = LivroNovo
    _include = [LivroNovo.autor, 
                LivroNovo.titulo, 
                LivroNovo.creation, 
                LivroNovo.preco]


class LivroNovoShortForm(ModelForm):
    """
    Form used to show entity short version on app's admin page, mainly for tables
    """
    _model_class = LivroNovo
    _include = [LivroNovo.autor, 
                LivroNovo.titulo, 
                LivroNovo.creation, 
                LivroNovo.preco]


class SaveLivroNovoCommand(SaveCommand):
    _model_form_class = LivroNovoForm


class UpdateLivroNovoCommand(UpdateNode):
    _model_form_class = LivroNovoForm


class ListLivroNovoCommand(ModelSearchCommand):
    def __init__(self):
        super(ListLivroNovoCommand, self).__init__(LivroNovo.query_by_creation())

