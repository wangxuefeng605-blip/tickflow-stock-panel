"""
Experience Collector

Stage35 Autonomous Learning
"""


class ExperienceCollector:


    def __init__(
        self,
        state
    ):

        self.state = state



    def collect(
        self,
        experience
    ):

        self.state.add_experience(
            experience
        )

        return {
            "status": "RECORDED",
            "experience": experience
        }



    def collect_result(
        self,
        decision,
        execution,
        reward
    ):

        experience = {
            "decision": decision,
            "execution": execution,
            "reward": reward
        }

        return self.collect(
            experience
        )