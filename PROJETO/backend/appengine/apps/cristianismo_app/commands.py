# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaebusiness.gaeutil import SaveCommand, ModelSearchCommand
from gaeforms.ndb.form import ModelForm
from gaegraph.business_base import UpdateNode
from cristianismo_app.model import Cristianismo

class CristianismoPublicForm(ModelForm):
    """
    Form used to show properties on app's home
    """
    _model_class = Cristianismo
    _include = [Cristianismo.autor, 
                Cristianismo.preco, 
                Cristianismo.edicao, 
                Cristianismo.titulo, 
                Cristianismo.descricao, 
                Cristianismo.editora]


class CristianismoForm(ModelForm):
    """
    Form used to save and update operations on app's admin page
    """
    _model_class = Cristianismo
    _include = [Cristianismo.autor, 
                Cristianismo.preco, 
                Cristianismo.edicao, 
                Cristianismo.titulo, 
                Cristianismo.descricao, 
                Cristianismo.editora]


class CristianismoDetailForm(ModelForm):
    """
    Form used to show entity details on app's admin page
    """
    _model_class = Cristianismo
    _include = [Cristianismo.creation, 
                Cristianismo.autor, 
                Cristianismo.preco, 
                Cristianismo.titulo, 
                Cristianismo.edicao, 
                Cristianismo.descricao, 
                Cristianismo.editora]


class CristianismoShortForm(ModelForm):
    """
    Form used to show entity short version on app's admin page, mainly for tables
    """
    _model_class = Cristianismo
    _include = [Cristianismo.creation, 
                Cristianismo.autor, 
                Cristianismo.preco, 
                Cristianismo.titulo, 
                Cristianismo.edicao, 
                Cristianismo.descricao, 
                Cristianismo.editora]


class SaveCristianismoCommand(SaveCommand):
    _model_form_class = CristianismoForm


class UpdateCristianismoCommand(UpdateNode):
    _model_form_class = CristianismoForm


class ListCristianismoCommand(ModelSearchCommand):
    def __init__(self):
        super(ListCristianismoCommand, self).__init__(Cristianismo.query_by_creation())

