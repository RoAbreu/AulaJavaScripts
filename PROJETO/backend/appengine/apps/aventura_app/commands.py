# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaebusiness.gaeutil import SaveCommand, ModelSearchCommand
from gaeforms.ndb.form import ModelForm
from gaegraph.business_base import UpdateNode
from aventura_app.model import Avenura

class AvenuraPublicForm(ModelForm):
    """
    Form used to show properties on app's home
    """
    _model_class = Avenura
    _include = [Avenura.Autor, 
                Avenura.Preco, 
                Avenura.Titulo, 
                Avenura.Edicao, 
                Avenura.Descricao, 
                Avenura.Editora]


class AvenuraForm(ModelForm):
    """
    Form used to save and update operations on app's admin page
    """
    _model_class = Avenura
    _include = [Avenura.Autor, 
                Avenura.Preco, 
                Avenura.Titulo, 
                Avenura.Edicao, 
                Avenura.Descricao, 
                Avenura.Editora]


class AvenuraDetailForm(ModelForm):
    """
    Form used to show entity details on app's admin page
    """
    _model_class = Avenura
    _include = [Avenura.creation, 
                Avenura.Autor, 
                Avenura.Preco, 
                Avenura.Edicao, 
                Avenura.Titulo, 
                Avenura.Descricao, 
                Avenura.Editora]


class AvenuraShortForm(ModelForm):
    """
    Form used to show entity short version on app's admin page, mainly for tables
    """
    _model_class = Avenura
    _include = [Avenura.creation, 
                Avenura.Autor, 
                Avenura.Preco, 
                Avenura.Edicao, 
                Avenura.Titulo, 
                Avenura.Descricao, 
                Avenura.Editora]


class SaveAvenuraCommand(SaveCommand):
    _model_form_class = AvenuraForm


class UpdateAvenuraCommand(UpdateNode):
    _model_form_class = AvenuraForm


class ListAvenuraCommand(ModelSearchCommand):
    def __init__(self):
        super(ListAvenuraCommand, self).__init__(Avenura.query_by_creation())

