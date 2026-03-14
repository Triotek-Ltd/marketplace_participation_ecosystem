"""Action registry seed for marketplace_account."""

from __future__ import annotations


DOC_ID = "marketplace_account"
ALLOWED_ACTIONS = ['create', 'activate', 'suspend', 'archive']
ACTION_RULES = {'create': {'allowed_in_states': ['requested', 'approved', 'active', 'suspended'], 'transitions_to': None}, 'activate': {'allowed_in_states': ['requested'], 'transitions_to': 'active'}, 'suspend': {'allowed_in_states': ['requested', 'approved', 'active', 'suspended'], 'transitions_to': None}, 'archive': {'allowed_in_states': ['requested', 'approved', 'active', 'suspended'], 'transitions_to': 'archived'}}

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
