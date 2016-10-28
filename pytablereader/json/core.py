# encoding: utf-8

"""
.. codeauthor:: Tsuyoshi Hombashi <gogogo.vm@gmail.com>
"""

from __future__ import absolute_import
import json

from .._constant import SourceType
from .._constant import TableNameTemplate as tnt
from ..interface import TableLoader
from .formatter import JsonTableFormatter


class JsonTableLoader(TableLoader):
    """
    Abstract class of JSON table loader.
    """

    @property
    def _format_name(self):
        return "json"


class JsonTableFileLoader(JsonTableLoader):
    """
    Concrete class of JSON file loader.

    .. py:attribute:: table_name

        Table name string. Defaults to ``%(filename)s_%(key)s``.
    """

    @property
    def source_type(self):
        return SourceType.FILE

    def __init__(self, file_path=None):
        super(JsonTableFileLoader, self).__init__(file_path)

    def load(self):
        """
        Extract |TableData| from a JSON file.
        |load_source_desc_file|

        This method can be loading two types of JSON formats:
        **(1)** single table data in a file,
        acceptable JSON schema is as follows:

        .. code-block:: json

            {
                "type": "array",
                "items": {
                    "type": "object",
                    "additionalProperties": {
                        "anyOf": [
                            {"type": "string"},
                            {"type": "number"},
                            {"type": "null"},
                        ],
                    },
                },
            }

        **(2)** multiple table data in a file,
        acceptable JSON schema is as follows:

        .. code-block:: json

            {
                "type": "object",
                "additionalProperties": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "additionalProperties": {
                            "anyOf": [
                                {"type": "string"},
                                {"type": "number"},
                                {"type": "null"}
                            ]
                        }
                    }
                }
            }

        :return:
            Loaded table data iterator.
            |load_table_name_desc|

            ===================  ==============================================
            format specifier     value after the replacement
            ===================  ==============================================
            ``%(filename)s``     |filename_desc|
            ``%(key)s``          | This is replaced the different value
                                 | for each single/multipl JSON tables:
                                 | [single JSON table]
                                 | ``%(format_name)s%(format_id)s``
                                 | [multiple JSON table] Table data key.
            ``%(format_name)s``  ``"json"``
            ``%(format_id)s``    |format_id_desc|
            ``%(global_id)s``    |global_id|
            ===================  ==============================================
        :rtype: |TableData| iterator
        :raises pytablereader.error.InvalidDataError:
            If the data is invalid JSON.
        :raises pytablereader.error.ValidationError:
            If the data is not acceptable JSON format.
        """

        self._validate()

        with open(self.source, "r") as fp:
            json_buffer = json.load(fp)

        formatter = JsonTableFormatter(json_buffer)
        formatter.accept(self)

        return formatter.to_table_data()

    def _get_default_table_name_template(self):
        return "{:s}_{:s}".format(tnt.FILENAME, tnt.KEY)


class JsonTableTextLoader(JsonTableLoader):
    """
    Concrete class of JSON text loader.

    .. py:attribute:: table_name

        Table name string. Defaults to ``%(key)s``.
    """

    @property
    def source_type(self):
        return SourceType.TEXT

    def __init__(self, text):
        super(JsonTableTextLoader, self).__init__(text)

    def load(self):
        """
        Extract |TableData| from a JSON text.
        |load_source_desc_text|

        :return:
            Loaded table data iterator.
            |load_table_name_desc|

            ===================  ==============================================
            format specifier     value after the replacement
            ===================  ==============================================
            ``%(filename)s``     ``""``
            ``%(key)s``          | This is replaced the different value
                                 | for each single/multipl JSON tables:
                                 | [single JSON table]
                                 | ``%(format_name)s%(format_id)s``
                                 | [multiple JSON table] Table data key.
            ``%(format_name)s``  ``"json"``
            ``%(format_id)s``    |format_id_desc|
            ``%(global_id)s``    |global_id|
            ===================  ==============================================
        :rtype: |TableData| iterator
        """

        self._validate()

        json_buffer = json.loads(self.source)

        formatter = JsonTableFormatter(json_buffer)
        formatter.accept(self)

        return formatter.to_table_data()

    def _get_default_table_name_template(self):
        return "{:s}".format(tnt.KEY)