# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaegraph.business_base import NodeSearch, DeleteNode
from teste_app.commands import ListTesteCommand, SaveTesteCommand, UpdateTesteCommand, \
    TestePublicForm, TesteDetailForm, TesteShortForm


def save_teste_cmd(**teste_properties):
    """
    Command to save Teste entity
    :param teste_properties: a dict of properties to save on model
    :return: a Command that save Teste, validating and localizing properties received as strings
    """
    return SaveTesteCommand(**teste_properties)


def update_teste_cmd(teste_id, **teste_properties):
    """
    Command to update Teste entity with id equals 'teste_id'
    :param teste_properties: a dict of properties to update model
    :return: a Command that update Teste, validating and localizing properties received as strings
    """
    return UpdateTesteCommand(teste_id, **teste_properties)


def list_testes_cmd():
    """
    Command to list Teste entities ordered by their creation dates
    :return: a Command proceed the db operations when executed
    """
    return ListTesteCommand()


def teste_detail_form(**kwargs):
    """
    Function to get Teste's detail form.
    :param kwargs: form properties
    :return: Form
    """
    return TesteDetailForm(**kwargs)


def teste_short_form(**kwargs):
    """
    Function to get Teste's short form. just a subset of teste's properties
    :param kwargs: form properties
    :return: Form
    """
    return TesteShortForm(**kwargs)

def teste_public_form(**kwargs):
    """
    Function to get Teste'spublic form. just a subset of teste's properties
    :param kwargs: form properties
    :return: Form
    """
    return TestePublicForm(**kwargs)


def get_teste_cmd(teste_id):
    """
    Find teste by her id
    :param teste_id: the teste id
    :return: Command
    """
    return NodeSearch(teste_id)


def delete_teste_cmd(teste_id):
    """
    Construct a command to delete a Teste
    :param teste_id: teste's id
    :return: Command
    """
    return DeleteNode(teste_id)

