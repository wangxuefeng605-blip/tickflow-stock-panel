"""
Performance Analyzer

Stage24 Production Observability
"""


class PerformanceAnalyzer:

    def analyze(
        self,
        metrics
    ):

        issues = []

        if metrics.get(
            "scanner_latency",
            0
        ) > 5:

            issues.append(
                "scanner_slow"
            )


        if metrics.get(
            "error_count",
            0
        ) > 0:

            issues.append(
                "runtime_error"
            )


        score = 1.0

        score -= (
            len(issues)
            * 0.2
        )

        if score >= 0.8:
            status = "GOOD"
        elif score >= 0.5:
            status = "WARNING"
        else:
            status = "BAD"


        return {
            "performance": status,
            "score": score,
            "issues": issues,
        }