"""Report-service seed for marketplace_inventory_feed."""

from __future__ import annotations


DOC_ID = "marketplace_inventory_feed"
DOC_KIND = "ledger"

LIST_COLUMNS = ['title', 'reference_no', 'posting_date', 'workflow_state']

class ReportService:
    def supports_reporting_hooks(self) -> bool:
        return DOC_KIND in {"transaction", "ledger", "workflow_case"}

    def default_dimensions(self) -> list[str]:
        return LIST_COLUMNS

    def reporting_profile(self) -> dict:
        return {'supports_snapshots': True, 'supports_outputs': True}
