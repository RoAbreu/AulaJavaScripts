# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaebusiness.gaeutil import SaveCommand, ModelSearchCommand
from gaeforms.ndb.form import ModelForm
from gaegraph.business_base import UpdateNode
from livro_app.model import Livro

class LivroPublicForm(ModelForm):
    """
    Form used to show properties on app's home
    """
    _model_class = Livro
    _include = [Livro.autor, 
                Livro.titulo, 
                Livro.preco]


class LivroForm(ModelForm):
    """
    Form used to save and update operations on app's admin page
    """
    _model_class = Livro
    _include = [Livro.autor, 
                Livro.titulo, 
                Livro.preco]


class LivroDetailForm(ModelForm):
    """
    Form used to show entity details on app's admin page
    """
    _model_class = Livro
    _include = [Livro.autor, 
                Livro.titulo, 
                Livro.creation, 
                Livro.preco]


class LivroShortForm(ModelForm):
    """
    Form used to show entity short version on app's admin page, mainly for tables
    """
    _model_class = Livro
    _include = [Livro.autor, 
                Livro.titulo, 
                Livro.creation, 
                Livro.preco]


class SaveLivroCommand(SaveCommand):
    _model_form_class = LivroForm


class UpdateLivroCommand(UpdateNode):
    _model_form_class = LivroForm


class ListLivroCommand(ModelSearchCommand):
    def __init__(self):
        super(ListLivroCommand, self).__init__(Livro.query_by_creation())

