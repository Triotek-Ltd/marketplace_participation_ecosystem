"""Action handler seed for marketplace_inventory_feed:transmit."""

from __future__ import annotations


DOC_ID = "marketplace_inventory_feed"
ACTION_ID = "transmit"
ACTION_RULE = {'allowed_in_states': ['created', 'transmitted', 'accepted', 'failed'], 'transitions_to': None}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {}

def handle_transmit(payload: dict, context: dict | None = None) -> dict:
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
