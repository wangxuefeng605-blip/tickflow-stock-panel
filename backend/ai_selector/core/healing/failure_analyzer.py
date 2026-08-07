"""
Runtime Failure Analyzer

Stage26 Self-Healing Intelligence
"""


class FailureAnalyzer:

    def analyze(self, errors):

        results = []

        for error in errors:

            message = (
                error.get(
                    "error",
                    ""
                )
                .lower()
            )

            component = error.get(
                "component",
                "unknown"
            )


            failure_type = (
                self.classify(
                    message
                )
            )


            results.append(
                {
                    "component": component,
                    "type": failure_type,
                    "severity": self.severity(
                        failure_type
                    ),
                    "action": self.action(
                        failure_type
                    )
                }
            )

        return results


    def classify(self, message):

        if "timeout" in message:
            return "TIMEOUT"

        if (
            "connection"
            in message
        ):
            return "NETWORK_ERROR"


        if (
            "data"
            in message
            or "parse"
            in message
        ):
            return "DATA_ERROR"


        return "UNKNOWN_ERROR"



    def severity(self, failure_type):

        mapping = {

            "TIMEOUT":
                "MEDIUM",

            "NETWORK_ERROR":
                "HIGH",

            "DATA_ERROR":
                "HIGH",

            "UNKNOWN_ERROR":
                "LOW",
        }

        return mapping.get(
            failure_type,
            "LOW"
        )



    def action(self, failure_type):

        mapping = {

            "TIMEOUT":
                "RETRY",

            "NETWORK_ERROR":
                "RECOVER",

            "DATA_ERROR":
                "REBUILD_CACHE",

            "UNKNOWN_ERROR":
                "RETRY",
        }

        return mapping.get(
            failure_type,
            "RETRY"
        )