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


def generate_timestamp() -> str:
    timestamp = int(time.time() * 1000)
    return str(timestamp)

def print_router_stats(base_url: str, url_path: str):
    session = requests.Session()
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Accept": "application/xml, text/xml, */*; q=0.01",
        "X-Requested-With": "XMLHttpRequest",
        "Referer": base_url
    }

    print(f"URL: {url_path}")
    
    try:
        response = session.get(url_path, headers=headers, timeout=5)

        if response.status_code == 200:
            print(response.text)
        else:
            print(f"Failed to pull data. HTTP Status: {response.status_code}")

    except Exception as e:
        print(f"Connection error: {e}")

def main():
    BASE_URL = "http://jazz.wifi"
    # BASE_URL = "http://192.168.1.1"
    HOME_PATH = "/mark_home.w.xml"
    TITLE_PATH = "/mark_title.w.xml"

    timestamp = generate_timestamp()
    print_router_stats(BASE_URL, f"{BASE_URL}{HOME_PATH}?_={timestamp}")

    timestamp = generate_timestamp()
    print_router_stats(BASE_URL, f"{BASE_URL}{TITLE_PATH}?_={timestamp}")

if __name__ == "__main__":
    main()