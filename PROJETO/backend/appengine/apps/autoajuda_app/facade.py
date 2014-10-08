# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaegraph.business_base import NodeSearch, DeleteNode
from autoajuda_app.commands import ListAutoajudaCommand, SaveAutoajudaCommand, UpdateAutoajudaCommand, \
    AutoajudaPublicForm, AutoajudaDetailForm, AutoajudaShortForm


def save_autoajuda_cmd(**autoajuda_properties):
    """
    Command to save Autoajuda entity
    :param autoajuda_properties: a dict of properties to save on model
    :return: a Command that save Autoajuda, validating and localizing properties received as strings
    """
    return SaveAutoajudaCommand(**autoajuda_properties)


def update_autoajuda_cmd(autoajuda_id, **autoajuda_properties):
    """
    Command to update Autoajuda entity with id equals 'autoajuda_id'
    :param autoajuda_properties: a dict of properties to update model
    :return: a Command that update Autoajuda, validating and localizing properties received as strings
    """
    return UpdateAutoajudaCommand(autoajuda_id, **autoajuda_properties)


def list_autoajudas_cmd():
    """
    Command to list Autoajuda entities ordered by their creation dates
    :return: a Command proceed the db operations when executed
    """
    return ListAutoajudaCommand()


def autoajuda_detail_form(**kwargs):
    """
    Function to get Autoajuda's detail form.
    :param kwargs: form properties
    :return: Form
    """
    return AutoajudaDetailForm(**kwargs)


def autoajuda_short_form(**kwargs):
    """
    Function to get Autoajuda's short form. just a subset of autoajuda's properties
    :param kwargs: form properties
    :return: Form
    """
    return AutoajudaShortForm(**kwargs)

def autoajuda_public_form(**kwargs):
    """
    Function to get Autoajuda'spublic form. just a subset of autoajuda's properties
    :param kwargs: form properties
    :return: Form
    """
    return AutoajudaPublicForm(**kwargs)


def get_autoajuda_cmd(autoajuda_id):
    """
    Find autoajuda by her id
    :param autoajuda_id: the autoajuda id
    :return: Command
    """
    return NodeSearch(autoajuda_id)


def delete_autoajuda_cmd(autoajuda_id):
    """
    Construct a command to delete a Autoajuda
    :param autoajuda_id: autoajuda's id
    :return: Command
    """
    return DeleteNode(autoajuda_id)

