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

from dataclasses import dataclass, field
from datetime import datetime
from re import match

from pincer.exceptions import InvalidUrlError, EmbedFieldError
from pincer.utils.api_object import APIObject
from pincer.utils.constants import MISSING, APINullable


def _field_size(field: str) -> int:
    """
    The Discord API removes white space
        when counting the length of a field.

    :param field:
        The field.

    :return:
        Length of the string without white space.
    """
    return 0 if field == MISSING else len(field.strip())


def _is_valid_url(url: str) -> bool:
    """
    Checks whether the url is a proper and valid url.
    (matches for http and attachment protocol.

    :param url:
        The url which must be checked.

    :return:
        Whether the provided url is valid.
    """
    stmt = r"(http[s]|attachment)?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"
    return bool(match(stmt, url))


def _check_if_valid_url(url: str):
    """
    Checks if the provided url is valid.

    :raises InvalidUrlError:
        if the url didn't match the url regex.
        (which means that it was malformed or didn't match the http/attachment
        protocol).
    """
    if not _is_valid_url(url):
        raise InvalidUrlError(
            "Url was malformed or wasn't of protocol http(s)/attachment.")


@dataclass
class EmbedAuthor:
    """
    Representation of the Embed Author class

    :param name:
        Name of the author

    :param url:
        Url of the author

    :param icon_url:
        Url of the author icon

    :param proxy_icon_url:
        A proxied url of the author icon
    """
    icon_url: APINullable[str] = MISSING
    name: APINullable[str] = MISSING
    proxy_icon_url: APINullable[str] = MISSING
    url: APINullable[str] = MISSING

    def __post_init__(self):
        """
        :raises EmbedFieldError:
            Name is longer than 256 characters.

        :raises InvalidUrlError:
            if the url didn't match the url regex.
            (which means that it was malformed or didn't match the
            http/attachment protocol).
        """
        if _field_size(self.name) > 256:
            raise EmbedFieldError.from_desc("Author name", 256, len(self.name))

        _check_if_valid_url(self.url)


@dataclass
class EmbedImage:
    """
    Representation of the Embed Image class

    :param url:
        Source url of the image

    :param proxy_url:
        A proxied url of the image

    :param height:
        Height of the image

    :param width:
        Width of the image
    """

    height: APINullable[int] = MISSING
    proxy_url: APINullable[str] = MISSING
    url: APINullable[str] = MISSING
    width: APINullable[int] = MISSING

    def __post_init__(self):
        """
        :raises InvalidUrlError:
            if the url didn't match the url regex.
            (which means that it was malformed or didn't match the
            http/attachment protocol).
        """
        _check_if_valid_url(self.url)


@dataclass
class EmbedProvider:
    """
    Representation of the Provider class

    :param name:
        Name of the provider

    :param url:
        Url of the provider
    """
    name: APINullable[str] = MISSING
    url: APINullable[str] = MISSING


@dataclass
class EmbedThumbnail:
    """
    Representation of the Embed Thumbnail class

    :param url:
        Source url of the thumbnail

    :param proxy_url:
        A proxied url of the thumbnail

    :param height:
        Height of the thumbnail

    :param width:
        Width of the thumbnail

    """

    height: APINullable[int] = MISSING
    proxy_url: APINullable[str] = MISSING
    url: APINullable[str] = MISSING
    width: APINullable[int] = MISSING

    def __post_init__(self):
        """
        :raises InvalidUrlError:
            if the url didn't match the url regex.
            (which means that it was malformed or didn't match the
            http/attachment protocol).
        """
        _check_if_valid_url(self.url)


@dataclass
class EmbedVideo:
    """
    Representation of the Embed Video class

    :param url:
        Source url of the video

    :param proxy_url:
        A proxied url of the video

    :param height:
        Height of the video

    :param width:
        Width of the video
    """
    height: APINullable[int] = MISSING
    url: APINullable[str] = MISSING
    proxy_url: APINullable[str] = MISSING
    width: APINullable[int] = MISSING


@dataclass
class EmbedFooter:
    """
    Representation of the Embed Footer class

    :param text:
        Footer text

    :param icon_url:
        Url of the footer icon

    :param proxy_icon_url:
        A proxied url of the footer icon

    :raises EmbedFieldError:
        Text is longer than 2048 characters
    """

    text: str

    icon_url: APINullable[str] = MISSING
    proxy_icon_url: APINullable[str] = MISSING

    def __post_init__(self):
        if _field_size(self.text) > 2048:
            raise EmbedFieldError.from_desc(
                "Footer text", 2048, len(self.text)
            )


@dataclass
class EmbedField:
    """
    Representation of the Embed Field class

    :param name:
        The name of the field

    :param value:
        The text in the field

    :param inline:
        Whether or not this field should display inline

    :raises EmbedFieldError:
        Name is longer than 256 characters

    :raises EmbedFieldError:
        Description is longer than 1024 characters
    """

    name: str
    value: str

    inline: APINullable[bool] = MISSING

    def __post_init__(self):
        if _field_size(self.name) > 256:
            raise EmbedFieldError.from_desc(
                "Field name", 256, len(self.name)
            )

        if _field_size(self.value) > 1024:
            raise EmbedFieldError.from_desc(
                "Field value", 1024, len(self.value)
            )


