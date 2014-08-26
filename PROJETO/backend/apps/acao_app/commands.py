# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaebusiness.gaeutil import SaveCommand, ModelSearchCommand
from gaeforms.ndb.form import ModelForm
from gaegraph.business_base import UpdateNode
from acao_app.model import Acao

class AcaoPublicForm(ModelForm):
    """
    Form used to show properties on app's home
    """
    _model_class = Acao
    _include = [Acao.Autor, 
                Acao.Preco, 
                Acao.Titulo, 
                Acao.Edicao, 
                Acao.Descricao, 
                Acao.Editora]


class AcaoForm(ModelForm):
    """
    Form used to save and update operations on app's admin page
    """
    _model_class = Acao
    _include = [Acao.Autor, 
                Acao.Preco, 
                Acao.Titulo, 
                Acao.Edicao, 
                Acao.Descricao, 
                Acao.Editora]


class AcaoDetailForm(ModelForm):
    """
    Form used to show entity details on app's admin page
    """
    _model_class = Acao
    _include = [Acao.creation, 
                Acao.Autor, 
                Acao.Preco, 
                Acao.Edicao, 
                Acao.Titulo, 
                Acao.Descricao, 
                Acao.Editora]


class AcaoShortForm(ModelForm):
    """
    Form used to show entity short version on app's admin page, mainly for tables
    """
    _model_class = Acao
    _include = [Acao.creation, 
                Acao.Autor, 
                Acao.Preco, 
                Acao.Edicao, 
                Acao.Titulo, 
                Acao.Descricao, 
                Acao.Editora]


class SaveAcaoCommand(SaveCommand):
    _model_form_class = AcaoForm


class UpdateAcaoCommand(UpdateNode):
    _model_form_class = AcaoForm


class ListAcaoCommand(ModelSearchCommand):
    def __init__(self):
        super(ListAcaoCommand, self).__init__(Acao.query_by_creation())

