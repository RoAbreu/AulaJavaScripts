# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaegraph.business_base import NodeSearch, DeleteNode
from didaticos_app.commands import ListDidaticosCommand, SaveDidaticosCommand, UpdateDidaticosCommand, \
    DidaticosPublicForm, DidaticosDetailForm, DidaticosShortForm


def save_didaticos_cmd(**didaticos_properties):
    """
    Command to save Didaticos entity
    :param didaticos_properties: a dict of properties to save on model
    :return: a Command that save Didaticos, validating and localizing properties received as strings
    """
    return SaveDidaticosCommand(**didaticos_properties)


def update_didaticos_cmd(didaticos_id, **didaticos_properties):
    """
    Command to update Didaticos entity with id equals 'didaticos_id'
    :param didaticos_properties: a dict of properties to update model
    :return: a Command that update Didaticos, validating and localizing properties received as strings
    """
    return UpdateDidaticosCommand(didaticos_id, **didaticos_properties)


def list_didaticoss_cmd():
    """
    Command to list Didaticos entities ordered by their creation dates
    :return: a Command proceed the db operations when executed
    """
    return ListDidaticosCommand()


def didaticos_detail_form(**kwargs):
    """
    Function to get Didaticos's detail form.
    :param kwargs: form properties
    :return: Form
    """
    return DidaticosDetailForm(**kwargs)


def didaticos_short_form(**kwargs):
    """
    Function to get Didaticos's short form. just a subset of didaticos's properties
    :param kwargs: form properties
    :return: Form
    """
    return DidaticosShortForm(**kwargs)

def didaticos_public_form(**kwargs):
    """
    Function to get Didaticos'spublic form. just a subset of didaticos's properties
    :param kwargs: form properties
    :return: Form
    """
    return DidaticosPublicForm(**kwargs)


def get_didaticos_cmd(didaticos_id):
    """
    Find didaticos by her id
    :param didaticos_id: the didaticos id
    :return: Command
    """
    return NodeSearch(didaticos_id)


def delete_didaticos_cmd(didaticos_id):
    """
    Construct a command to delete a Didaticos
    :param didaticos_id: didaticos's id
    :return: Command
    """
    return DeleteNode(didaticos_id)

