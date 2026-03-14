"""Action registry seed for marketplace_fulfillment_order."""

from __future__ import annotations


DOC_ID = "marketplace_fulfillment_order"
ALLOWED_ACTIONS = ['create', 'transmit', 'accept', 'fulfill', 'flag_exception', 'close', 'archive']
ACTION_RULES = {'create': {'allowed_in_states': ['draft', 'transmitted', 'accepted', 'fulfilled', 'exception'], 'transitions_to': None}, 'transmit': {'allowed_in_states': ['draft', 'transmitted', 'accepted', 'fulfilled', 'exception'], 'transitions_to': None}, 'accept': {'allowed_in_states': ['draft', 'transmitted', 'accepted', 'fulfilled', 'exception'], 'transitions_to': None}, 'fulfill': {'allowed_in_states': ['draft', 'transmitted', 'accepted', 'fulfilled', 'exception'], 'transitions_to': None}, 'flag_exception': {'allowed_in_states': ['draft', 'transmitted', 'accepted', 'fulfilled', 'exception'], 'transitions_to': None}, 'close': {'allowed_in_states': ['draft', 'transmitted', 'accepted', 'fulfilled', 'exception'], 'transitions_to': 'closed'}, 'archive': {'allowed_in_states': ['draft', 'transmitted', 'accepted', 'fulfilled', 'exception'], 'transitions_to': 'archived'}}

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
