"""Business-domain service seed for Marketplace Return Case."""

from __future__ import annotations

from typing import Any


ARCHETYPE_PROFILE = {'workflow_profile': {'mode': 'case_flow', 'supports_assignment': True, 'supports_escalation': True}, 'reporting_profile': {'supports_snapshots': True, 'supports_outputs': False}, 'integration_profile': {'external_sync_enabled': False}, 'lifecycle_states': ['requested', 'reviewed', 'approved', 'rejected', 'completed', 'escalated', 'closed', 'archived'], 'is_transactional': False}

CONTRACT = {'title_field': 'title', 'status_field': 'workflow_state', 'reference_field': 'reference_no', 'required_fields': ['title', 'workflow_state'], 'field_purposes': {'workflow_state': 'lifecycle_state', 'related_marketplace_fulfillment_order': 'relation_collection', 'related_listing_binding': 'relation_collection', 'related_refund_case': 'relation_collection', 'related_delivery_exception_case': 'relation_collection'}, 'search_fields': ['title', 'reference_no', 'description', 'case_code', 'source_fulfillment_order_listing', 'return_reason'], 'list_columns': ['title', 'reference_no', 'workflow_state', 'modified'], 'initial_state': 'requested', 'lifecycle_states': ['requested', 'reviewed', 'approved', 'rejected', 'completed', 'escalated', 'closed', 'archived'], 'terminal_states': ['closed', 'archived'], 'records_profile': {'record_class': 'business_record', 'legal_significance': 'standard', 'confidentiality': 'internal', 'official_copy_format': 'pdf', 'evidence_gaps': []}, 'record_contract': {'doc_kind': 'workflow_case', 'supports_attachments': True, 'supports_comments': True, 'supports_activity_log': True, 'supports_assignments': True, 'is_submittable': False, 'supports_submission_snapshot': True, 'supports_official_outputs': True, 'supports_evidence_pack': True, 'supports_signoff': True}, 'submission_snapshot_policy': {'enabled': True, 'trigger_action': 'submit', 'freeze_fields_after_snapshot': True, 'retain_snapshot_history': True, 'snapshot_label_template': '{reference_no}-{workflow_state}', 'trigger_actions': ['submit']}, 'signature_policy': {'enabled': True, 'mode': 'approval', 'required_roles': ['System Manager', 'operations coordinator'], 'reason_required': False, 'counter_signature_required': False}, 'audit_policy': {'track_state_history': True, 'track_action_log': True, 'track_external_refs': True, 'require_reason_for_change': False, 'require_action_comment': False, 'hash_official_outputs': False}, 'records_management': {'retention_policy_ref': 'administration.office_administration.filing_records_management.retention_disposal.retention_policy', 'legal_hold_enabled': False, 'disposition_action': 'archive', 'immutable_after_submit': True, 'official_copy_on_submit': False, 'chain_of_custody_required': False, 'retention_trigger_field': None, 'legal_hold_field': None, 'disposition_actions': ['archive']}, 'legal_hold_policy': {'enabled': False, 'hold_field': None, 'restrict_disposition_while_active': True, 'allow_override_roles': []}, 'official_copy_policy': {'enabled': True, 'format': 'pdf', 'generate_on_submit': False, 'hash_outputs': False, 'include_audit_summary': True, 'include_attachments_index': True, 'trigger_actions': []}, 'evidence_policy': {'required_attachments': [], 'required_references': [], 'required_approvals': [], 'verification_fields': []}, 'chain_of_custody_policy': {'enabled': False, 'custody_event_field': None, 'require_transfer_reason': False, 'require_actor_identity': True}, 'display_runtime_hints': {'doc_key': 'marketplace_return_case', 'supports_related_lookup': True, 'supports_fetch_rules': True, 'workflow_hints': {'relation_context': {'related_docs': ['marketplace_fulfillment_order', 'listing_binding', 'refund_case', 'delivery_exception_case'], 'borrowed_fields': ['source order/listing context from linked docs'], 'inferred_roles': ['account owner', 'operations coordinator', 'case owner']}, 'actors': ['account owner', 'operations coordinator', 'case owner'], 'action_actors': {'create': ['account owner'], 'review': ['operations coordinator'], 'approve': ['operations coordinator'], 'reject': ['operations coordinator'], 'close': ['account owner'], 'archive': ['account owner']}}, 'action_side_effects_file': 'side_effects.json', 'supports_official_copy': True, 'supports_evidence_timeline': True, 'supports_chain_of_custody': False}, 'action_contracts': {'create': {'rule': {'allowed_in_states': ['requested', 'reviewed', 'approved', 'rejected', 'completed', 'escalated'], 'transitions_to': None}, 'requires_action_comment': False, 'requires_reason_for_change': False, 'requires_evidence': False, 'is_disposition_action': False, 'creates_submission_snapshot': False, 'creates_official_copy': False, 'requires_signature': False}, 'review': {'rule': {'allowed_in_states': ['requested', 'reviewed', 'approved', 'rejected', 'completed', 'escalated'], 'transitions_to': 'reviewed'}, 'requires_action_comment': False, 'requires_reason_for_change': False, 'requires_evidence': False, 'is_disposition_action': False, 'creates_submission_snapshot': False, 'creates_official_copy': False, 'requires_signature': False}, 'approve': {'rule': {'allowed_in_states': ['requested', 'reviewed', 'approved', 'rejected', 'completed', 'escalated'], 'transitions_to': 'approved'}, 'requires_action_comment': False, 'requires_reason_for_change': False, 'requires_evidence': False, 'is_disposition_action': False, 'creates_submission_snapshot': False, 'creates_official_copy': False, 'requires_signature': True}, 'reject': {'rule': {'allowed_in_states': ['requested', 'reviewed', 'approved', 'rejected', 'completed', 'escalated'], 'transitions_to': 'rejected'}, 'requires_action_comment': False, 'requires_reason_for_change': False, 'requires_evidence': False, 'is_disposition_action': False, 'creates_submission_snapshot': False, 'creates_official_copy': False, 'requires_signature': False}, 'complete': {'rule': {'allowed_in_states': ['requested', 'reviewed', 'approved', 'rejected', 'completed', 'escalated'], 'transitions_to': None}, 'requires_action_comment': False, 'requires_reason_for_change': False, 'requires_evidence': False, 'is_disposition_action': False, 'creates_submission_snapshot': False, 'creates_official_copy': False, 'requires_signature': False}, 'escalate': {'rule': {'allowed_in_states': ['requested', 'reviewed', 'approved', 'rejected', 'completed', 'escalated'], 'transitions_to': 'escalated'}, 'requires_action_comment': False, 'requires_reason_for_change': False, 'requires_evidence': False, 'is_disposition_action': False, 'creates_submission_snapshot': False, 'creates_official_copy': False, 'requires_signature': False}, 'close': {'rule': {'allowed_in_states': ['requested', 'reviewed', 'approved', 'rejected', 'completed', 'escalated'], 'transitions_to': 'closed'}, 'requires_action_comment': False, 'requires_reason_for_change': False, 'requires_evidence': False, 'is_disposition_action': False, 'creates_submission_snapshot': False, 'creates_official_copy': False, 'requires_signature': False}, 'archive': {'rule': {'allowed_in_states': ['requested', 'reviewed', 'approved', 'rejected', 'completed', 'escalated'], 'transitions_to': 'archived'}, 'requires_action_comment': False, 'requires_reason_for_change': False, 'requires_evidence': False, 'is_disposition_action': True, 'creates_submission_snapshot': False, 'creates_official_copy': False, 'requires_signature': False}}, 'action_targets': {'create': None, 'review': 'reviewed', 'approve': 'approved', 'reject': 'rejected', 'complete': None, 'escalate': 'escalated', 'close': 'closed', 'archive': 'archived'}}

