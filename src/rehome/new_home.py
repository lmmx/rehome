from dataclasses import dataclass, field

__all__ = ["Rehome"]

@dataclass
class Rehome:
    colocate: list[str] = field(default_factory=list)
