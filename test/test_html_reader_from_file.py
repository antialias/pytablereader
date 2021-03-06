# encoding: utf-8

"""
.. codeauthor:: Tsuyoshi Hombashi <tsuyoshi.hombashi@gmail.com>
"""

from __future__ import unicode_literals

import os

import pytablereader as ptr
import pytablewriter as ptw
import pytest


class Test_HtmlTableTextLoader_load(object):

    @pytest.mark.parametrize(["filename"], [
        ["python - Wiktionary.html"],
    ])
    def test_smoke(self, tmpdir, filename):
        test_data_file_path = os.path.join(
            os.path.dirname(__file__), "data", filename)
        loader = ptr.TableFileLoader(test_data_file_path)

        success_count = 0

        for tabledata in loader.load():
            if tabledata.is_empty():
                continue

            assert len(ptw.dump_tabledata(tabledata)) > 10

            success_count += 1

        assert success_count > 0
