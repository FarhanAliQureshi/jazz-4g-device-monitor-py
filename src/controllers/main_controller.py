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


class MainController:
    def __init__(self, model: DataModel, view: MainView):
        self.model = model
        self.view = view
        self.bind_callbacks()

    def bind_callbacks(self):
        self.view.bind_call_home(self.handle_call_home)
        self.view.bind_call_title(self.handle_call_title)

    def handle_call_home(self):
        raw_data = self.model.get_home_raw_data()
        self.view.update_source(self.model.source_url)
        self.view.update_output(raw_data)

    def handle_call_title(self):
        raw_data = self.model.get_title_raw_data()
        self.view.update_source(self.model.source_url)
        self.view.update_output(raw_data)
