"""Action handler seed for seller_onboarding_case:reject."""

from __future__ import annotations


DOC_ID = "seller_onboarding_case"
ACTION_ID = "reject"
ACTION_RULE = {'allowed_in_states': ['opened', 'in_review', 'approved', 'rejected'], 'transitions_to': 'rejected'}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'relation_context': {'related_docs': ['marketplace_account', 'listing_binding'], 'borrowed_fields': ['applicant', 'marketplace context from linked account/program refs'], 'inferred_roles': ['case owner']}, 'actors': ['case owner'], 'action_actors': {'create': ['case owner'], 'assign': ['case owner'], 'review': ['case owner'], 'approve': ['case owner'], 'reject': ['case owner'], 'close': ['case owner'], 'archive': ['case owner']}}

def handle_reject(payload: dict, context: dict | None = None) -> dict:
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
