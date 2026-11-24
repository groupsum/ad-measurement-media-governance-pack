"""Find a specification and its downstream path in the installed manifest."""

from ssot_pack_ad_measurement_media import load_document_manifest

specification = next(
    row for row in load_document_manifest("spec")
    if row["id"] == "spc:openrtb-bid-request-measurement-field-requirements"
)
assert specification["target_path"] == ".ssot/specs/SPEC-2001-openrtb-bid-request-measurement-field-requirements.yaml"
