"""Action registry seed for sponsored_listing_record."""

from __future__ import annotations


DOC_ID = "sponsored_listing_record"
ALLOWED_ACTIONS = ['create', 'activate', 'pause', 'end', 'archive']
ACTION_RULES = {'create': {'allowed_in_states': ['draft', 'active', 'paused', 'ended'], 'transitions_to': None}, 'activate': {'allowed_in_states': ['draft'], 'transitions_to': 'active'}, 'pause': {'allowed_in_states': ['draft', 'active', 'paused', 'ended'], 'transitions_to': None}, 'end': {'allowed_in_states': ['draft', 'active', 'paused', 'ended'], 'transitions_to': None}, 'archive': {'allowed_in_states': ['draft', 'active', 'paused', 'ended'], 'transitions_to': 'archived'}}

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
