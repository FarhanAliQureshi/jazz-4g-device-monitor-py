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

from src.models.xml_base_model import XmlBaseModel


class MarkTitleModel(XmlBaseModel):
    def __init__(self, data: str | None = None):
        super().__init__(data)
        self._set_defaults()
        if self._root is not None:
            self.process_data()

    def _set_defaults(self):
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

    def reset(self):
        super().reset()
        self._set_defaults()

    def process_data(self, data: str | None = None):
        if data and data.strip():
            self.reset()
            self.raw_data = data

        if self._root is None:
            raise ValueError("Must provide raw data from API")

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
