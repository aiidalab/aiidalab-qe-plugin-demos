import ipywidgets as ipw
import traitlets as tl
from ase import Atoms

class SurfaceImporter(ipw.VBox):
    """Create surface structure use ASE builder."""

    structure = tl.Instance(Atoms, allow_none=True)

    def __init__(self, title="Surface importer"):
        self.title = title
        self.fcc111_symbol = ipw.Text(placeholder="Input the symbol of the element")
        self.create_fcc111_structure_btn = ipw.Button(
            description="FCC111 surface",
            button_style="primary",
            tooltip="Generate surface from symbol",
        )
        self.create_fcc111_structure_btn.on_click(self._on_fcc111_button_pressed)
        children = (
            ipw.HBox([self.fcc111_symbol, self.create_fcc111_structure_btn]),
        )
        super().__init__(children=children)

    def _on_fcc111_button_pressed(self, change=None):
        """Create a ase structure when button is pressed."""
        from ase.build import fcc111
        if not self.fcc111_symbol.value:
            return
        atoms = fcc111(self.fcc111_symbol.value, (1, 1, 4), vacuum=3)
        atoms.pbc = True
        # remove surface tags
        atoms.set_tags(0)
        self.structure = atoms


    @tl.default("structure")
    def _default_structure(self):
        return None
