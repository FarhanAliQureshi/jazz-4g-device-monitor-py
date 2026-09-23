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

from src.models.xml_base_model import XmlBaseModel


class TestXmlModel(unittest.TestCase):
    def setUp(self):
        self.xml_model = XmlBaseModel(None)
        self.test_xml = """<?xml version="1.0" encoding="UTF-8"?>
            <data>
            <key1>value1</key1>
            <key2>2</key2>
            <key3>-3</key3>
            <key4>0</key4>
            <key5>Lorem ipsum</key5>
            </data>"""
        
        self.broken_xml = """<?xml version="1.0" encoding="UTF-8"?>
            <key1>value1</key1>
            <key2>value2"""

    def test_processing_xml_key_value_all_correct(self):
        self.xml_model.raw_data = self.test_xml
        self.assertEqual(self.xml_model.get_key_value("key1"), "value1")
        self.assertEqual(self.xml_model.get_key_value("key2"), "2")
        self.assertEqual(self.xml_model.get_key_value("key3"), "-3")
        self.assertEqual(self.xml_model.get_key_value("key4"), "0")
        self.assertEqual(self.xml_model.get_key_value("key5"), "Lorem ipsum")

    def test_processing_xml_raises_value_exception_on_none(self):
        with self.assertRaises(ValueError):
            self.xml_model.raw_data = None

    def test_processing_xml_raises_value_exception_on_empty_string(self):
        with self.assertRaises(ValueError):
            self.xml_model.raw_data = ""

    def test_processing_xml_raises_runtime_exception_on_broken_xml(self):
        with self.assertRaises(RuntimeError):
            self.xml_model.raw_data = self.broken_xml

    def test_searching_for_key_without_xml_raises_runtime_exception(self):
        empty_model = XmlBaseModel(None)
        with self.assertRaises(RuntimeError):
            empty_model.get_key_value("key")

    def test_searching_with_none_key_name_raises_value_exception(self):
        self.xml_model.raw_data = self.test_xml
        with self.assertRaises(ValueError):
            self.xml_model.get_key_value(None)

    def test_searching_without_key_name_raises_value_exception(self):
        self.xml_model.raw_data = self.test_xml
        with self.assertRaises(ValueError):
            self.xml_model.get_key_value("")

    def test_searching_non_existing_key_name_raises_key_exception(self):
        self.xml_model.raw_data = self.test_xml
        with self.assertRaises(KeyError):
            self.xml_model.get_key_value("KeyNameDoesNotExist")
