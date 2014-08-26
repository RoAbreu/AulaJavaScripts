# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaegraph.business_base import NodeSearch, DeleteNode
from acao_app.commands import ListAcaoCommand, SaveAcaoCommand, UpdateAcaoCommand, \
    AcaoPublicForm, AcaoDetailForm, AcaoShortForm


def save_acao_cmd(**acao_properties):
    """
    Command to save Acao entity
    :param acao_properties: a dict of properties to save on model
    :return: a Command that save Acao, validating and localizing properties received as strings
    """
    return SaveAcaoCommand(**acao_properties)


def update_acao_cmd(acao_id, **acao_properties):
    """
    Command to update Acao entity with id equals 'acao_id'
    :param acao_properties: a dict of properties to update model
    :return: a Command that update Acao, validating and localizing properties received as strings
    """
    return UpdateAcaoCommand(acao_id, **acao_properties)


def list_acaos_cmd():
    """
    Command to list Acao entities ordered by their creation dates
    :return: a Command proceed the db operations when executed
    """
    return ListAcaoCommand()


def acao_detail_form(**kwargs):
    """
    Function to get Acao's detail form.
    :param kwargs: form properties
    :return: Form
    """
    return AcaoDetailForm(**kwargs)


def acao_short_form(**kwargs):
    """
    Function to get Acao's short form. just a subset of acao's properties
    :param kwargs: form properties
    :return: Form
    """
    return AcaoShortForm(**kwargs)

def acao_public_form(**kwargs):
    """
    Function to get Acao'spublic form. just a subset of acao's properties
    :param kwargs: form properties
    :return: Form
    """
    return AcaoPublicForm(**kwargs)


def get_acao_cmd(acao_id):
    """
    Find acao by her id
    :param acao_id: the acao id
    :return: Command
    """
    return NodeSearch(acao_id)


def delete_acao_cmd(acao_id):
    """
    Construct a command to delete a Acao
    :param acao_id: acao's id
    :return: Command
    """
    return DeleteNode(acao_id)

