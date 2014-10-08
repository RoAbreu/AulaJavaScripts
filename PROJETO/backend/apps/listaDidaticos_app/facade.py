# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaegraph.business_base import NodeSearch, DeleteNode
from listaDidaticos_app.commands import ListListaDidaticosCommand, SaveListaDidaticosCommand, UpdateListaDidaticosCommand, \
    ListaDidaticosPublicForm, ListaDidaticosDetailForm, ListaDidaticosShortForm


def save_lista_didaticos_cmd(**lista_didaticos_properties):
    """
    Command to save ListaDidaticos entity
    :param lista_didaticos_properties: a dict of properties to save on model
    :return: a Command that save ListaDidaticos, validating and localizing properties received as strings
    """
    return SaveListaDidaticosCommand(**lista_didaticos_properties)


def update_lista_didaticos_cmd(lista_didaticos_id, **lista_didaticos_properties):
    """
    Command to update ListaDidaticos entity with id equals 'lista_didaticos_id'
    :param lista_didaticos_properties: a dict of properties to update model
    :return: a Command that update ListaDidaticos, validating and localizing properties received as strings
    """
    return UpdateListaDidaticosCommand(lista_didaticos_id, **lista_didaticos_properties)


def list_lista_didaticoss_cmd():
    """
    Command to list ListaDidaticos entities ordered by their creation dates
    :return: a Command proceed the db operations when executed
    """
    return ListListaDidaticosCommand()


def lista_didaticos_detail_form(**kwargs):
    """
    Function to get ListaDidaticos's detail form.
    :param kwargs: form properties
    :return: Form
    """
    return ListaDidaticosDetailForm(**kwargs)


def lista_didaticos_short_form(**kwargs):
    """
    Function to get ListaDidaticos's short form. just a subset of lista_didaticos's properties
    :param kwargs: form properties
    :return: Form
    """
    return ListaDidaticosShortForm(**kwargs)

def lista_didaticos_public_form(**kwargs):
    """
    Function to get ListaDidaticos'spublic form. just a subset of lista_didaticos's properties
    :param kwargs: form properties
    :return: Form
    """
    return ListaDidaticosPublicForm(**kwargs)


def get_lista_didaticos_cmd(lista_didaticos_id):
    """
    Find lista_didaticos by her id
    :param lista_didaticos_id: the lista_didaticos id
    :return: Command
    """
    return NodeSearch(lista_didaticos_id)


def delete_lista_didaticos_cmd(lista_didaticos_id):
    """
    Construct a command to delete a ListaDidaticos
    :param lista_didaticos_id: lista_didaticos's id
    :return: Command
    """
    return DeleteNode(lista_didaticos_id)

