from dataclasses import dataclass


@dataclass
class OrchestratorDependencies:

    ranking: object

    decision: object

    strategy: object

    execution: object