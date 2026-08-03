class AllocationOptimizer:


    def allocate(
        self,
        strategy
    ):

        total = sum(
            strategy.values()
        )

        if total == 0:
            return 0

        return min(
            1.0,
            total
        )