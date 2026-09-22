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

import tkinter as tk


class MainView(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Jazz 4G WiFi Device Monitor")
        self.geometry("600x400")
        # self.resizable(False, False)
        self._setup_ui()

    def _setup_ui(self):
        self.entry = tk.Entry(self)
        self.entry.pack(padx=10, pady=10, fill=tk.BOTH)

        self.text_box = tk.Text(self, height=10, width=40)
        self.text_box.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
        
        self.button_frame = tk.Frame(self)
        self.button_frame.pack(fill=tk.X, padx=10, pady=(0, 10))

        self.call_home_btn = tk.Button(self.button_frame, text="Call /mark_home.w.xml")
        self.call_home_btn.pack(side=tk.LEFT, padx=5, expand=True, fill=tk.X)

        self.call_title_btn = tk.Button(self.button_frame, text="Call /mark_title.w.xml")
        self.call_title_btn.pack(side=tk.LEFT, padx=5, expand=True, fill=tk.X)

        self.call_model_home_btn = tk.Button(self.button_frame, text="Display MarkHome API")
        self.call_model_home_btn.pack(side=tk.LEFT, padx=5, expand=True, fill=tk.X)

        self.call_model_title_btn = tk.Button(self.button_frame, text="Display MarkTitle API")
        self.call_model_title_btn.pack(side=tk.LEFT, padx=5, expand=True, fill=tk.X)

    def update_output(self, text: str):
        self.text_box.delete("1.0", "end")
        self.text_box.insert("1.0", text)

    def update_source(self, text: str):
        self.entry.delete(0, tk.END)
        self.entry.insert(0, text)

    def bind_call_home(self, callback):
        self.call_home_btn.config(command=callback)

    def bind_call_title(self, callback):
        self.call_title_btn.config(command=callback)

    def bind_call_model_home(self, callback):
        self.call_model_home_btn.config(command=callback)

    def bind_call_model_title(self, callback):
        self.call_model_title_btn.config(command=callback)
        