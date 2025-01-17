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

from pincer.utils.timestamp import Timestamp
from pincer.utils.snowflake import Snowflake
from pincer.utils.api_object import APIObject
from pincer.utils.constants import APINullable, MISSING

@dataclass
class ThreadMetadata(APIObject):
    """
    Represents a Discord Thread Metadata object

    :param archived:
        whether the thread is archived

    :param auto_archive_duration:
        duration in minutes to automatically archive the thread
        after recent activity, can be set to: 60, 1440, 4320, 10080

    :param archive_timestamp:
        timestamp when the thread's archive status was last changed,
        used for calculating recent activity

    :param locked:
        whether the thread is locked; when a thread is locked,
        only users with MANAGE_THREADS can unarchive it

    :param invitable:
        whether non-moderators can add other non-moderators to a thread;
        only available on private threads
    """
    archived: bool
    auto_archive_duration: int
    archive_timestamp: Timestamp
    locked: bool

    invitable: APINullable[bool] = MISSING

@dataclass
class ThreadMember(APIObject):
    """
    Represents a Discord Thread Member object

    :param join_timestamp:
        the time the current user last joined the thread

    :param flags:
        any user-thread settings, currently only used for notifications

    :param id:
        id of the thread

    :param user_id:
        id of the user
    """
    join_timestamp: Timestamp
    flags: int

    id: APINullable[Snowflake] = MISSING
    user_id: APINullable[Snowflake] = MISSING

