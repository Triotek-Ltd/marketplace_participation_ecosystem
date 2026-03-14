"""Doc runtime hooks for marketplace_account."""

class DocRuntime:
    doc_key = "marketplace_account"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'activate', 'suspend', 'archive']
