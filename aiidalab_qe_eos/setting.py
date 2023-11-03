# -*- coding: utf-8 -*-
"""Panel for EOS plugin.
"""
import ipywidgets as ipw
from aiidalab_qe.common.panel import Panel

class Setting(Panel):

    title = "EOS Settings"
    identifier = "eos"

    def __init__(self, **kwargs):
        self.settings_title = ipw.HTML(
            """<div style="padding-top: 0px; padding-bottom: 0px">
            <h4>Settings</h4></div>"""
        )
        self.settings_help = ipw.HTML(
            """<div style="line-height: 140%; padding-top: 0px; padding-bottom: 5px">
            Please set the value of scale and number of points.
            </div>"""
        )
        self.workchain_protocol = ipw.ToggleButtons(
            options=["fast", "moderate", "precise"],
            value="moderate",
        )
        self.scale = ipw.FloatText(
            value=0.05,
            description="Value of scale:",
            disabled=False,
            style={"description_width": "initial"},
        )
        self.npoint = ipw.IntText(
            value=5,
            description="Value of npoint:",
            disabled=False,
            style={"description_width": "initial"},
        )

        self.children=[
                self.settings_title,
                self.settings_help,
                self.scale,
                self.npoint,
            ]
        super().__init__(**kwargs)

    def get_panel_value(self):
        """Return a dictionary with the input parameters for the plugin."""
        return {
            "scale": self.scale.value,
            "npoint": self.npoint.value,
        }

    def set_panel_value(self, input_dict):
        """Set a dictionary with the input parameters for the plugin."""
        self.scale.value = input_dict.get("scale", 1)
        self.npoint.value = input_dict.get("npoint", 2)
