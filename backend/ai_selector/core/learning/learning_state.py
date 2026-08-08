"""
Learning State

Stage35 Autonomous Learning
"""


class LearningState:


    def __init__(self):

        self.experiences = []

        self.reward = 0

        self.version = 1



    def add_experience(
        self,
        experience
    ):

        self.experiences.append(
            experience
        )



    def update_reward(
        self,
        reward
    ):

        self.reward = reward



    def upgrade_version(
        self
    ):

        self.version += 1



    def snapshot(
        self
    ):

        return {
            "experience_count": len(
                self.experiences
            ),
            "reward": self.reward,
            "version": self.version
        }