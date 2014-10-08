# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaebusiness.gaeutil import SaveCommand, ModelSearchCommand
from gaeforms.ndb.form import ModelForm
from gaegraph.business_base import UpdateNode
from autoajuda_app.model import Autoajuda

class AutoajudaPublicForm(ModelForm):
    """
    Form used to show properties on app's home
    """
    _model_class = Autoajuda
    _include = [Autoajuda.Autor, 
                Autoajuda.preco, 
                Autoajuda.edicao, 
                Autoajuda.titulo, 
                Autoajuda.descricao, 
                Autoajuda.editora]


class AutoajudaForm(ModelForm):
    """
    Form used to save and update operations on app's admin page
    """
    _model_class = Autoajuda
    _include = [Autoajuda.Autor, 
                Autoajuda.preco, 
                Autoajuda.edicao, 
                Autoajuda.titulo, 
                Autoajuda.descricao, 
                Autoajuda.editora]


class AutoajudaDetailForm(ModelForm):
    """
    Form used to show entity details on app's admin page
    """
    _model_class = Autoajuda
    _include = [Autoajuda.creation, 
                Autoajuda.Autor, 
                Autoajuda.preco, 
                Autoajuda.titulo, 
                Autoajuda.edicao, 
                Autoajuda.descricao, 
                Autoajuda.editora]


class AutoajudaShortForm(ModelForm):
    """
    Form used to show entity short version on app's admin page, mainly for tables
    """
    _model_class = Autoajuda
    _include = [Autoajuda.creation, 
                Autoajuda.Autor, 
                Autoajuda.preco, 
                Autoajuda.titulo, 
                Autoajuda.edicao, 
                Autoajuda.descricao, 
                Autoajuda.editora]


class SaveAutoajudaCommand(SaveCommand):
    _model_form_class = AutoajudaForm


class UpdateAutoajudaCommand(UpdateNode):
    _model_form_class = AutoajudaForm


class ListAutoajudaCommand(ModelSearchCommand):
    def __init__(self):
        super(ListAutoajudaCommand, self).__init__(Autoajuda.query_by_creation())

