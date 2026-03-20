"""Action handler seed for marketplace_campaign:close."""

from __future__ import annotations

from typing import Any, cast


DOC_ID = "marketplace_campaign"
ACTION_ID = "close"
ACTION_RULE: dict[str, Any] = {'allowed_in_states': ['draft', 'approved', 'active', 'paused', 'completed'], 'transitions_to': None}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'relation_context': {'related_docs': ['marketplace_account', 'sponsored_listing_record', 'campaign_performance_snapshot'], 'borrowed_field_context': ['account', 'listing context from marketplace-account bindings'], 'inferred_roles': ['Finance Officer']}, 'actors': ['Finance Officer'], 'action_actors': {'create': ['Finance Officer'], 'review': ['Finance Officer'], 'approve': ['Finance Officer'], 'launch': ['Finance Officer'], 'pause': ['Finance Officer'], 'close': ['Finance Officer'], 'archive': ['Finance Officer']}}

ACTION_CONTRACT: dict[str, Any] = {'rule': {'allowed_in_states': ['draft', 'approved', 'active', 'paused', 'completed'], 'transitions_to': None}, 'requires_action_comment': False, 'requires_reason_for_change': False, 'requires_evidence': False, 'is_disposition_action': False, 'creates_submission_snapshot': False, 'creates_official_copy': False, 'requires_signature': False}

def handle_close(payload: dict, context: dict | None = None) -> dict:
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
