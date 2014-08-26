# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaegraph.business_base import NodeSearch, DeleteNode
from aventura_app.commands import ListAvenuraCommand, SaveAvenuraCommand, UpdateAvenuraCommand, \
    AvenuraPublicForm, AvenuraDetailForm, AvenuraShortForm


def save_avenura_cmd(**avenura_properties):
    """
    Command to save Avenura entity
    :param avenura_properties: a dict of properties to save on model
    :return: a Command that save Avenura, validating and localizing properties received as strings
    """
    return SaveAvenuraCommand(**avenura_properties)


def update_avenura_cmd(avenura_id, **avenura_properties):
    """
    Command to update Avenura entity with id equals 'avenura_id'
    :param avenura_properties: a dict of properties to update model
    :return: a Command that update Avenura, validating and localizing properties received as strings
    """
    return UpdateAvenuraCommand(avenura_id, **avenura_properties)


def list_avenuras_cmd():
    """
    Command to list Avenura entities ordered by their creation dates
    :return: a Command proceed the db operations when executed
    """
    return ListAvenuraCommand()


def avenura_detail_form(**kwargs):
    """
    Function to get Avenura's detail form.
    :param kwargs: form properties
    :return: Form
    """
    return AvenuraDetailForm(**kwargs)


def avenura_short_form(**kwargs):
    """
    Function to get Avenura's short form. just a subset of avenura's properties
    :param kwargs: form properties
    :return: Form
    """
    return AvenuraShortForm(**kwargs)

def avenura_public_form(**kwargs):
    """
    Function to get Avenura'spublic form. just a subset of avenura's properties
    :param kwargs: form properties
    :return: Form
    """
    return AvenuraPublicForm(**kwargs)


def get_avenura_cmd(avenura_id):
    """
    Find avenura by her id
    :param avenura_id: the avenura id
    :return: Command
    """
    return NodeSearch(avenura_id)


def delete_avenura_cmd(avenura_id):
    """
    Construct a command to delete a Avenura
    :param avenura_id: avenura's id
    :return: Command
    """
    return DeleteNode(avenura_id)

