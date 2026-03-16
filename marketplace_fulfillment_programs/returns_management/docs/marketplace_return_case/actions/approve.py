"""Action handler seed for marketplace_return_case:approve."""

from __future__ import annotations


DOC_ID = "marketplace_return_case"
ACTION_ID = "approve"
ACTION_RULE = {'allowed_in_states': ['requested', 'reviewed', 'approved', 'rejected', 'completed', 'escalated'], 'transitions_to': 'approved'}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'relation_context': {'related_docs': ['marketplace_fulfillment_order', 'listing_binding', 'refund_case', 'delivery_exception_case'], 'borrowed_fields': ['source order/listing context from linked docs'], 'inferred_roles': ['account owner', 'operations coordinator', 'case owner']}, 'actors': ['account owner', 'operations coordinator', 'case owner'], 'action_actors': {'create': ['account owner'], 'review': ['operations coordinator'], 'approve': ['operations coordinator'], 'reject': ['operations coordinator'], 'close': ['account owner'], 'archive': ['account owner']}}

def handle_approve(payload: dict, context: dict | None = None) -> dict:
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
