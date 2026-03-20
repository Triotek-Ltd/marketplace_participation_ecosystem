"""Action registry seed for marketplace_account."""

from __future__ import annotations

from typing import Any


DOC_ID = "marketplace_account"
ALLOWED_ACTIONS = ['create', 'activate', 'suspend', 'archive']
ACTION_RULES: dict[str, dict[str, Any]] = {'create': {'allowed_in_states': ['requested', 'approved', 'active', 'suspended'], 'transitions_to': None}, 'activate': {'allowed_in_states': ['requested'], 'transitions_to': 'active'}, 'suspend': {'allowed_in_states': ['requested', 'approved', 'active', 'suspended'], 'transitions_to': None}, 'archive': {'allowed_in_states': ['requested', 'approved', 'active', 'suspended'], 'transitions_to': 'archived'}}

STATE_FIELD = 'workflow_state'

AUDIT_POLICY = {'track_state_history': True, 'track_action_log': True, 'track_external_refs': True, 'require_reason_for_change': False, 'require_action_comment': False, 'hash_official_outputs': False}
EVIDENCE_POLICY = {'required_attachments': [], 'required_references': [], 'required_approvals': [], 'verification_fields': []}
RECORDS_MANAGEMENT = {'retention_policy_ref': 'administration.office_administration.filing_records_management.retention_disposal.retention_policy', 'legal_hold_enabled': False, 'disposition_action': 'archive', 'immutable_after_submit': True, 'official_copy_on_submit': False, 'chain_of_custody_required': False, 'retention_trigger_field': None, 'legal_hold_field': None, 'disposition_actions': ['archive']}

def get_action_handler_name(action_id: str) -> str:
    return f"handle_{action_id}"

def get_action_module_path(action_id: str) -> str:
    return f"actions/{action_id}.py"

def action_contract(action_id: str) -> dict:
    return {
        "state_field": STATE_FIELD,
        "rule": ACTION_RULES.get(action_id, {}),
        "audit_policy": AUDIT_POLICY,
        "evidence_policy": EVIDENCE_POLICY,
        "records_management": RECORDS_MANAGEMENT,
    }
