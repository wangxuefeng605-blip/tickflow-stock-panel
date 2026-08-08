from core.policy.policy_state import PolicyState


class PolicyRegistry:

    def __init__(self):

        self.policies = {}


    def register(self, policy):

        self.policies[
            policy.version
        ] = policy


    def get(self, version):

        return self.policies.get(version)


    def list(self):

        return list(
            self.policies.values()
        )


    def get_active(self):

        for policy in self.policies.values():

            if policy.active:
                return policy

        return None