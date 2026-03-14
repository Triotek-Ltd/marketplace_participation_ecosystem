"""Doc runtime hooks for listing_binding."""

class DocRuntime:
    doc_key = "listing_binding"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'sync', 'activate', 'suspend', 'delist', 'archive']
