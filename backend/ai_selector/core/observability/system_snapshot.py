"""
System Snapshot

Stage24 Production Observability
"""


from datetime import datetime


class SystemSnapshot:

    def __init__(self):
        self.components = {}

        self.created_at = None


    def update(
        self,
        name: str,
        data
    ):

        self.components[name] = data


    def generate(self):

        self.created_at = datetime.now().isoformat()

        return {
            "components": self.components,
            "created_at": self.created_at,
        }