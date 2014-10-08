# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaegraph.business_base import NodeSearch, DeleteNode
from dicionarios_app.commands import ListDicionariosCommand, SaveDicionariosCommand, UpdateDicionariosCommand, \
    DicionariosPublicForm, DicionariosDetailForm, DicionariosShortForm


def save_dicionarios_cmd(**dicionarios_properties):
    """
    Command to save Dicionarios entity
    :param dicionarios_properties: a dict of properties to save on model
    :return: a Command that save Dicionarios, validating and localizing properties received as strings
    """
    return SaveDicionariosCommand(**dicionarios_properties)


def update_dicionarios_cmd(dicionarios_id, **dicionarios_properties):
    """
    Command to update Dicionarios entity with id equals 'dicionarios_id'
    :param dicionarios_properties: a dict of properties to update model
    :return: a Command that update Dicionarios, validating and localizing properties received as strings
    """
    return UpdateDicionariosCommand(dicionarios_id, **dicionarios_properties)


def list_dicionarioss_cmd():
    """
    Command to list Dicionarios entities ordered by their creation dates
    :return: a Command proceed the db operations when executed
    """
    return ListDicionariosCommand()


def dicionarios_detail_form(**kwargs):
    """
    Function to get Dicionarios's detail form.
    :param kwargs: form properties
    :return: Form
    """
    return DicionariosDetailForm(**kwargs)


def dicionarios_short_form(**kwargs):
    """
    Function to get Dicionarios's short form. just a subset of dicionarios's properties
    :param kwargs: form properties
    :return: Form
    """
    return DicionariosShortForm(**kwargs)

def dicionarios_public_form(**kwargs):
    """
    Function to get Dicionarios'spublic form. just a subset of dicionarios's properties
    :param kwargs: form properties
    :return: Form
    """
    return DicionariosPublicForm(**kwargs)


def get_dicionarios_cmd(dicionarios_id):
    """
    Find dicionarios by her id
    :param dicionarios_id: the dicionarios id
    :return: Command
    """
    return NodeSearch(dicionarios_id)


def delete_dicionarios_cmd(dicionarios_id):
    """
    Construct a command to delete a Dicionarios
    :param dicionarios_id: dicionarios's id
    :return: Command
    """
    return DeleteNode(dicionarios_id)

