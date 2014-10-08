# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaegraph.business_base import NodeSearch, DeleteNode
from litinfantojuv_app.commands import ListLitinfantojuvCommand, SaveLitinfantojuvCommand, UpdateLitinfantojuvCommand, \
    LitinfantojuvPublicForm, LitinfantojuvDetailForm, LitinfantojuvShortForm


def save_litinfantojuv_cmd(**litinfantojuv_properties):
    """
    Command to save Litinfantojuv entity
    :param litinfantojuv_properties: a dict of properties to save on model
    :return: a Command that save Litinfantojuv, validating and localizing properties received as strings
    """
    return SaveLitinfantojuvCommand(**litinfantojuv_properties)


def update_litinfantojuv_cmd(litinfantojuv_id, **litinfantojuv_properties):
    """
    Command to update Litinfantojuv entity with id equals 'litinfantojuv_id'
    :param litinfantojuv_properties: a dict of properties to update model
    :return: a Command that update Litinfantojuv, validating and localizing properties received as strings
    """
    return UpdateLitinfantojuvCommand(litinfantojuv_id, **litinfantojuv_properties)


def list_litinfantojuvs_cmd():
    """
    Command to list Litinfantojuv entities ordered by their creation dates
    :return: a Command proceed the db operations when executed
    """
    return ListLitinfantojuvCommand()


def litinfantojuv_detail_form(**kwargs):
    """
    Function to get Litinfantojuv's detail form.
    :param kwargs: form properties
    :return: Form
    """
    return LitinfantojuvDetailForm(**kwargs)


def litinfantojuv_short_form(**kwargs):
    """
    Function to get Litinfantojuv's short form. just a subset of litinfantojuv's properties
    :param kwargs: form properties
    :return: Form
    """
    return LitinfantojuvShortForm(**kwargs)

def litinfantojuv_public_form(**kwargs):
    """
    Function to get Litinfantojuv'spublic form. just a subset of litinfantojuv's properties
    :param kwargs: form properties
    :return: Form
    """
    return LitinfantojuvPublicForm(**kwargs)


def get_litinfantojuv_cmd(litinfantojuv_id):
    """
    Find litinfantojuv by her id
    :param litinfantojuv_id: the litinfantojuv id
    :return: Command
    """
    return NodeSearch(litinfantojuv_id)


def delete_litinfantojuv_cmd(litinfantojuv_id):
    """
    Construct a command to delete a Litinfantojuv
    :param litinfantojuv_id: litinfantojuv's id
    :return: Command
    """
    return DeleteNode(litinfantojuv_id)

