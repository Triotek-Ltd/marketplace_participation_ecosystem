"""Action registry seed for marketplace_inventory_feed."""

from __future__ import annotations


DOC_ID = "marketplace_inventory_feed"
ALLOWED_ACTIONS = ['record', 'transmit', 'review', 'archive']
ACTION_RULES = {'record': {'allowed_in_states': ['created', 'transmitted', 'accepted', 'failed'], 'transitions_to': None}, 'transmit': {'allowed_in_states': ['created', 'transmitted', 'accepted', 'failed'], 'transitions_to': None}, 'review': {'allowed_in_states': ['created', 'transmitted', 'accepted', 'failed'], 'transitions_to': None}, 'archive': {'allowed_in_states': ['created', 'transmitted', 'accepted', 'failed'], 'transitions_to': 'archived'}}

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
