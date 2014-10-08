# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaegraph.business_base import NodeSearch, DeleteNode
from listaReligiao_app.commands import ListListaReligiaoCommand, SaveListaReligiaoCommand, UpdateListaReligiaoCommand, \
    ListaReligiaoPublicForm, ListaReligiaoDetailForm, ListaReligiaoShortForm


def save_lista_religiao_cmd(**lista_religiao_properties):
    """
    Command to save ListaReligiao entity
    :param lista_religiao_properties: a dict of properties to save on model
    :return: a Command that save ListaReligiao, validating and localizing properties received as strings
    """
    return SaveListaReligiaoCommand(**lista_religiao_properties)


def update_lista_religiao_cmd(lista_religiao_id, **lista_religiao_properties):
    """
    Command to update ListaReligiao entity with id equals 'lista_religiao_id'
    :param lista_religiao_properties: a dict of properties to update model
    :return: a Command that update ListaReligiao, validating and localizing properties received as strings
    """
    return UpdateListaReligiaoCommand(lista_religiao_id, **lista_religiao_properties)


def list_lista_religiaos_cmd():
    """
    Command to list ListaReligiao entities ordered by their creation dates
    :return: a Command proceed the db operations when executed
    """
    return ListListaReligiaoCommand()


def lista_religiao_detail_form(**kwargs):
    """
    Function to get ListaReligiao's detail form.
    :param kwargs: form properties
    :return: Form
    """
    return ListaReligiaoDetailForm(**kwargs)


def lista_religiao_short_form(**kwargs):
    """
    Function to get ListaReligiao's short form. just a subset of lista_religiao's properties
    :param kwargs: form properties
    :return: Form
    """
    return ListaReligiaoShortForm(**kwargs)

def lista_religiao_public_form(**kwargs):
    """
    Function to get ListaReligiao'spublic form. just a subset of lista_religiao's properties
    :param kwargs: form properties
    :return: Form
    """
    return ListaReligiaoPublicForm(**kwargs)


def get_lista_religiao_cmd(lista_religiao_id):
    """
    Find lista_religiao by her id
    :param lista_religiao_id: the lista_religiao id
    :return: Command
    """
    return NodeSearch(lista_religiao_id)


def delete_lista_religiao_cmd(lista_religiao_id):
    """
    Construct a command to delete a ListaReligiao
    :param lista_religiao_id: lista_religiao's id
    :return: Command
    """
    return DeleteNode(lista_religiao_id)

