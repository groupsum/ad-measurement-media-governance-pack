"""Inspect the installed pack identity."""

from ssot_pack_ad_measurement_media import load_pack_metadata

metadata = load_pack_metadata()
assert metadata["origin"]["id"] == "pack:ad-measurement-media"
print(metadata["origin"]["id"])
