"""Action handler seed for marketplace_fulfillment_order:flag_exception."""

from __future__ import annotations


DOC_ID = "marketplace_fulfillment_order"
ACTION_ID = "flag_exception"
ACTION_RULE = {'allowed_in_states': ['draft', 'transmitted', 'accepted', 'fulfilled', 'exception'], 'transitions_to': None}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'relation_context': {'related_docs': ['marketplace_account', 'marketplace_inventory_feed', 'marketplace_return_case', 'external_fulfillment_order'], 'borrowed_fields': ['order/account context from linked marketplace or operations docs'], 'inferred_roles': ['account owner', 'operations coordinator', 'case owner']}, 'actors': ['account owner', 'operations coordinator', 'case owner'], 'action_actors': {'create': ['account owner'], 'close': ['account owner'], 'archive': ['account owner']}}

def handle_flag_exception(payload: dict, context: dict | None = None) -> dict:
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
