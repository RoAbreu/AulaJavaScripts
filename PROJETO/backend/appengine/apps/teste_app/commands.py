# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaebusiness.gaeutil import SaveCommand, ModelSearchCommand
from gaeforms.ndb.form import ModelForm
from gaegraph.business_base import UpdateNode
from teste_app.model import Teste

class TestePublicForm(ModelForm):
    """
    Form used to show properties on app's home
    """
    _model_class = Teste
    _include = [Teste.autor, 
                Teste.preco, 
                Teste.edicao, 
                Teste.titulo, 
                Teste.descricao, 
                Teste.editora]


class TesteForm(ModelForm):
    """
    Form used to save and update operations on app's admin page
    """
    _model_class = Teste
    _include = [Teste.autor, 
                Teste.preco, 
                Teste.edicao, 
                Teste.titulo, 
                Teste.descricao, 
                Teste.editora]


class TesteDetailForm(ModelForm):
    """
    Form used to show entity details on app's admin page
    """
    _model_class = Teste
    _include = [Teste.creation, 
                Teste.autor, 
                Teste.preco, 
                Teste.titulo, 
                Teste.edicao, 
                Teste.descricao, 
                Teste.editora]


class TesteShortForm(ModelForm):
    """
    Form used to show entity short version on app's admin page, mainly for tables
    """
    _model_class = Teste
    _include = [Teste.creation, 
                Teste.autor, 
                Teste.preco, 
                Teste.titulo, 
                Teste.edicao, 
                Teste.descricao, 
                Teste.editora]


class SaveTesteCommand(SaveCommand):
    _model_form_class = TesteForm


class UpdateTesteCommand(UpdateNode):
    _model_form_class = TesteForm


class ListTesteCommand(ModelSearchCommand):
    def __init__(self):
        super(ListTesteCommand, self).__init__(Teste.query_by_creation())

