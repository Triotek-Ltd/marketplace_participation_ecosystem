"""Doc runtime hooks for seller_onboarding_case."""

class DocRuntime:
    doc_key = "seller_onboarding_case"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'assign', 'review', 'approve', 'reject', 'close', 'archive']
