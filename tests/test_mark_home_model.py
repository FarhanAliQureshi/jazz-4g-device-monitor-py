# Copyright (C) 2026 Farhan Ali Qureshi
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#

import unittest

from src.models.xml_model import MarkHomeModel


class TestHomeModel(unittest.TestCase):
    def setUp(self):
        self.home_model = MarkHomeModel(None)
        self.test_xml = """<?xml version="1.0" encoding="UTF-8"?>
            <status>
            <divice>
            <networkmode>3</networkmode>
            <modem_mode>0</modem_mode>
            <op_mode>4G,LTE</op_mode>
            <sig>5</sig>
            <roam>0</roam>
            <cell>11024,43286272,842,84481ecbc1bd9b35</cell>
            <utms_cell_info>-1</utms_cell_info>
            <geran_cell_info>-1</geran_cell_info>
            <netstatus>9</netstatus>
            <wifistatus>1</wifistatus>
            <dial_mode>0</dial_mode>
            </divice>
            <user_cnt>2</user_cnt>
            <update>1</update>
            <tx>1.31 GBytes</tx>
            <rx>2.95 GBytes</rx>
            <active_time>2days 03:22:46</active_time>
            </status>"""
        
        self.broken_xml = """<?xml version="1.0" encoding="UTF-8"?>
            <status>
            <divice>
            <networkmode>3</networkmode>
            <modem_mode>0</modem_mode>
            <op_mode>4G,LTE"""

    def test_processing_all_correct_key_value(self):
        self.home_model.process_data(self.test_xml)
        self.assertEqual(self.home_model.networkmode, 3)
        self.assertEqual(self.home_model.modem_mode, 0)
        self.assertEqual(self.home_model.op_mode, "4G,LTE")
        self.assertEqual(self.home_model.sig, 5)
        self.assertEqual(self.home_model.roam, 0)
        self.assertEqual(self.home_model.cell, "11024,43286272,842,84481ecbc1bd9b35")
        self.assertEqual(self.home_model.utms_cell_info, -1)
        self.assertEqual(self.home_model.geran_cell_info, -1)
        self.assertEqual(self.home_model.netstatus, 9)
        self.assertEqual(self.home_model.wifistatus, 1)
        self.assertEqual(self.home_model.dial_mode, 0)
        self.assertEqual(self.home_model.user_cnt, 2)
        self.assertEqual(self.home_model.update, 1)
        self.assertEqual(self.home_model.tx, "1.31 GBytes")
        self.assertEqual(self.home_model.rx, "2.95 GBytes")
        self.assertEqual(self.home_model.active_time, "2days 03:22:46")

    def test_process_none_raises_value_exception(self):
        with self.assertRaises(ValueError):
            self.home_model.process_data(None)

    def test_process_empty_raises_value_exception(self):
        with self.assertRaises(ValueError):
            self.home_model.process_data("")

    def test_process_broken_xml_raises_runtime_exception(self):
        with self.assertRaises(RuntimeError):
            self.home_model.process_data(self.broken_xml)
