# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaegraph.business_base import NodeSearch, DeleteNode
from livro_app.commands import ListLivroCommand, SaveLivroCommand, UpdateLivroCommand, \
    LivroPublicForm, LivroDetailForm, LivroShortForm


def save_livro_cmd(**livro_properties):
    """
    Command to save Livro entity
    :param livro_properties: a dict of properties to save on model
    :return: a Command that save Livro, validating and localizing properties received as strings
    """
    return SaveLivroCommand(**livro_properties)


def update_livro_cmd(livro_id, **livro_properties):
    """
    Command to update Livro entity with id equals 'livro_id'
    :param livro_properties: a dict of properties to update model
    :return: a Command that update Livro, validating and localizing properties received as strings
    """
    return UpdateLivroCommand(livro_id, **livro_properties)


def list_livros_cmd():
    """
    Command to list Livro entities ordered by their creation dates
    :return: a Command proceed the db operations when executed
    """
    return ListLivroCommand()


def livro_detail_form(**kwargs):
    """
    Function to get Livro's detail form.
    :param kwargs: form properties
    :return: Form
    """
    return LivroDetailForm(**kwargs)


def livro_short_form(**kwargs):
    """
    Function to get Livro's short form. just a subset of livro's properties
    :param kwargs: form properties
    :return: Form
    """
    return LivroShortForm(**kwargs)

def livro_public_form(**kwargs):
    """
    Function to get Livro'spublic form. just a subset of livro's properties
    :param kwargs: form properties
    :return: Form
    """
    return LivroPublicForm(**kwargs)


def get_livro_cmd(livro_id):
    """
    Find livro by her id
    :param livro_id: the livro id
    :return: Command
    """
    return NodeSearch(livro_id)


def delete_livro_cmd(livro_id):
    """
    Construct a command to delete a Livro
    :param livro_id: livro's id
    :return: Command
    """
    return DeleteNode(livro_id)

