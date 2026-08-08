class PolicySelector:

    def select(self, policies):

        if not policies:
            return None

        return max(
            policies,
            key=lambda p: p.score
        )