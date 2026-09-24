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

from src.models.mark_home_model import MarkHomeModel
from src.models.mark_title_model import MarkTitleModel
from src.models.router_api_model import RouterApiModel


class DataModel:
    def __init__(self):
        self.api_model = RouterApiModel()

    def get_home_model(self) -> MarkHomeModel:
        xml_data = self.api_model.get_home_api_data()
        if self.api_model.api_error:
            raise RuntimeError(self.api_model.api_error_message)
        
        model = MarkHomeModel(xml_data)
        model.source_url = self.api_model.api_url
        model.datetime_stamp = self.api_model.datetime_stamp

        return model

    def get_title_model(self) -> MarkTitleModel:
        xml_data = self.api_model.get_title_api_data()
        if self.api_model.api_error:
            raise RuntimeError(self.api_model.api_error_message)
        
        model = MarkTitleModel(xml_data)
        model.source_url = self.api_model.api_url
        model.datetime_stamp = self.api_model.datetime_stamp

        return model
