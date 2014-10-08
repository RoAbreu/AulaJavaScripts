# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaegraph.business_base import NodeSearch, DeleteNode
from biblias_app.commands import ListBibliasCommand, SaveBibliasCommand, UpdateBibliasCommand, \
    BibliasPublicForm, BibliasDetailForm, BibliasShortForm


def save_biblias_cmd(**biblias_properties):
    """
    Command to save Biblias entity
    :param biblias_properties: a dict of properties to save on model
    :return: a Command that save Biblias, validating and localizing properties received as strings
    """
    return SaveBibliasCommand(**biblias_properties)


def update_biblias_cmd(biblias_id, **biblias_properties):
    """
    Command to update Biblias entity with id equals 'biblias_id'
    :param biblias_properties: a dict of properties to update model
    :return: a Command that update Biblias, validating and localizing properties received as strings
    """
    return UpdateBibliasCommand(biblias_id, **biblias_properties)


def list_bibliass_cmd():
    """
    Command to list Biblias entities ordered by their creation dates
    :return: a Command proceed the db operations when executed
    """
    return ListBibliasCommand()


def biblias_detail_form(**kwargs):
    """
    Function to get Biblias's detail form.
    :param kwargs: form properties
    :return: Form
    """
    return BibliasDetailForm(**kwargs)


def biblias_short_form(**kwargs):
    """
    Function to get Biblias's short form. just a subset of biblias's properties
    :param kwargs: form properties
    :return: Form
    """
    return BibliasShortForm(**kwargs)

def biblias_public_form(**kwargs):
    """
    Function to get Biblias'spublic form. just a subset of biblias's properties
    :param kwargs: form properties
    :return: Form
    """
    return BibliasPublicForm(**kwargs)


def get_biblias_cmd(biblias_id):
    """
    Find biblias by her id
    :param biblias_id: the biblias id
    :return: Command
    """
    return NodeSearch(biblias_id)


def delete_biblias_cmd(biblias_id):
    """
    Construct a command to delete a Biblias
    :param biblias_id: biblias's id
    :return: Command
    """
    return DeleteNode(biblias_id)

