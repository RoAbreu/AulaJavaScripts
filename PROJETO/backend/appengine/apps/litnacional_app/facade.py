# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaegraph.business_base import NodeSearch, DeleteNode
from litnacional_app.commands import ListLitnacionalCommand, SaveLitnacionalCommand, UpdateLitnacionalCommand, \
    LitnacionalPublicForm, LitnacionalDetailForm, LitnacionalShortForm


def save_litnacional_cmd(**litnacional_properties):
    """
    Command to save Litnacional entity
    :param litnacional_properties: a dict of properties to save on model
    :return: a Command that save Litnacional, validating and localizing properties received as strings
    """
    return SaveLitnacionalCommand(**litnacional_properties)


def update_litnacional_cmd(litnacional_id, **litnacional_properties):
    """
    Command to update Litnacional entity with id equals 'litnacional_id'
    :param litnacional_properties: a dict of properties to update model
    :return: a Command that update Litnacional, validating and localizing properties received as strings
    """
    return UpdateLitnacionalCommand(litnacional_id, **litnacional_properties)


def list_litnacionals_cmd():
    """
    Command to list Litnacional entities ordered by their creation dates
    :return: a Command proceed the db operations when executed
    """
    return ListLitnacionalCommand()


def litnacional_detail_form(**kwargs):
    """
    Function to get Litnacional's detail form.
    :param kwargs: form properties
    :return: Form
    """
    return LitnacionalDetailForm(**kwargs)


def litnacional_short_form(**kwargs):
    """
    Function to get Litnacional's short form. just a subset of litnacional's properties
    :param kwargs: form properties
    :return: Form
    """
    return LitnacionalShortForm(**kwargs)

def litnacional_public_form(**kwargs):
    """
    Function to get Litnacional'spublic form. just a subset of litnacional's properties
    :param kwargs: form properties
    :return: Form
    """
    return LitnacionalPublicForm(**kwargs)


def get_litnacional_cmd(litnacional_id):
    """
    Find litnacional by her id
    :param litnacional_id: the litnacional id
    :return: Command
    """
    return NodeSearch(litnacional_id)


def delete_litnacional_cmd(litnacional_id):
    """
    Construct a command to delete a Litnacional
    :param litnacional_id: litnacional's id
    :return: Command
    """
    return DeleteNode(litnacional_id)

