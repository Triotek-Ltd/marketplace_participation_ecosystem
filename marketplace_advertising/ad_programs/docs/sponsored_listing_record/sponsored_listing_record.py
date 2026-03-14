"""Doc runtime hooks for sponsored_listing_record."""

class DocRuntime:
    doc_key = "sponsored_listing_record"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'activate', 'pause', 'end', 'archive']
