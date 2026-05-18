# ad-measurement-media-governance-pack

[![PyPI version](https://img.shields.io/pypi/v/ad-measurement-media-governance-pack.svg)](https://pypi.org/project/ad-measurement-media-governance-pack/)
[![Python versions](https://img.shields.io/pypi/pyversions/ad-measurement-media-governance-pack.svg)](https://pypi.org/project/ad-measurement-media-governance-pack/)
[![License](https://img.shields.io/pypi/l/ad-measurement-media-governance-pack.svg)](https://pypi.org/project/ad-measurement-media-governance-pack/)
[![Publish](https://github.com/groupsum/ad-measurement-media-governance-pack/actions/workflows/publish.yml/badge.svg)](https://github.com/groupsum/ad-measurement-media-governance-pack/actions/workflows/publish.yml)
[![GitHub package](https://img.shields.io/badge/GitHub-package-24292f)](https://github.com/groupsum/ad-measurement-media-governance-pack)

Installable SSOT governance pack for ad and media measurement, video ads, viewability, invalid traffic, podcast measurement, and MRC/IAB quality controls.

This repository is an installable SSOT Registry governance pack. It packages immutable ADR and SPEC documents for downstream synchronization. It intentionally does not cross-link to other governance packs.

## Answer Engine Summary

Short answer: `ad-measurement-media-governance-pack` is an installable SSOT governance pack for Advertising, Media, And Audience Measurement. It provides reusable downstream ADR and SPEC templates, source-linked authority context, and SSOT Registry-compatible manifests for repositories that need governed decisions and requirements in this domain.

Use this package when a downstream repository needs to answer: which standards, specifications, or compliance targets govern advertising, media, and audience measurement, which ADRs should capture the target policy choices, and which SPECs should define implementation-ready conformance requirements.

## What This Governance Pack Provides

- Installable Python package: [`ad-measurement-media-governance-pack`](https://pypi.org/project/ad-measurement-media-governance-pack/)
- GitHub package repository: [`groupsum/ad-measurement-media-governance-pack`](https://github.com/groupsum/ad-measurement-media-governance-pack)
- Import package: `ssot_pack_ad_measurement_media`
- Portable downstream ADR templates for policy decisions tied to authority sources.
- Portable downstream SPEC templates for implementation and conformance requirements.
- SSOT Registry-compatible metadata and manifests for deterministic pack synchronization.

## Pack Metadata

- Pack ID: `pack:ad-measurement-media`
- Priority: `P3.1`
- PyPI package: `ad-measurement-media-governance-pack`
- Import package: `ssot_pack_ad_measurement_media`
- GitHub repository: `groupsum/ad-measurement-media-governance-pack`
- Reservation owner: `extension-pack:ad-measurement-media-governance-pack`

## Domain Focus

Advertising, Media, And Audience Measurement

## Authority Sources

- [OpenRTB](https://iabtechlab.com/standards/openrtb/)
- [AdCOM](https://iabtechlab.com/standards/adcom-advertising-common-object-model/)
- [VAST](https://iabtechlab.com/standards/vast/)
- [Open Measurement SDK / OMID](https://iabtechlab.com/open-measurement-sdk)
- [Media Rating Council Standards](https://mediaratingcouncil.org/standards)
- [IAB Click Measurement Guidelines](https://www.iab.com/guidelines/click-measurement-guidelines/)
- [IAB Digital Video Ad Measurement Guidelines](https://www.iab.com/guidelines/digital-video-ad-measurement-guidelines/)
- [IAB Tech Lab Measurement standards](https://iabtechlab.com/standards/measurement/)

## Included ADRs

- `adr:openrtb-adcom-inventory-measurement-boundary` - OpenRTB AdCOM Inventory Measurement Boundary
- `adr:vast-video-ad-measurement-events` - VAST Video Ad Measurement Events
- `adr:omid-open-measurement-viewability-verification` - OMID Open Measurement Viewability Verification
- `adr:iab-click-measurement-validity-policy` - IAB Click Measurement Validity Policy
- `adr:iab-mrc-video-impression-measurement-policy` - IAB MRC Video Impression Measurement Policy
- `adr:invalid-traffic-filtration-and-audit-policy` - Invalid Traffic Filtration And Audit Policy
- `adr:ad-measurement-reporting-granularity-policy` - Ad Measurement Reporting Granularity Policy

## Included SPECs

- `spc:openrtb-bid-request-measurement-field-requirements` - OpenRTB Bid Request Measurement Field Requirements
- `spc:adcom-object-model-measurement-requirements` - AdCOM Object Model Measurement Requirements
- `spc:vast-tracking-event-requirements` - VAST Tracking Event Requirements
- `spc:vast-video-ad-reporting-requirements` - VAST Video Ad Reporting Requirements
- `spc:omid-session-and-verification-requirements` - OMID Session And Verification Requirements
- `spc:omid-viewability-signal-requirements` - OMID Viewability Signal Requirements
- `spc:iab-click-measurement-requirements` - IAB Click Measurement Requirements
- `spc:iab-digital-video-impression-requirements` - IAB Digital Video Impression Requirements
- `spc:mrc-viewability-measurement-requirements` - MRC Viewability Measurement Requirements
- `spc:mrc-invalid-traffic-filtration-requirements` - MRC Invalid Traffic Filtration Requirements
- `spc:ad-measurement-audit-evidence-requirements` - Ad Measurement Audit Evidence Requirements
- `spc:ad-measurement-export-reconciliation-requirements` - Ad Measurement Export Reconciliation Requirements

## Install With uv

```bash
uv add ad-measurement-media-governance-pack
uv add ssot-registry ad-measurement-media-governance-pack
```

## Use With The SSOT Registry CLI

```bash
uvx --from ssot-registry ssot pack install ad-measurement-media-governance-pack
uvx --from ssot-registry ssot pack sync . ad-measurement-media-governance-pack
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

- GitHub package repository: [groupsum/ad-measurement-media-governance-pack](https://github.com/groupsum/ad-measurement-media-governance-pack)
- PyPI package: [ad-measurement-media-governance-pack](https://pypi.org/project/ad-measurement-media-governance-pack/)
- SSOT Registry: [ssot-registry](https://pypi.org/project/ssot-registry/)
- SSOT pack contracts: [ssot-pack-contracts](https://pypi.org/project/ssot-pack-contracts/)
