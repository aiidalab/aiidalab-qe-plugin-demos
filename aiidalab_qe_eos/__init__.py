from .setting import Setting
from .workchain import workchain_and_builder
from .result import Result
from .structure_importer import StructureImporter
from .structure_editor import StructureEditor
from aiidalab_qe.common.panel import OutlinePanel


class EosOutline(OutlinePanel):
    title = "Equation of State (EOS)"


eos ={
"outline": EosOutline,
"importer": StructureImporter,
"editor": StructureEditor,
"setting": Setting,
"workchain": workchain_and_builder,
"result": Result,
}
