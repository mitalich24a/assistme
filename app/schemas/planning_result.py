from dataclasses import dataclass, field


@dataclass
class PlanningResult:
    tasks: list[str] = field(default_factory=list)

    dependencies: dict[str, list[str]] = field(default_factory=dict)

    estimates: dict[str, int] = field(default_factory=dict)