from .setting import Setting
from .workchain import workchain_and_builder
from .result import Result
from aiidalab_qe.common.panel import OutlinePanel


class EosOutline(OutlinePanel):
    title = "Equation of State (EOS)"


eos ={
"outline": EosOutline,
"setting": Setting,
"workchain": workchain_and_builder,
"result": Result,
}
