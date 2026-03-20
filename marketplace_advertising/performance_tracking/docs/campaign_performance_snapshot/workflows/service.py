"""Workflow service seed for campaign_performance_snapshot."""

from __future__ import annotations

from typing import Any, cast


DOC_ID = "campaign_performance_snapshot"
ARCHETYPE = "ledger"
INITIAL_STATE = 'created'
STATES = ['created', 'reviewed', 'archived']
TERMINAL_STATES = ['archived']
ACTION_RULES: dict[str, dict[str, Any]] = {'record': {'allowed_in_states': ['created', 'reviewed'], 'transitions_to': None}, 'review': {'allowed_in_states': ['created', 'reviewed'], 'transitions_to': 'reviewed'}, 'archive': {'allowed_in_states': ['created', 'reviewed'], 'transitions_to': 'archived'}}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {}

RECORD_CONTRACT = {'doc_kind': 'ledger', 'supports_attachments': True, 'supports_comments': True, 'supports_activity_log': True, 'supports_assignments': True, 'is_submittable': False, 'supports_submission_snapshot': True, 'supports_official_outputs': True, 'supports_evidence_pack': True, 'supports_signoff': False}
SNAPSHOT_POLICY = {'enabled': True, 'trigger_action': 'submit', 'freeze_fields_after_snapshot': True, 'retain_snapshot_history': True, 'snapshot_label_template': '{reference_no}-{workflow_state}', 'trigger_actions': ['submit']}
RECORDS_MANAGEMENT = {'retention_policy_ref': 'administration.office_administration.filing_records_management.retention_disposal.retention_policy', 'legal_hold_enabled': False, 'disposition_action': 'archive', 'immutable_after_submit': True, 'official_copy_on_submit': False, 'chain_of_custody_required': False, 'retention_trigger_field': None, 'legal_hold_field': None, 'disposition_actions': ['archive']}

class WorkflowService:
    def allowed_actions_for_state(self, state: str | None) -> list[str]:
        if not state:
            return list(ACTION_RULES.keys())
        allowed = []
        for action_id, rule in ACTION_RULES.items():
            states = rule.get("allowed_in_states") or []
            if not states or state in states:
                allowed.append(action_id)
        return allowed

    def is_action_allowed(self, action_id: str, state: str | None) -> bool:
        return action_id in self.allowed_actions_for_state(state)

    def next_state_for(self, action_id: str) -> str | None:
        rule = ACTION_RULES.get(action_id, {})
        return cast(str | None, rule.get("transitions_to"))

    def apply_action(self, action_id: str, state: str | None) -> dict:
        if not self.is_action_allowed(action_id, state):
            raise ValueError(f"Action '{action_id}' is not allowed in state '{state}'")
        next_state = self.next_state_for(action_id)
        updates = {STATE_FIELD: next_state} if STATE_FIELD and next_state else {}
        return {
            "action_id": action_id,
            "current_state": state,
            "next_state": next_state,
            "updates": updates,
        }

    def is_terminal(self, state: str | None) -> bool:
        return bool(state and state in TERMINAL_STATES)

    def workflow_summary(self) -> dict:
        return {
            "initial_state": INITIAL_STATE,
            "states": STATES,
            "terminal_states": TERMINAL_STATES,
            "business_objective": WORKFLOW_HINTS.get("business_objective"),
            "ordered_steps": WORKFLOW_HINTS.get("ordered_steps", []),
            "is_submittable": bool(RECORD_CONTRACT.get("is_submittable")),
            "submission_actions": SNAPSHOT_POLICY.get("trigger_actions", []),
            "disposition_actions": RECORDS_MANAGEMENT.get("disposition_actions", []),
        }

    def workflow_profile(self) -> dict:
        return {'mode': 'posting_flow', 'supports_reconciliation': True}
