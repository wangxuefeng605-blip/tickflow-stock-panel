class RebalanceEngine:


    def rebalance(
        self,
        current,
        target
    ):

        orders = []


        current_codes = set(
            current.keys()
        )

        target_codes = set(
            target.keys()
        )


        # 新增仓位
        for code in target_codes - current_codes:

            orders.append({

                "code": code,

                "action": "BUY",

                "qty": target[code]

            })


        # 清理仓位
        for code in current_codes - target_codes:

            orders.append({

                "code": code,

                "action": "SELL",

                "qty": current[code]

            })


        return orders