# TODO: Handle Bad Request if embed that is too big is sent
# https://discord.com/developers/docs/resources/channel#embed-limits
# Currently ignored since I don't think it would make sense to put
# This with the Embed class
@dataclass
class Embed(APIObject):
    """
    Representation of the discord Embed class

    :property author:
        Author information.

    :param color:
        Embed color code.

    :param description:
        Embed description.

    :param fields:
        Fields information.

    :param footer:
        Footer information.

    :param image:
        Image information.

    :param provider:
        Provider information.

    :param thumbnail:
        Thumbnail information.

    :param timestamp:
        Timestamp of embed content in ISO format.

    :param title:
        Embed title.

    :param url:
        Embed url.

    :param video:
        Video information.
    """

    author: APINullable[EmbedAuthor] = MISSING
    color: APINullable[int] = MISSING
    description: APINullable[str] = MISSING
    fields: list[EmbedField] = field(default_factory=list)
    footer: APINullable[EmbedFooter] = MISSING
    image: APINullable[EmbedImage] = MISSING
    provider: APINullable[EmbedProvider] = MISSING
    thumbnail: APINullable[EmbedThumbnail] = MISSING
    timestamp: APINullable[str] = MISSING
    title: APINullable[str] = MISSING
    url: APINullable[str] = MISSING
    video: APINullable[EmbedVideo] = MISSING

    def __post_init__(self):
        """
        :raises EmbedFieldError:
            Embed title is longer than 256 characters.
        :raises EmbedFieldError:
            Embed description is longer than 4096 characters.
        :raises EmbedFieldError:
            Embed has more than 25 fields.
        """
        if _field_size(self.title) > 256:
            raise EmbedFieldError.from_desc(
                "Embed title", 256, len(self.title)
            )

        if _field_size(self.description) > 4096:
            raise EmbedFieldError.from_desc(
                "Embed description", 4096, len(self.description)
            )

        if len(self.fields) > 25:
            raise EmbedFieldError.from_desc(
                "Embed field", 25, len(self.fields)
            )

    def set_timestamp(self, time: datetime) -> Embed:
        """
        Discord uses iso format for time stamps.
        This function will set the time to that format.

        :param time:
            A datetime object.

        :return: self
        """
        self.timestamp = time.isoformat()

        return self

    def set_author(
            self,
            icon_url: APINullable[str] = MISSING,
            name: APINullable[str] = MISSING,
            proxy_icon_url: APINullable[str] = MISSING,
            url: APINullable[str] = MISSING
    ) -> Embed:
        """
        Set the author message for the embed. This is the top
        field of the embed.

        :param icon_url:
            The icon which will be next to the author name.

        :param name:
            The name for the author (so the message).

        :param proxy_icon_url:
            A proxied url of the author icon.

        :param url:
            The url for the author name, this will make the
            name field a link/url.

        :return: self
        """

        self.author = EmbedAuthor(
            icon_url=icon_url,
            name=name,
            proxy_icon_url=proxy_icon_url,
            url=url
        )

        return self

    def set_image(
            self,
            height: APINullable[int] = MISSING,
            url: APINullable[str] = MISSING,
            proxy_url: APINullable[str] = MISSING,
            width: APINullable[int] = MISSING
    ) -> Embed:
        """
        Sets an image for your embed.

        :param url:
            Source url of the video

        :param proxy_url:
            A proxied url of the video

        :param height:
            Height of the video

        :param width:
            Width of the video

        :return: self
        """
        self.video = EmbedImage(
            height=height,
            url=url,
            proxy_url=proxy_url,
            width=width
        )

        return self

    def set_thumbnail(
            self,
            height: APINullable[int] = MISSING,
            url: APINullable[str] = MISSING,
            proxy_url: APINullable[str] = MISSING,
            width: APINullable[int] = MISSING
    ) -> Embed:
        """
        Sets the thumbnail of the embed.
        This image is bigger than the `image` property.

        :param url:
            Source url of the video

        :param proxy_url:
            A proxied url of the video

        :param height:
            Height of the video

        :param width:
            Width of the video

        :return self:
        """
        self.video = EmbedThumbnail(
            height=height,
            url=url,
            proxy_url=proxy_url,
            width=width
        )

        return self

    def set_footer(
            self,
            text: str,
            icon_url: APINullable[str] = MISSING,
            proxy_icon_url: APINullable[str] = MISSING
    ) -> Embed:
        """
        Sets the embed footer. This is at the bottom of your embed.

        :param text:
            Footer text

        :param icon_url:
            Url of the footer icon

        :param proxy_icon_url:
            A proxied url of the footer icon

        :return: self
        """
        self.footer = EmbedFooter(
            text=text,
            icon_url=icon_url,
            proxy_icon_url=proxy_icon_url
        )

        return self

    def add_field(
            self,
            name: str,
            value: str,
            inline: APINullable[bool] = MISSING
    ) -> Embed:
        """
        Adds a field to the embed.
        An embed can contain up to 25 fields.

        :param name:
            The name of the field

        :param value:
            The text in the field

        :param inline:
            Whether or not this field should display inline

        :raises EmbedFieldError:
            Raised when there are more than 25 fields in the embed
        """
        _field = EmbedField(
            name=name,
            value=value,
            inline=inline
        )

        if len(self.fields) > 25:
            raise EmbedFieldError.from_desc(
                "Embed field", 25, len(self.fields) + 1
            )

        self.fields += [_field]

        return self
