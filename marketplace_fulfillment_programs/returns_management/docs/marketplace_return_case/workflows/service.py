"""Workflow service seed for marketplace_return_case."""

from __future__ import annotations


DOC_ID = "marketplace_return_case"
ARCHETYPE = "workflow_case"
INITIAL_STATE = 'requested'
STATES = ['requested', 'reviewed', 'approved', 'rejected', 'completed', 'escalated', 'closed', 'archived']
TERMINAL_STATES = ['closed', 'archived']
ACTION_RULES = {'create': {'allowed_in_states': ['requested', 'reviewed', 'approved', 'rejected', 'completed', 'escalated'], 'transitions_to': None}, 'review': {'allowed_in_states': ['requested', 'reviewed', 'approved', 'rejected', 'completed', 'escalated'], 'transitions_to': 'reviewed'}, 'approve': {'allowed_in_states': ['requested', 'reviewed', 'approved', 'rejected', 'completed', 'escalated'], 'transitions_to': 'approved'}, 'reject': {'allowed_in_states': ['requested', 'reviewed', 'approved', 'rejected', 'completed', 'escalated'], 'transitions_to': 'rejected'}, 'complete': {'allowed_in_states': ['requested', 'reviewed', 'approved', 'rejected', 'completed', 'escalated'], 'transitions_to': None}, 'escalate': {'allowed_in_states': ['requested', 'reviewed', 'approved', 'rejected', 'completed', 'escalated'], 'transitions_to': 'escalated'}, 'close': {'allowed_in_states': ['requested', 'reviewed', 'approved', 'rejected', 'completed', 'escalated'], 'transitions_to': 'closed'}, 'archive': {'allowed_in_states': ['requested', 'reviewed', 'approved', 'rejected', 'completed', 'escalated'], 'transitions_to': 'archived'}}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'relation_context': {'related_docs': ['marketplace_fulfillment_order', 'listing_binding', 'refund_case', 'delivery_exception_case'], 'borrowed_fields': ['source order/listing context from linked docs'], 'inferred_roles': ['account owner', 'operations coordinator', 'case owner']}, 'actors': ['account owner', 'operations coordinator', 'case owner'], 'action_actors': {'create': ['account owner'], 'review': ['operations coordinator'], 'approve': ['operations coordinator'], 'reject': ['operations coordinator'], 'close': ['account owner'], 'archive': ['account owner']}}

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
        return rule.get("transitions_to")

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
        }

    def workflow_profile(self) -> dict:
        return {'mode': 'case_flow', 'supports_assignment': True, 'supports_escalation': True}
