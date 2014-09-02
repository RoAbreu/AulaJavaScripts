# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaebusiness.gaeutil import SaveCommand, ModelSearchCommand
from gaeforms.ndb.form import ModelForm
from gaegraph.business_base import UpdateNode
from litinfantojuv_app.model import Litinfantojuv

class LitinfantojuvPublicForm(ModelForm):
    """
    Form used to show properties on app's home
    """
    _model_class = Litinfantojuv
    _include = [Litinfantojuv.Autor, 
                Litinfantojuv.preco, 
                Litinfantojuv.edicao, 
                Litinfantojuv.titulo, 
                Litinfantojuv.descricao, 
                Litinfantojuv.editora]


class LitinfantojuvForm(ModelForm):
    """
    Form used to save and update operations on app's admin page
    """
    _model_class = Litinfantojuv
    _include = [Litinfantojuv.Autor, 
                Litinfantojuv.preco, 
                Litinfantojuv.edicao, 
                Litinfantojuv.titulo, 
                Litinfantojuv.descricao, 
                Litinfantojuv.editora]


class LitinfantojuvDetailForm(ModelForm):
    """
    Form used to show entity details on app's admin page
    """
    _model_class = Litinfantojuv
    _include = [Litinfantojuv.creation, 
                Litinfantojuv.Autor, 
                Litinfantojuv.preco, 
                Litinfantojuv.titulo, 
                Litinfantojuv.edicao, 
                Litinfantojuv.descricao, 
                Litinfantojuv.editora]


class LitinfantojuvShortForm(ModelForm):
    """
    Form used to show entity short version on app's admin page, mainly for tables
    """
    _model_class = Litinfantojuv
    _include = [Litinfantojuv.creation, 
                Litinfantojuv.Autor, 
                Litinfantojuv.preco, 
                Litinfantojuv.titulo, 
                Litinfantojuv.edicao, 
                Litinfantojuv.descricao, 
                Litinfantojuv.editora]


class SaveLitinfantojuvCommand(SaveCommand):
    _model_form_class = LitinfantojuvForm


class UpdateLitinfantojuvCommand(UpdateNode):
    _model_form_class = LitinfantojuvForm


class ListLitinfantojuvCommand(ModelSearchCommand):
    def __init__(self):
        super(ListLitinfantojuvCommand, self).__init__(Litinfantojuv.query_by_creation())

