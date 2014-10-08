# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaegraph.business_base import NodeSearch, DeleteNode
from listaDicionarios_app.commands import ListListaDicionariosCommand, SaveListaDicionariosCommand, UpdateListaDicionariosCommand, \
    ListaDicionariosPublicForm, ListaDicionariosDetailForm, ListaDicionariosShortForm


def save_lista_dicionarios_cmd(**lista_dicionarios_properties):
    """
    Command to save ListaDicionarios entity
    :param lista_dicionarios_properties: a dict of properties to save on model
    :return: a Command that save ListaDicionarios, validating and localizing properties received as strings
    """
    return SaveListaDicionariosCommand(**lista_dicionarios_properties)


def update_lista_dicionarios_cmd(lista_dicionarios_id, **lista_dicionarios_properties):
    """
    Command to update ListaDicionarios entity with id equals 'lista_dicionarios_id'
    :param lista_dicionarios_properties: a dict of properties to update model
    :return: a Command that update ListaDicionarios, validating and localizing properties received as strings
    """
    return UpdateListaDicionariosCommand(lista_dicionarios_id, **lista_dicionarios_properties)


def list_lista_dicionarioss_cmd():
    """
    Command to list ListaDicionarios entities ordered by their creation dates
    :return: a Command proceed the db operations when executed
    """
    return ListListaDicionariosCommand()


def lista_dicionarios_detail_form(**kwargs):
    """
    Function to get ListaDicionarios's detail form.
    :param kwargs: form properties
    :return: Form
    """
    return ListaDicionariosDetailForm(**kwargs)


def lista_dicionarios_short_form(**kwargs):
    """
    Function to get ListaDicionarios's short form. just a subset of lista_dicionarios's properties
    :param kwargs: form properties
    :return: Form
    """
    return ListaDicionariosShortForm(**kwargs)

def lista_dicionarios_public_form(**kwargs):
    """
    Function to get ListaDicionarios'spublic form. just a subset of lista_dicionarios's properties
    :param kwargs: form properties
    :return: Form
    """
    return ListaDicionariosPublicForm(**kwargs)


def get_lista_dicionarios_cmd(lista_dicionarios_id):
    """
    Find lista_dicionarios by her id
    :param lista_dicionarios_id: the lista_dicionarios id
    :return: Command
    """
    return NodeSearch(lista_dicionarios_id)


def delete_lista_dicionarios_cmd(lista_dicionarios_id):
    """
    Construct a command to delete a ListaDicionarios
    :param lista_dicionarios_id: lista_dicionarios's id
    :return: Command
    """
    return DeleteNode(lista_dicionarios_id)

