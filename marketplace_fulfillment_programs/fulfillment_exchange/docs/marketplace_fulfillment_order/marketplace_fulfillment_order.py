"""Doc runtime hooks for marketplace_fulfillment_order."""

class DocRuntime:
    doc_key = "marketplace_fulfillment_order"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'transmit', 'accept', 'fulfill', 'flag_exception', 'close', 'archive']
