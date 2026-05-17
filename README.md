# ssot-pack-ad-measurement-media

Installable SSOT governance pack for ad and media measurement, video ads, viewability, invalid traffic, podcast measurement, and MRC/IAB quality controls.

This repository is an installable SSOT Registry governance pack. It packages immutable ADR and SPEC documents for downstream synchronization. It intentionally does not cross-link to other governance packs.

## Pack Metadata

- Pack ID: `pack:ad-measurement-media`
- Priority: `P3.1`
- PyPI package: `ssot-pack-ad-measurement-media`
- Import package: `ssot_pack_ad_measurement_media`
- GitHub repository: `groupsum/ad-measurement-media-governance-pack`
- Reservation owner: `extension-pack:ssot-pack-ad-measurement-media`

## Domain Focus

Advertising, Media, And Audience Measurement

## Authority Sources

- OpenRTB
- AdCOM
- VAST
- Open Measurement SDK / OMID
- Media Rating Council Standards
- IAB Click Measurement Guidelines
- IAB Digital Video Ad Measurement Guidelines
- IAB Tech Lab Measurement standards

## Included ADRs

- `adr:openrtb-adcom-inventory-measurement-boundary` - OpenRTB AdCOM Inventory Measurement Boundary
- `adr:vast-video-ad-measurement-events` - VAST Video Ad Measurement Events
- `adr:omid-open-measurement-viewability-verification` - OMID Open Measurement Viewability Verification
- `adr:iab-click-measurement-validity-policy` - IAB Click Measurement Validity Policy
- `adr:iab-mrc-video-impression-measurement-policy` - IAB MRC Video Impression Measurement Policy
- `adr:invalid-traffic-filtration-and-audit-policy` - Invalid Traffic Filtration And Audit Policy
- `adr:ad-measurement-reporting-granularity-policy` - Ad Measurement Reporting Granularity Policy

## Included SPECs

- `spc:vast-video-measurement-contract` - VAST Video Measurement Contract
- `spc:omid-viewability-contract` - OMID Viewability Contract
- `spc:iab-click-video-podcast-measurement-contract` - IAB Click Video Podcast Measurement Contract
- `spc:bot-filtering-measurement-contract` - Bot Filtering Measurement Contract

## Install With uv

```bash
uv add ssot-pack-ad-measurement-media
uv add ssot-registry ssot-pack-ad-measurement-media
```

## Use With The SSOT Registry CLI

```bash
uvx --from ssot-registry ssot pack install ssot-pack-ad-measurement-media
uvx --from ssot-registry ssot pack sync . ssot-pack-ad-measurement-media
uv run ssot adr list .
uv run ssot spec list .
```

## Programmatic Usage

```python
from ssot_pack_ad_measurement_media import load_document_manifest

adr_manifest = load_document_manifest("adr")
spec_manifest = load_document_manifest("spec")
```

## Resources

- GitHub repository: https://github.com/groupsum/ad-measurement-media-governance-pack
- PyPI package: https://pypi.org/project/ssot-pack-ad-measurement-media/
- SSOT Registry: https://pypi.org/project/ssot-registry/
