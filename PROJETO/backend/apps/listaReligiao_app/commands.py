# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaebusiness.gaeutil import SaveCommand, ModelSearchCommand
from gaeforms.ndb.form import ModelForm
from gaegraph.business_base import UpdateNode
from listaReligiao_app.model import ListaReligiao

class ListaReligiaoPublicForm(ModelForm):
    """
    Form used to show properties on app's home
    """
    _model_class = ListaReligiao
    _include = [ListaReligiao.autor, 
                ListaReligiao.preco, 
                ListaReligiao.edicao, 
                ListaReligiao.titulo, 
                ListaReligiao.descricao, 
                ListaReligiao.editora]


class ListaReligiaoForm(ModelForm):
    """
    Form used to save and update operations on app's admin page
    """
    _model_class = ListaReligiao
    _include = [ListaReligiao.autor, 
                ListaReligiao.preco, 
                ListaReligiao.edicao, 
                ListaReligiao.titulo, 
                ListaReligiao.descricao, 
                ListaReligiao.editora]


class ListaReligiaoDetailForm(ModelForm):
    """
    Form used to show entity details on app's admin page
    """
    _model_class = ListaReligiao
    _include = [ListaReligiao.creation, 
                ListaReligiao.autor, 
                ListaReligiao.preco, 
                ListaReligiao.titulo, 
                ListaReligiao.edicao, 
                ListaReligiao.descricao, 
                ListaReligiao.editora]


class ListaReligiaoShortForm(ModelForm):
    """
    Form used to show entity short version on app's admin page, mainly for tables
    """
    _model_class = ListaReligiao
    _include = [ListaReligiao.creation, 
                ListaReligiao.autor, 
                ListaReligiao.preco, 
                ListaReligiao.titulo, 
                ListaReligiao.edicao, 
                ListaReligiao.descricao, 
                ListaReligiao.editora]


class SaveListaReligiaoCommand(SaveCommand):
    _model_form_class = ListaReligiaoForm


class UpdateListaReligiaoCommand(UpdateNode):
    _model_form_class = ListaReligiaoForm


class ListListaReligiaoCommand(ModelSearchCommand):
    def __init__(self):
        super(ListListaReligiaoCommand, self).__init__(ListaReligiao.query_by_creation())

