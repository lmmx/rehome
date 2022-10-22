from dataclasses import KW_ONLY, dataclass, field
from pathlib import Path

__all__ = ["Rehome"]


@dataclass
class Rehome:
    path: Path
    _: KW_ONLY
    colocate: list[str] = field(default_factory=list)
    debug: bool = False

    @property
    def name_groups(self) -> list[list[str]]:
        """
        Names which should be kept together
        """
        return [c.split() for c in self.colocate]
