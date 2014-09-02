# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaebusiness.gaeutil import SaveCommand, ModelSearchCommand
from gaeforms.ndb.form import ModelForm
from gaegraph.business_base import UpdateNode
from religiao_app.model import Religiao

class ReligiaoPublicForm(ModelForm):
    """
    Form used to show properties on app's home
    """
    _model_class = Religiao
    _include = [Religiao.Autor, 
                Religiao.preco, 
                Religiao.edicao, 
                Religiao.titulo, 
                Religiao.descricao, 
                Religiao.editora]


class ReligiaoForm(ModelForm):
    """
    Form used to save and update operations on app's admin page
    """
    _model_class = Religiao
    _include = [Religiao.Autor, 
                Religiao.preco, 
                Religiao.edicao, 
                Religiao.titulo, 
                Religiao.descricao, 
                Religiao.editora]


class ReligiaoDetailForm(ModelForm):
    """
    Form used to show entity details on app's admin page
    """
    _model_class = Religiao
    _include = [Religiao.creation, 
                Religiao.Autor, 
                Religiao.preco, 
                Religiao.titulo, 
                Religiao.edicao, 
                Religiao.descricao, 
                Religiao.editora]


class ReligiaoShortForm(ModelForm):
    """
    Form used to show entity short version on app's admin page, mainly for tables
    """
    _model_class = Religiao
    _include = [Religiao.creation, 
                Religiao.Autor, 
                Religiao.preco, 
                Religiao.titulo, 
                Religiao.edicao, 
                Religiao.descricao, 
                Religiao.editora]


class SaveReligiaoCommand(SaveCommand):
    _model_form_class = ReligiaoForm


class UpdateReligiaoCommand(UpdateNode):
    _model_form_class = ReligiaoForm


class ListReligiaoCommand(ModelSearchCommand):
    def __init__(self):
        super(ListReligiaoCommand, self).__init__(Religiao.query_by_creation())

