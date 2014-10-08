# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaegraph.business_base import NodeSearch, DeleteNode
from budismo_app.commands import ListBudismoCommand, SaveBudismoCommand, UpdateBudismoCommand, \
    BudismoPublicForm, BudismoDetailForm, BudismoShortForm


def save_budismo_cmd(**budismo_properties):
    """
    Command to save Budismo entity
    :param budismo_properties: a dict of properties to save on model
    :return: a Command that save Budismo, validating and localizing properties received as strings
    """
    return SaveBudismoCommand(**budismo_properties)


def update_budismo_cmd(budismo_id, **budismo_properties):
    """
    Command to update Budismo entity with id equals 'budismo_id'
    :param budismo_properties: a dict of properties to update model
    :return: a Command that update Budismo, validating and localizing properties received as strings
    """
    return UpdateBudismoCommand(budismo_id, **budismo_properties)


def list_budismos_cmd():
    """
    Command to list Budismo entities ordered by their creation dates
    :return: a Command proceed the db operations when executed
    """
    return ListBudismoCommand()


def budismo_detail_form(**kwargs):
    """
    Function to get Budismo's detail form.
    :param kwargs: form properties
    :return: Form
    """
    return BudismoDetailForm(**kwargs)


def budismo_short_form(**kwargs):
    """
    Function to get Budismo's short form. just a subset of budismo's properties
    :param kwargs: form properties
    :return: Form
    """
    return BudismoShortForm(**kwargs)

def budismo_public_form(**kwargs):
    """
    Function to get Budismo'spublic form. just a subset of budismo's properties
    :param kwargs: form properties
    :return: Form
    """
    return BudismoPublicForm(**kwargs)


def get_budismo_cmd(budismo_id):
    """
    Find budismo by her id
    :param budismo_id: the budismo id
    :return: Command
    """
    return NodeSearch(budismo_id)


def delete_budismo_cmd(budismo_id):
    """
    Construct a command to delete a Budismo
    :param budismo_id: budismo's id
    :return: Command
    """
    return DeleteNode(budismo_id)

