from core.market.market_snapshot import (
    MarketSnapshot
)


class RealtimeFactorEngine:


    def calculate(
        self,
        snapshot: MarketSnapshot
    ):

        momentum = (
            snapshot.change_pct / 10
        )


        volume_strength = (
            min(
                snapshot.volume / 10000000,
                1
            )
        )


        trend = (
            max(
                momentum,
                0
            )
        )


        return {

            "momentum": round(
                momentum,
                4
            ),

            "volume_strength": round(
                volume_strength,
                4
            ),

            "trend": round(
                trend,
                4
            )
        }