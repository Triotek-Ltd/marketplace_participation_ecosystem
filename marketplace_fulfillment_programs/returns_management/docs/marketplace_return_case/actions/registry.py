"""Action registry seed for marketplace_return_case."""

from __future__ import annotations


DOC_ID = "marketplace_return_case"
ALLOWED_ACTIONS = ['create', 'review', 'approve', 'reject', 'complete', 'escalate', 'close', 'archive']
ACTION_RULES = {'create': {'allowed_in_states': ['requested', 'reviewed', 'approved', 'rejected', 'completed', 'escalated'], 'transitions_to': None}, 'review': {'allowed_in_states': ['requested', 'reviewed', 'approved', 'rejected', 'completed', 'escalated'], 'transitions_to': 'reviewed'}, 'approve': {'allowed_in_states': ['requested', 'reviewed', 'approved', 'rejected', 'completed', 'escalated'], 'transitions_to': 'approved'}, 'reject': {'allowed_in_states': ['requested', 'reviewed', 'approved', 'rejected', 'completed', 'escalated'], 'transitions_to': 'rejected'}, 'complete': {'allowed_in_states': ['requested', 'reviewed', 'approved', 'rejected', 'completed', 'escalated'], 'transitions_to': None}, 'escalate': {'allowed_in_states': ['requested', 'reviewed', 'approved', 'rejected', 'completed', 'escalated'], 'transitions_to': 'escalated'}, 'close': {'allowed_in_states': ['requested', 'reviewed', 'approved', 'rejected', 'completed', 'escalated'], 'transitions_to': 'closed'}, 'archive': {'allowed_in_states': ['requested', 'reviewed', 'approved', 'rejected', 'completed', 'escalated'], 'transitions_to': 'archived'}}

STATE_FIELD = 'workflow_state'

def get_action_handler_name(action_id: str) -> str:
    return f"handle_{action_id}"

def get_action_module_path(action_id: str) -> str:
    return f"actions/{action_id}.py"

def action_contract(action_id: str) -> dict:
    return {
        "state_field": STATE_FIELD,
        "rule": ACTION_RULES.get(action_id, {}),
    }
