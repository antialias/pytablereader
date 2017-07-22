# encoding: utf-8

"""
.. codeauthor:: Tsuyoshi Hombashi <tsuyoshi.hombashi@gmail.com>
"""

from __future__ import absolute_import

import requests


class ValidationError(Exception):
    """
    Exception raised when data is not properly formatted.
    """


class InvalidNameError(Exception):
    """
    Base name error class.
    """


class InvalidTableNameError(InvalidNameError):
    """
    Exception raised when the table name is invalid.
    """


class InvalidHeaderNameError(InvalidNameError):
    """
    Exception raised when a table header name is invalid.
    """


class InvalidPathError(Exception):
    """
    Base path exception class.
    """


class InvalidFilePathError(InvalidPathError):
    """
    Exception raised when invalid file path used.
    """


class InvalidUrlError(InvalidPathError):
    """
    Exception raised when invalid URL used.
    """


class InvalidDataError(ValueError):
    """
    Exception raised when data is invalid as tabular data.
    """


class EmptyDataError(InvalidDataError):
    """
    Exception raised when data does not include valid table data.
    """


class OpenError(IOError):
    """
    Exception raised when failed to open a file.
    """


class LoaderNotFoundError(Exception):
    """
    Exception raised when loader not found.
    """


class HTTPError(requests.RequestException):
    """
    An HTTP error occurred.

    .. seealso::

        http://docs.python-requests.org/en/master/api/#exceptions
    """


class ProxyError(requests.exceptions.ProxyError):
    """
    A proxy error occurred.

    .. seealso::

        http://docs.python-requests.org/en/master/_modules/requests/exceptions/
    """


class PypandocImportError(ImportError):
    """
    Exception raised when import error occurred with pypandoc package.
    """
