"""Doc runtime hooks for marketplace_inventory_feed."""

class DocRuntime:
    doc_key = "marketplace_inventory_feed"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['record', 'transmit', 'review', 'archive']
