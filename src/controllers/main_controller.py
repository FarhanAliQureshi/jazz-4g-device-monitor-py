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

from src.models.data_model import DataModel
from src.views.main_view import MainView
from datetime import datetime

class MainController:
    def __init__(self, model: DataModel, view: MainView):
        self.model = model
        self.view = view
        self.bind_callbacks()

    def bind_callbacks(self):
        self.view.bind_call_home(self.handle_call_home)
        self.view.bind_call_title(self.handle_call_title)
        self.view.bind_call_model_home(self.handle_call_model_home)
        self.view.bind_call_model_title(self.handle_call_model_title)

    def handle_call_home(self):
        home_model = self.model.get_home_model()
        self.view.update_source(home_model.source_url)
        self.view.update_output(home_model.raw_data)

    def handle_call_title(self):
        title_model = self.model.get_title_model()
        self.view.update_source(title_model.source_url)
        self.view.update_output(title_model.raw_data)

    def handle_call_model_home(self):
        try:
            home = self.model.get_home_model()
        except Exception as e:  # noqa: BLE001
            self.view.update_source("")
            self.view.update_output(f"ERROR: {e}")
            return

        self.view.update_source(home.source_url)
        output = []
        output.append(f"Log Date Time: {home.datetime_stamp}")
        output.append(f"Network Mode: {home.networkmode}")
        output.append(f"Modem Mode: {home.modem_mode}")
        output.append(f"Operation Mode: {home.op_mode}")
        output.append(f"Signal Strength: {home.sig}")
        output.append(f"Roaming: {home.roam}")
        output.append(f"Cell Information: {home.cell}")
        output.append(f"UTMS Cell Information: {home.utms_cell_info}")
        output.append(f"Geran Cell Information: {home.geran_cell_info}")
        output.append(f"Net Status: {home.netstatus}")
        output.append(f"WiFi Status: {home.wifistatus}")
        output.append(f"Dial Mode: {home.dial_mode}")
        output.append(f"User Count: {home.user_cnt}")
        output.append(f"Update: {home.update}")
        output.append(f"Sent: {home.tx}")
        output.append(f"Received: {home.rx}")
        output.append(f"Active Time: {home.active_time}")
        self.view.update_output("\n".join(output))

    def handle_call_model_title(self):
        try:
            title = self.model.get_title_model()
        except Exception as e:  # noqa: BLE001
            self.view.update_source("")
            output = []
            output.append(f"Log Date Time: {datetime.now()}")  # noqa: DTZ005
            output.append(f"ERROR: {e}")
            self.view.update_output("\n".join(output))
            return

        self.view.update_source(title.source_url)        
        output = []
        output.append(f"Log Date Time: {title.datetime_stamp}")
        output.append(f"Timeout: {title.timeout}")
        output.append(f"Login: {title.login}")
        output.append(f"Language: {title.lang}")
        output.append(f"Times: {title.times}")
        output.append(f"Count: {title.count}")
        output.append(f"SD Times: {title.sd_times}")
        output.append(f"SD Count: {title.sd_count}")
        output.append(f"DSC: {title.dsc}")
        output.append(f"ONEX: {title.onex}")
        output.append(f"WiFi: {title.wifi}")
        output.append(f"Battery: {title.batt}")
        output.append(f"Battery Percentage: {title.batt_p}%")
        output.append(f"CSPN: {title.cspn}")
        output.append(f"PIN: {title.pin}")
        output.append(f"USB: {title.usb}")
        output.append(f"Net Status: {title.netstatus}")
        output.append(f"Operation Mode: {title.op_mode}")
        output.append(f"Roaming: {title.roam}")
        output.append(f"SD Status: {title.sd_st}")
        output.append(f"Rate: {title.rate}")
        output.append(f"Fota: {title.fota}")
        output.append(f"SMS Index: {title.sms_ind}")
        output.append(f"SMS Count: {title.sms_cnt}")
        output.append(f"Firmware Software Version: {title.swver}")
        output.append(f"CUP: {title.cup}")
        self.view.update_output("\n".join(output))
