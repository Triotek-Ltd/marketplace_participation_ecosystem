"""Action handler seed for listing_binding:create."""

from __future__ import annotations


DOC_ID = "listing_binding"
ACTION_ID = "create"
ACTION_RULE = {'allowed_in_states': ['draft', 'active', 'suspended', 'delisted'], 'transitions_to': None}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'relation_context': {'related_docs': ['marketplace_account', 'marketplace_fulfillment_order', 'sponsored_listing_record', 'catalog_product'], 'borrowed_fields': ['product', 'catalog context from operations/platform product docs'], 'inferred_roles': ['account owner']}, 'actors': ['account owner'], 'action_actors': {'create': ['account owner'], 'activate': ['account owner'], 'archive': ['account owner']}}

def handle_create(payload: dict, context: dict | None = None) -> dict:
    context = context or {}
    next_state = ACTION_RULE.get("transitions_to")
    updates = {STATE_FIELD: next_state} if STATE_FIELD and next_state else {}
    return {
        "doc_id": DOC_ID,
        "action_id": ACTION_ID,
        "payload": payload,
        "context": context,
        "allowed_in_states": ACTION_RULE.get("allowed_in_states", []),
        "next_state": next_state,
        "updates": updates,
        "workflow_objective": WORKFLOW_HINTS.get("business_objective"),
    }
