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

import requests

from src.models.mark_home_model import MarkHomeModel
from src.models.mark_title_model import MarkTitleModel


class DataModel:
    def __init__(self):
        self._base_url = "http://jazz.wifi"     # Or try "http://192.168.1.1"
        self._home_api_path = "/mark_home.w.xml"
        self._title_api_path = "/mark_title.w.xml"
        self._source_url = ""           # NOTE: Temporary, remove after testing
        self._raw_output = ""           # NOTE: Temporary, remove after testing
        self._api_error = False         # NOTE: Temporary, remove after testing
        self._api_error_message = ""    # NOTE: Temporary, remove after testing

    def __generate_timestamp(self) -> str:
        timestamp = int(time.time() * 1000)
        return str(timestamp)

    def get_home_raw_data(self) -> str:
        self._raw_output = self._get_raw_router_stats(self._base_url, self._home_api_path)
        return self._raw_output

    def get_title_raw_data(self) -> str:
        self._raw_output = self._get_raw_router_stats(self._base_url, self._title_api_path)
        return self._raw_output

    # NOTE: Temporary, remove after testing
    @property
    def source_url(self) -> str:
        return self._source_url

    def _get_raw_router_stats(self, base_url: str, api_path: str) -> str:
        session = requests.Session()
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Accept": "application/xml, text/xml, */*; q=0.01",
            "X-Requested-With": "XMLHttpRequest",
            "Referer": base_url
        }

        timestamp = self.__generate_timestamp()
        url = f"{base_url}{api_path}?_={timestamp}"
        self._source_url = url      # NOTE: Temporary for testing
        
        try:
            response = session.get(url, headers=headers, timeout=5)

            if response.status_code == 200:
                # print(response.text)
                self._api_error = False
                self._api_error_message = ""
                return response.text
            else:
                # print(f"Failed to pull data. HTTP Status: {response.status_code}")
                self._api_error = True
                self._api_error_message = f"Failed to pull data. HTTP Status: {response.status_code}"
                return self._api_error_message

        except Exception as e:  # noqa: BLE001
            # print(f"Connection error: {e}")
            self._api_error = True
            msg = f"Connection error: {e}"
            self._api_error_message = msg
            return msg


    def get_mark_home(self) -> MarkHomeModel:
        raw_data = self.get_home_raw_data()
        data = MarkHomeModel(raw_data)
        return data

    def get_mark_title(self) -> MarkTitleModel:
        raw_data = self.get_title_raw_data()
        data = MarkTitleModel(raw_data)
        return data
