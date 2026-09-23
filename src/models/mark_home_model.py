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

