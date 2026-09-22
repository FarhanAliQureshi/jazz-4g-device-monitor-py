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

    def __init__(self, data: str | None):
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
        if not data:
            raise ValueError("No data supplied for XML Parser")
        
        self._raw_data = data
        try:
            self._root = ET.fromstring(self._raw_data)
        except ET.ParseError as e:
            raise RuntimeError(f"Error parsing raw data: {e}")

    def get_key_value(self, key_name: str) -> str:
        if not self._root:
            raise RuntimeError("Load data before calling for the value of a key")
        if not key_name:
            raise ValueError("Expected Key Name for ElementTree search")
        
        key = self._root.find(key_name)
        if key is None:
            raise KeyError(f"Key Name '{key_name}' not found in XML ElementTree search")
        
        value = key.text
        return value

class MarkHomeModel(XmlBaseModel):
    def __init__(self, data: str | None):
        super().__init__(None)
        self.reset()
        if data:
            self.process_data(data)

    def reset(self):
        super().reset()
        self.networkmode = 0
        self.modem_mode = 0
        self.op_mode = ""
        self.sig = 0
        self.roam = 0
        self.cell = ""
        self.utms_cell_info = 0
        self.geran_cell_info = 0
        self.netstatus = 0
        self.wifistatus = 0
        self.dial_mode = 0
        self.user_cnt = 0
        self.update = 0
        self.tx = ""
        self.rx = ""
        self.active_time = ""

    def process_data(self, data: str):
        if not data:
            raise ValueError("Must provide raw data from API")

        self.reset()
        self.raw_data = data

        self.networkmode = int(self.get_key_value("divice/networkmode"))
        self.modem_mode = int(self.get_key_value("divice/modem_mode"))
        self.op_mode = self.get_key_value("divice/op_mode")
        self.sig = int(self.get_key_value("divice/sig"))
        self.roam = int(self.get_key_value("divice/roam"))
        self.cell = self.get_key_value("divice/cell")
        self.utms_cell_info = int(self.get_key_value("divice/utms_cell_info"))
        self.geran_cell_info = int(self.get_key_value("divice/geran_cell_info"))
        self.netstatus = int(self.get_key_value("divice/netstatus"))
        self.wifistatus = int(self.get_key_value("divice/wifistatus"))
        self.dial_mode = int(self.get_key_value("divice/dial_mode"))
        self.user_cnt = int(self.get_key_value("user_cnt"))
        self.update = int(self.get_key_value("update"))
        self.tx = self.get_key_value("tx")
        self.rx = self.get_key_value("rx")
        self.active_time = self.get_key_value("active_time")


class MarkTitleModel(XmlBaseModel):
    def __init__(self, data: str | None):
        super().__init__(None)
        self.reset()
        if data:
            self.process_data(data)

    def reset(self):
        super().reset()
        self.timeout = 0
        self.login = 0
        self.lang = ""
        self.times = 0
        self.count = 0
        self.sd_times = 0
        self.sd_count = 0
        self.dsc = 0
        self.onex = 0
        self.wifi = 0
        self.batt = 0
        self.batt_p = 0
        self.cspn = ""
        self.pin = 0
        self.usb = 0
        self.netstatus = 0
        self.op_mode = ""
        self.roam = 0
        self.sd_st = 0
        self.rate = ""
        self.fota = 0
        self.sms_ind = ""
        self.sms_cnt = ""
        self.swver = ""
        self.cup = 0

    def process_data(self, data: str):
        if not data:
            raise ValueError("Must provide raw data from API")

        self.reset()
        self.raw_data = data

        self.timeout = int(self.get_key_value("timeout"))
        self.login = int(self.get_key_value("login"))
        self.lang = self.get_key_value("lang")
        self.times = int(self.get_key_value("times"))
        self.count = int(self.get_key_value("count"))
        self.sd_times = int(self.get_key_value("sd_times"))
        self.sd_count = int(self.get_key_value("sd_count"))
        self.dsc = int(self.get_key_value("dsc"))
        self.onex = int(self.get_key_value("onex"))
        self.wifi = int(self.get_key_value("wifi"))
        self.batt = int(self.get_key_value("batt"))
        self.batt_p = int(self.get_key_value("batt_p"))
        self.cspn = self.get_key_value("cspn")
        self.pin = int(self.get_key_value("pin"))
        self.usb = int(self.get_key_value("usb"))
        self.netstatus = int(self.get_key_value("netstatus"))
        self.op_mode = self.get_key_value("op_mode")
        self.roam = int(self.get_key_value("roam"))
        self.sd_st = int(self.get_key_value("sd_st"))
        self.rate = self.get_key_value("rate")
        self.fota = int(self.get_key_value("fota"))
        self.sms_ind = self.get_key_value("sms_ind")
        self.sms_cnt = self.get_key_value("sms_cnt")
        self.swver = self.get_key_value("swver")
        self.cup = int(self.get_key_value("cup"))
