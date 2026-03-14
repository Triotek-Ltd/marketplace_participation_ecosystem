"""Doc runtime hooks for campaign_performance_snapshot."""

class DocRuntime:
    doc_key = "campaign_performance_snapshot"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['record', 'review', 'archive']
