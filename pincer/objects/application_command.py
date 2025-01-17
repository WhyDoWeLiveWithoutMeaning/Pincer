# -*- coding: utf-8 -*-
# MIT License
#
# Copyright (c) 2021 Pincer
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files
# (the "Software"), to deal in the Software without restriction,
# including without limitation the rights to use, copy, modify, merge,
# publish, distribute, sublicense, and/or sell copies of the Software,
# and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
# CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import List, Union

from pincer.utils.api_object import APIObject
from pincer.utils.constants import MISSING, APINullable
from pincer.utils.snowflake import Snowflake


class ApplicationCommandType(Enum):
    """
    Defines the different types of application commands.

    :param CHAT_INPUT:
        Slash commands; a text-based command that shows up when a user
        types /

    :param USER:
        A UI-based command that shows up when you right click or tap on
        a user

    :param MESSAGE:
        A UI-based command that shows up when you right click or tap on
        a message
    """
    CHAT_INPUT = 1
    USER = 2
    MESSAGE = 3


class ApplicationCommandOptionType(Enum):
    """
    Represents a parameter type.

    :param SUB_COMMAND:
        The parameter will be a subcommand.

    :param SUB_COMMAND_GROUP:
        The parameter will be a group of subcommands.

    :param STRING:
        The parameter will be a string.

    :param INTEGER:
        The parameter will be an integer/number. (-2^53 and 2^53)

    :param BOOLEAN:
        The parameter will be a boolean.

    :param USER:
        The parameter will be a Discord user object.

    :param CHANNEL:
        The parameter will be a Discord channel object.

    :param ROLE:
        The parameter will be a Discord role object.

    :param MENTIONABLE:
        The parameter will be mentionable.

    :param NUMBER:
        The parameter will be a float. (-2^53 and 2^53)
    """
    SUB_COMMAND = 1
    SUB_COMMAND_GROUP = 2
    STRING = 3
    INTEGER = 4  # 54-bit
    BOOLEAN = 5
    USER = 6
    CHANNEL = 7
    ROLE = 8
    MENTIONABLE = 9
    NUMBER = 10  # 54-bit


@dataclass
class ApplicationCommandInteractionDataOption(APIObject):
    """
    Represents a Discord Application Command Interaction Data Option

    :param name:
        the name of the parameter

    :param type:
        value of application command option type

    :param value:
        the value of the pair

    :param options:
        present if this option is a group or subcommand
    """
    name: str
    type: int
    value: APINullable[ApplicationCommandOptionType] = MISSING
    options: APINullable[
        List[ApplicationCommandInteractionDataOption]] = MISSING


@dataclass
class ApplicationCommandOptionChoice(APIObject):
    """
    Represents a Discord Application Command Option Choice object

    :param name:
        1-100 character choice name

    :param value:
        value of the choice, up to 100 characters if string
    """
    name: str
    value: Union[str, int, float]


@dataclass
class ApplicationCommandOption(APIObject):
    """
    Represents a Discord Application Command Option object

    :param type:
        the type of option

    :param name:
        1-32 lowercase character name matching `^[\w-]{1,32}$`

    :param description:
        1-100 character description

    :param required:
        if the parameter is required or optional--default `False`

    :param choices:
        choices for `STRING`, `INTEGER`, and `NUMBER`
        types for the user to pick from, max 25

    :param options:
        if the option is a subcommand or subcommand group type,
        this nested options will be the parameters
    """
    type: ApplicationCommandOptionType
    name: str
    description: str

    required: APINullable[bool] = False
    choices: APINullable[List[ApplicationCommandOptionChoice]] = MISSING
    options: APINullable[List[ApplicationCommandOption]] = MISSING


@dataclass
class ApplicationCommand(APIObject):
    """
    Represents a Discord Application Command object

    :param id:
        unique id of the command

    :param type:
        the type of command, defaults `1` if not set

    :param application_id:
        unique id of the parent application

    :param guild_id:
        guild id of the command, if not global

    :param name:
        1-32 character name

    :param description:
        1-100 character description for `CHAT_INPUT` commands,
        empty string for `USER` and `MESSAGE` commands

    :param options:
        the parameters for the command, max 25

    :param default_permission:
        whether the command is enabled by default
        when the app is added to a guild
    """
    id: Snowflake
    type: ApplicationCommandType
    application_id: Snowflake
    name: str
    description: str

    options: APINullable[List[ApplicationCommandOption]] = MISSING
    guild_id: APINullable[Snowflake] = MISSING
    default_permission: APINullable[bool] = True
