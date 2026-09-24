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

import time
from datetime import datetime

import requests


class RouterApiModel:
    def __init__(self):
        self.base_url: str = "http://jazz.wifi"
        # self.base_url: str = "http://192.168.1.1"
        self.home_api_path: str = "/mark_home.w.xml"
        self.title_api_path: str = "/mark_title.w.xml"
        self.api_url: str = ""
        self.api_response: str = ""
        self.api_error: bool = False
        self.api_error_message: str = ""
        self.datetime_stamp: datetime = None

    def _generate_timestamp(self) -> str:
        timestamp = int(time.time() * 1000)
        return str(timestamp)

    def _call_router_api(self, api_path: str) -> str:
        session = requests.Session()
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Accept": "application/xml, text/xml, */*; q=0.01",
            "X-Requested-With": "XMLHttpRequest",
            "Referer": self.base_url
        }

        timestamp = self._generate_timestamp()
        url = f"{self.base_url}{api_path}?_={timestamp}"
        self.api_url = url
        self.datetime_stamp = datetime.now()  # noqa: DTZ005
        
        try:
            response = session.get(url, headers=headers, timeout=5)

            if response.status_code == 200:
                self.api_error = False
                self.api_error_message = ""
                self.api_response = response.text
                return response.text
            else:
                self.api_error = True
                self.api_error_message = f"Failed to pull data. HTTP Status: {response.status_code}"
                return self.api_error_message

        except Exception as e:  # noqa: BLE001
            self.api_error = True
            msg = f"Connection error: {e}"
            self.api_error_message = msg
            return msg

    def get_home_api_data(self) -> str:
        return self._call_router_api(self.home_api_path)

    def get_title_api_data(self) -> str:
        return self._call_router_api(self.title_api_path)
