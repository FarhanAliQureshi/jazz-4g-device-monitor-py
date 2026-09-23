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

import xml.etree.ElementTree as ET


class XmlBaseModel:
    _data: str
    _root: ET.ElementTree

    def __init__(self, data: str | None = None):
        self._data = None
        self._root = None
        if data:
            self.raw_data = data

    def reset(self):
        self._data = None
        self._root = None

    @property
    def raw_data(self) -> str:
        return self._data

    @raw_data.setter
    def raw_data(self, data: str) -> None:
        if not data or not data.strip():
            raise ValueError("No data supplied for XML Parser")
        
        self._data = data
        try:
            self._root = ET.fromstring(self._data)
        except ET.ParseError as e:
            raise RuntimeError(f"Error parsing raw data: {e}")

    def get_key_value(self, key_name: str) -> str:
        if self._root is None:
            raise RuntimeError("Load data before calling for the value of a key")
        if not key_name or not key_name.strip():
            raise ValueError("Expected Key Name for ElementTree search")
        
        key = self._root.find(key_name)
        if key is None:
            raise KeyError(f"Key Name '{key_name}' not found in XML ElementTree search")
        
        value = key.text
        return value
