"""Doc runtime hooks for marketplace_campaign."""

class DocRuntime:
    doc_key = "marketplace_campaign"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'review', 'approve', 'launch', 'pause', 'close', 'archive']
