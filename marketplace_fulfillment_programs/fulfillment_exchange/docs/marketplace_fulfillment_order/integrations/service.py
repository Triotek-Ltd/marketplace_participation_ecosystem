"""Integration-service seed for marketplace_fulfillment_order."""

from __future__ import annotations


DOC_ID = "marketplace_fulfillment_order"
INTEGRATION_RULES = {'external_refs': [{'field_id': 'source_reference', 'kind': 'source', 'label': 'Source Reference'}, {'field_id': 'external_reference', 'kind': 'source', 'label': 'External Reference'}], 'sync_rules': []}

class IntegrationService:
    def sync_rules(self) -> list:
        return INTEGRATION_RULES.get("sync_rules", [])

    def integration_profile(self) -> dict:
        return {'external_sync_enabled': True, 'tracks_external_refs': True}
