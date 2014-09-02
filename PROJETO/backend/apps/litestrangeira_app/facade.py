# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaegraph.business_base import NodeSearch, DeleteNode
from litestrangeira_app.commands import ListLitestrangeiraCommand, SaveLitestrangeiraCommand, UpdateLitestrangeiraCommand, \
    LitestrangeiraPublicForm, LitestrangeiraDetailForm, LitestrangeiraShortForm


def save_litestrangeira_cmd(**litestrangeira_properties):
    """
    Command to save Litestrangeira entity
    :param litestrangeira_properties: a dict of properties to save on model
    :return: a Command that save Litestrangeira, validating and localizing properties received as strings
    """
    return SaveLitestrangeiraCommand(**litestrangeira_properties)


def update_litestrangeira_cmd(litestrangeira_id, **litestrangeira_properties):
    """
    Command to update Litestrangeira entity with id equals 'litestrangeira_id'
    :param litestrangeira_properties: a dict of properties to update model
    :return: a Command that update Litestrangeira, validating and localizing properties received as strings
    """
    return UpdateLitestrangeiraCommand(litestrangeira_id, **litestrangeira_properties)


def list_litestrangeiras_cmd():
    """
    Command to list Litestrangeira entities ordered by their creation dates
    :return: a Command proceed the db operations when executed
    """
    return ListLitestrangeiraCommand()


def litestrangeira_detail_form(**kwargs):
    """
    Function to get Litestrangeira's detail form.
    :param kwargs: form properties
    :return: Form
    """
    return LitestrangeiraDetailForm(**kwargs)


def litestrangeira_short_form(**kwargs):
    """
    Function to get Litestrangeira's short form. just a subset of litestrangeira's properties
    :param kwargs: form properties
    :return: Form
    """
    return LitestrangeiraShortForm(**kwargs)

def litestrangeira_public_form(**kwargs):
    """
    Function to get Litestrangeira'spublic form. just a subset of litestrangeira's properties
    :param kwargs: form properties
    :return: Form
    """
    return LitestrangeiraPublicForm(**kwargs)


def get_litestrangeira_cmd(litestrangeira_id):
    """
    Find litestrangeira by her id
    :param litestrangeira_id: the litestrangeira id
    :return: Command
    """
    return NodeSearch(litestrangeira_id)


def delete_litestrangeira_cmd(litestrangeira_id):
    """
    Construct a command to delete a Litestrangeira
    :param litestrangeira_id: litestrangeira's id
    :return: Command
    """
    return DeleteNode(litestrangeira_id)

