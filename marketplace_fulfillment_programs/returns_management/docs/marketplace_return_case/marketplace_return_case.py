"""Doc runtime hooks for marketplace_return_case."""

class DocRuntime:
    doc_key = "marketplace_return_case"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'review', 'approve', 'reject', 'complete', 'escalate', 'close', 'archive']