WORKFLOW_HINTS = {'relation_context': {'related_docs': ['marketplace_fulfillment_order', 'listing_binding', 'refund_case', 'delivery_exception_case'], 'borrowed_fields': ['source order/listing context from linked docs'], 'inferred_roles': ['account owner', 'operations coordinator', 'case owner']}, 'actors': ['account owner', 'operations coordinator', 'case owner'], 'action_actors': {'create': ['account owner'], 'review': ['operations coordinator'], 'approve': ['operations coordinator'], 'reject': ['operations coordinator'], 'close': ['account owner'], 'archive': ['account owner']}}

SIDE_EFFECT_HINTS = {'downstream_effects': [], 'related_docs': ['marketplace_fulfillment_order', 'listing_binding', 'refund_case', 'delivery_exception_case'], 'action_targets': {'create': None, 'review': 'reviewed', 'approve': 'approved', 'reject': 'rejected', 'complete': None, 'escalate': 'escalated', 'close': 'closed', 'archive': 'archived'}, 'action_side_effects_file': None}

class DomainService:
    doc_id = "marketplace_return_case"
    archetype = "workflow_case"
    doc_kind = "workflow_case"

    def required_fields(self) -> list[str]:
        return CONTRACT.get("required_fields", [])

    def state_field(self) -> str | None:
        return CONTRACT.get("status_field")

    def default_state(self) -> str | None:
        return CONTRACT.get("initial_state")

    def list_columns(self) -> list[str]:
        return CONTRACT.get("list_columns", [])

    def records_profile(self) -> dict[str, Any]:
        return CONTRACT.get("records_profile", {})

    def record_contract(self) -> dict[str, Any]:
        return CONTRACT.get("record_contract", {})

    def submission_snapshot_policy(self) -> dict[str, Any]:
        return CONTRACT.get("submission_snapshot_policy", {})

    def signature_policy(self) -> dict[str, Any]:
        return CONTRACT.get("signature_policy", {})

    def records_management_policy(self) -> dict[str, Any]:
        return CONTRACT.get("records_management", {})

    def legal_hold_policy(self) -> dict[str, Any]:
        return CONTRACT.get("legal_hold_policy", {})

    def official_copy_policy(self) -> dict[str, Any]:
        return CONTRACT.get("official_copy_policy", {})

    def evidence_policy(self) -> dict[str, Any]:
        return CONTRACT.get("evidence_policy", {})

    def chain_of_custody_policy(self) -> dict[str, Any]:
        return CONTRACT.get("chain_of_custody_policy", {})

    def audit_policy(self) -> dict[str, Any]:
        return CONTRACT.get("audit_policy", {})

    def _requires_reason_for_change(self) -> bool:
        return bool(self.audit_policy().get("require_reason_for_change"))

    def _requires_action_comment(self) -> bool:
        return bool(self.audit_policy().get("require_action_comment"))

    def _is_hold_active(self, context: dict | None = None) -> bool:
        context = context or {}
        legal_hold = context.get("legal_hold")
        if legal_hold is None:
            legal_hold = context.get("has_legal_hold")
        if legal_hold is None:
            legal_hold = (context.get("record_flags") or {}).get("legal_hold")
        return bool(legal_hold)

    def _action_requires_evidence(self, action_id: str) -> bool:
        policy = self.evidence_policy()
        required_actions = set(policy.get("required_for_actions", []))
        return bool(policy.get("required") or action_id in required_actions)

    def validate_action_compliance(
        self,
        action_id: str,
        payload: dict,
        *,
        state: str | None = None,
        context: dict | None = None,
    ) -> dict:
        payload = dict(payload)
        disposition_actions = set(self.records_management_policy().get("disposition_actions", []))
        if action_id in disposition_actions and self._is_hold_active(context):
            raise ValueError("This record is under legal hold and cannot be dispositioned.")
        if self._requires_action_comment() and not payload.get("action_comment"):
            raise ValueError("Action comment is required for this record action.")
        if self._requires_reason_for_change() and not payload.get("reason_for_change"):
            raise ValueError("Reason for change is required for this record action.")
        if self._action_requires_evidence(action_id):
            attachments = payload.get("attachments") or []
            references = payload.get("evidence_refs") or payload.get("related_evidence") or []
            if not attachments and not references:
                raise ValueError("Evidence attachments or references are required for this action.")
        action_contracts = CONTRACT.get("action_contracts", {})
        action_contract = action_contracts.get(action_id, {}) if isinstance(action_contracts, dict) else {}
        if action_contract.get("requires_signature"):
            actor = ((context or {}).get("request") or None)
            user = getattr(actor, "user", None) if actor is not None else None
            is_authenticated = bool(user and getattr(user, "is_authenticated", False))
            if not (payload.get("signature") or payload.get("signature_name") or is_authenticated):
                raise ValueError("A signature or authenticated approver is required for this approval action.")
        return payload

    def validate_invariants(self, payload: dict, *, partial: bool = False) -> dict:
        if partial:
            required_scope = [field for field in self.required_fields() if field in payload]
        else:
            required_scope = self.required_fields()
        missing_fields = [field for field in required_scope if not payload.get(field)]
        if missing_fields:
            raise ValueError(f"Missing required business fields: {', '.join(missing_fields)}")
        state_field = self.state_field()
        allowed_states = set(CONTRACT.get("lifecycle_states", []))
        if state_field and payload.get(state_field) and allowed_states and payload[state_field] not in allowed_states:
            raise ValueError(f"Invalid state '{payload[state_field]}' for {state_field}")
        return payload

    def prepare_create_payload(self, payload: dict, context: dict | None = None) -> dict:
        payload = dict(payload)
        state_field = self.state_field()
        if state_field and not payload.get(state_field) and self.default_state():
            payload[state_field] = self.default_state()
        title_field = CONTRACT.get("title_field")
        reference_field = CONTRACT.get("reference_field")
        if title_field and not payload.get(title_field) and reference_field and payload.get(reference_field):
            payload[title_field] = str(payload[reference_field])
        payload = self.validate_invariants(payload)
        return payload

    def after_create(self, instance, serialized_data: dict, context: dict | None = None) -> dict:
        return serialized_data

    def prepare_update_payload(self, instance, payload: dict, context: dict | None = None) -> dict:
        payload = dict(payload)
        payload = self.validate_invariants(payload, partial=True)
        return payload

    def after_update(self, instance, serialized_data: dict, context: dict | None = None) -> dict:
        return serialized_data

    def after_action(
        self,
        instance,
        action_id: str,
        payload: dict,
        action_result: dict,
        context: dict | None = None,
    ) -> dict:
        payload = self.validate_action_compliance(
            action_id,
            payload,
            state=(context or {}).get("state") if context else None,
            context=context,
        )
        side_effects: list[dict[str, Any]] = []
        request = (context or {}).get("request") if context else None
        user = getattr(request, "user", None) if request is not None else None
        actor_name = payload.get("signature_name") or getattr(user, "username", None)
        side_effects.append(
            {
                "kind": "action_audit_log",
                "action_id": action_id,
                "actor": actor_name,
                "comment": payload.get("action_comment"),
                "reason_for_change": payload.get("reason_for_change"),
                "requires_reason": self._requires_reason_for_change(),
                "requires_comment": self._requires_action_comment(),
            }
        )
        snapshot_policy = self.submission_snapshot_policy()
        snapshot_triggers = set(snapshot_policy.get("trigger_actions", []))
        if snapshot_policy.get("enabled") and action_id in snapshot_triggers:
            side_effects.append(
                {
                    "kind": "submission_snapshot",
                    "action_id": action_id,
                    "mode": snapshot_policy.get("mode"),
                    "immutable": snapshot_policy.get("immutable"),
                    "label_template": snapshot_policy.get("snapshot_label_template"),
                }
            )
        official_copy_policy = self.official_copy_policy()
        if official_copy_policy.get("enabled") and action_id in set(official_copy_policy.get("trigger_actions", [])):
            side_effects.append(
                {
                    "kind": "official_copy",
                    "action_id": action_id,
                    "format": official_copy_policy.get("format"),
                    "hash": "sha1" if official_copy_policy.get("hash_outputs") else None,
                }
            )
        if self.chain_of_custody_policy().get("enabled"):
            side_effects.append(
                {
                    "kind": "chain_of_custody_event",
                    "action_id": action_id,
                    "capture_actor": self.chain_of_custody_policy().get("capture_actor"),
                    "capture_timestamp": self.chain_of_custody_policy().get("capture_timestamp"),
                }
            )
        action_contracts = CONTRACT.get("action_contracts", {})
        action_contract = action_contracts.get(action_id, {}) if isinstance(action_contracts, dict) else {}
        if action_contract.get("requires_signature"):
            signer = actor_name
            side_effects.append(
                {
                    "kind": "approval_signature",
                    "action_id": action_id,
                    "signature_name": signer,
                    "required_roles": self.signature_policy().get("required_roles", []),
                    "reason_required": self.signature_policy().get("reason_required"),
                }
            )
        return {
            "updates": {},
            "side_effects": side_effects,
        }

    def shape_retrieve_data(self, instance, serialized_data: dict, context: dict | None = None) -> dict:
        serialized_data.setdefault("_business_capabilities", self.business_capabilities())
        return serialized_data

    def workflow_objective(self) -> str | None:
        return WORKFLOW_HINTS.get("business_objective")

    def side_effect_hints(self) -> dict:
        return SIDE_EFFECT_HINTS

    def business_capabilities(self) -> dict:
        return {
            **ARCHETYPE_PROFILE,
            "required_fields": self.required_fields(),
            "state_field": self.state_field(),
            "default_state": self.default_state(),
            "is_submittable": bool(self.record_contract().get("is_submittable")),
            "supports_submission_snapshot": bool(self.record_contract().get("supports_submission_snapshot")),
            "supports_official_outputs": bool(self.record_contract().get("supports_official_outputs")),
            "supports_evidence_pack": bool(self.record_contract().get("supports_evidence_pack")),
            "supports_signoff": bool(self.record_contract().get("supports_signoff")),
        }
