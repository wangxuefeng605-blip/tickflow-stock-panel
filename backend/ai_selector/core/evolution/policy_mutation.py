class PolicyMutation:

    def mutate(self, policy):

        new_policy = type(policy)(
            version=f"{policy.version}-mutated",
            score=policy.score
        )

        return new_policy