"""Action handler seed for marketplace_return_case:reject."""

from __future__ import annotations

from typing import Any, cast


DOC_ID = "marketplace_return_case"
ACTION_ID = "reject"
ACTION_RULE: dict[str, Any] = {'allowed_in_states': ['requested', 'reviewed', 'approved', 'rejected', 'completed', 'escalated'], 'transitions_to': 'rejected'}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'relation_context': {'related_docs': ['marketplace_fulfillment_order', 'listing_binding', 'refund_case', 'delivery_exception_case'], 'borrowed_fields': ['source order/listing context from linked docs'], 'inferred_roles': ['account owner', 'operations coordinator', 'case owner']}, 'actors': ['account owner', 'operations coordinator', 'case owner'], 'action_actors': {'create': ['account owner'], 'review': ['operations coordinator'], 'approve': ['operations coordinator'], 'reject': ['operations coordinator'], 'close': ['account owner'], 'archive': ['account owner']}}

ACTION_CONTRACT: dict[str, Any] = {'rule': {'allowed_in_states': ['requested', 'reviewed', 'approved', 'rejected', 'completed', 'escalated'], 'transitions_to': 'rejected'}, 'requires_action_comment': False, 'requires_reason_for_change': False, 'requires_evidence': False, 'is_disposition_action': False, 'creates_submission_snapshot': False, 'creates_official_copy': False, 'requires_signature': False}

def handle_reject(payload: dict, context: dict | None = None) -> dict:
    context = context or {}
    next_state = cast(str | None, ACTION_RULE.get("transitions_to"))
    updates = {STATE_FIELD: next_state} if STATE_FIELD and next_state else {}
    return {
        "doc_id": DOC_ID,
        "action_id": ACTION_ID,
        "payload": payload,
        "context": context,
        "allowed_in_states": ACTION_RULE.get("allowed_in_states", []),
        "next_state": next_state,
        "updates": updates,
        "action_contract": ACTION_CONTRACT,
        "workflow_objective": WORKFLOW_HINTS.get("business_objective"),
    }
