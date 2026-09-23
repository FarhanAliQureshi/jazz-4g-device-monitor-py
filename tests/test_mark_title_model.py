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

from src.models.mark_title_model import MarkTitleModel


class TestTitleModel(unittest.TestCase):
    def setUp(self):
        self.title_model = MarkTitleModel(None)
        self.test_xml = """<?xml version="1.0" encoding="UTF-8"?>
            <title>
            <timeout>256254</timeout>
            <login>17</login>
            <lang>en</lang>
            <times>0</times>
            <count>5</count>
            <sd_times>0</sd_times>
            <sd_count>5</sd_count>
            <dsc>7</dsc>
            <onex>5</onex>
            <wifi>1</wifi>
            <batt>768</batt>
            <batt_p>77</batt_p>
            <cspn>NETWORK</cspn>
            <pin>0</pin>
            <usb>0</usb>
            <netstatus>9</netstatus>
            <op_mode>4G,LTE</op_mode>
            <roam>0</roam>
            <sd_st>0</sd_st>
            <rate>8644,0</rate>
            <fota>1</fota>
            <sms_ind>3,62</sms_ind>
            <sms_cnt>62,62,0,0</sms_cnt>
            <swver>Mobile.Router.B99</swver>
            <cup>1</cup>
            </title>"""
        
        self.broken_xml = """<?xml version="1.0" encoding="UTF-8"?>
            <title>
            <timeout>256254</timeout>
            <login>17</login>
            <lang>en"""

    def test_processing_all_correct_key_value(self):
        self.title_model.process_data(self.test_xml)
        self.assertEqual(self.title_model.timeout, 256254)
        self.assertEqual(self.title_model.login, 17)
        self.assertEqual(self.title_model.lang, "en")
        self.assertEqual(self.title_model.times, 0)
        self.assertEqual(self.title_model.count, 5)
        self.assertEqual(self.title_model.sd_times, 0)
        self.assertEqual(self.title_model.sd_count, 5)
        self.assertEqual(self.title_model.dsc, 7)
        self.assertEqual(self.title_model.onex, 5)
        self.assertEqual(self.title_model.wifi, 1)
        self.assertEqual(self.title_model.batt, 768)
        self.assertEqual(self.title_model.batt_p, 77)
        self.assertEqual(self.title_model.cspn, "NETWORK")
        self.assertEqual(self.title_model.pin, 0)
        self.assertEqual(self.title_model.usb, 0)
        self.assertEqual(self.title_model.netstatus, 9)
        self.assertEqual(self.title_model.op_mode, "4G,LTE")
        self.assertEqual(self.title_model.roam, 0)
        self.assertEqual(self.title_model.sd_st, 0)
        self.assertEqual(self.title_model.rate, "8644,0")
        self.assertEqual(self.title_model.fota, 1)
        self.assertEqual(self.title_model.sms_ind, "3,62")
        self.assertEqual(self.title_model.sms_cnt, "62,62,0,0")
        self.assertEqual(self.title_model.swver, "Mobile.Router.B99")
        self.assertEqual(self.title_model.cup, 1)

    def test_process_none_raises_value_exception(self):
        with self.assertRaises(ValueError):
            self.title_model.process_data(None)

    def test_process_empty_raises_value_exception(self):
        with self.assertRaises(ValueError):
            self.title_model.process_data("")

    def test_process_broken_xml_raises_runtime_exception(self):
        with self.assertRaises(RuntimeError):
            self.title_model.process_data(self.broken_xml)
