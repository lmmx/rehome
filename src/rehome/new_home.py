from dataclasses import dataclass, field
from pathlib import Path

__all__ = ["Rehome"]


@dataclass
class Rehome:
    target: Path
    protect: list[str] = field(default_factory=list)
    group: list[str] = field(default_factory=list)
    debug: bool = False

    def __post_init__(self) -> None:
        assert self.target_path.exists(), f"Target {self.target_path} doesn't exist"

    @property
    def target_path(self) -> Path:
        return self.target.resolve()

    @property
    def dir(self) -> Path:
        return self.target_path.parent

    @property
    def name_groups(self) -> list[list[str]]:
        """
        Names which should be kept together
        """
        return [c.split() for c in self.group]
