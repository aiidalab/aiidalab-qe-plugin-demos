"""Module to provide functionality to edit structures."""


import ase
import ipywidgets as ipw
import numpy as np
import spglib
import traitlets as tl
from aiidalab_widgets_base.utils import StatusHTML
from aiidalab_widgets_base.structures import _register_structure

class StructureEditor(ipw.VBox):
    """Widget that allows for cut surface slab."""

    structure = tl.Instance(ase.Atoms, allow_none=True)

    def __init__(self, title="EOS editor"):
        self.title = title
        self._status_message = StatusHTML()

        self.surface_indices = ipw.HBox(
                    [
                        ipw.IntText(value=1, layout={"width": "60px"})
                        for i in range(3)
                    ]
                )
        self.nlayer = ipw.IntText(description="Layers",
                                  value=3,
                                  )
        self.vacuum = ipw.FloatText(description="Vacuum (Å)",
                                    value=5,
                                    )
        self.periodic = ipw.Checkbox(description="Periodic",
                                            value=False,
                                            indent=False,
                                            )
        apply_surface_indices = ipw.Button(description="Generate surface")
        apply_surface_indices.on_click(self.apply_surface_indices)
        super().__init__(
            children=[
                self._status_message,
                ipw.HBox(
                    [
                        ipw.HTML(
                            "Surface indices: ",
                        ),
                        self.surface_indices,
                    ],
                ),
                self.nlayer,
                self.vacuum,
                self.periodic,
                apply_surface_indices,
            ],
        )


    @tl.observe("structure")
    def _observe_structure(self, change):
        """Update cell after the structure has been modified."""
        # reset transformation matrix
        self.reset_surface_indices_matrix()

    @_register_structure
    def apply_surface_indices(self, _=None, atoms=None):
        """Apply the transformation matrix to the structure."""
        from ase.build import surface

        # only update structure when atoms is not None.
        if atoms is not None:
            indices = [self.surface_indices.children[i].value for i in range(3)]
            try:
                atoms = surface(atoms, indices,
                                layers=self.nlayer.value,
                                vacuum=self.vacuum.value,
                                periodic=self.periodic.value,
                                )
            except Exception as e:
                self._status_message.message = """
            <div class="alert alert-info">
            <strong>The transformation matrix is wrong! {}</strong>
            </div>
            """.format(
                    e
                )
                return
            # translate
            self.structure = atoms

    @_register_structure
    def reset_surface_indices_matrix(self, _=None, atoms=None):
        """Reset the transformation matrix to identity matrix."""
        for i in range(3):
                self.surface_indices.children[i].value = 1
