# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaegraph.business_base import NodeSearch, DeleteNode
from livroNovo_app.commands import ListLivroNovoCommand, SaveLivroNovoCommand, UpdateLivroNovoCommand, \
    LivroNovoPublicForm, LivroNovoDetailForm, LivroNovoShortForm


def save_livro_novo_cmd(**livro_novo_properties):
    """
    Command to save LivroNovo entity
    :param livro_novo_properties: a dict of properties to save on model
    :return: a Command that save LivroNovo, validating and localizing properties received as strings
    """
    return SaveLivroNovoCommand(**livro_novo_properties)


def update_livro_novo_cmd(livro_novo_id, **livro_novo_properties):
    """
    Command to update LivroNovo entity with id equals 'livro_novo_id'
    :param livro_novo_properties: a dict of properties to update model
    :return: a Command that update LivroNovo, validating and localizing properties received as strings
    """
    return UpdateLivroNovoCommand(livro_novo_id, **livro_novo_properties)


def list_livro_novos_cmd():
    """
    Command to list LivroNovo entities ordered by their creation dates
    :return: a Command proceed the db operations when executed
    """
    return ListLivroNovoCommand()


def livro_novo_detail_form(**kwargs):
    """
    Function to get LivroNovo's detail form.
    :param kwargs: form properties
    :return: Form
    """
    return LivroNovoDetailForm(**kwargs)


def livro_novo_short_form(**kwargs):
    """
    Function to get LivroNovo's short form. just a subset of livro_novo's properties
    :param kwargs: form properties
    :return: Form
    """
    return LivroNovoShortForm(**kwargs)

def livro_novo_public_form(**kwargs):
    """
    Function to get LivroNovo'spublic form. just a subset of livro_novo's properties
    :param kwargs: form properties
    :return: Form
    """
    return LivroNovoPublicForm(**kwargs)


def get_livro_novo_cmd(livro_novo_id):
    """
    Find livro_novo by her id
    :param livro_novo_id: the livro_novo id
    :return: Command
    """
    return NodeSearch(livro_novo_id)


def delete_livro_novo_cmd(livro_novo_id):
    """
    Construct a command to delete a LivroNovo
    :param livro_novo_id: livro_novo's id
    :return: Command
    """
    return DeleteNode(livro_novo_id)

