# ad-measurement-media-governance-pack

<!-- readme-standards:begin branding -->
<p align="center"><a href="https://github.com/groupsum/readme-standards"><img src="https://raw.githubusercontent.com/groupsum/readme-standards/master/docs/assets/readme-standards.svg" alt="Groupsum README Standards" width="300"></a></p>
<p align="center"><strong>ad-measurement-media-governance-pack</strong></p>
<p align="center">Installable SSOT governance pack for ad and media measurement, video ads, viewability, invalid traffic, podcast measurement, and MRC/IAB quality controls.</p>
<p align="center">
<a href="https://pypi.org/project/ad-measurement-media-governance-pack/"><img alt="pypi: ad-measurement-media-governance-pack" src="https://img.shields.io/pypi/v/ad-measurement-media-governance-pack?labelColor=1E293B&amp;color=1D4ED8"></a>
<a href="https://github.com/groupsum/ad-measurement-media-governance-pack/blob/master/pyproject.toml"><img alt="Source version: 0.2.0.dev1" src="https://img.shields.io/static/v1?label=Source%20version&amp;message=0.2.0.dev1&amp;labelColor=1E293B&amp;color=4338CA"></a>
<a href="https://github.com/groupsum/ad-measurement-media-governance-pack/blob/master/pyproject.toml"><img alt="Python: &gt;=3.10,&lt;3.15" src="https://img.shields.io/static/v1?label=Python&amp;message=%3E%3D3.10%2C%3C3.15&amp;labelColor=1E293B&amp;color=0F766E"></a>
<a href="https://github.com/groupsum/ad-measurement-media-governance-pack/blob/master/pyproject.toml"><img alt="Layer: governance" src="https://img.shields.io/static/v1?label=Layer&amp;message=governance&amp;labelColor=1E293B&amp;color=6D28D9"></a>
<a href="https://github.com/groupsum/ad-measurement-media-governance-pack/blob/master/README.md#lifecycle-and-migration"><img alt="Lifecycle: active" src="https://img.shields.io/static/v1?label=Lifecycle&amp;message=active&amp;labelColor=1E293B&amp;color=166534"></a>
<a href="https://github.com/groupsum/ad-measurement-media-governance-pack/blob/master/LICENSE"><img alt="License: Apache-2.0" src="https://img.shields.io/static/v1?label=License&amp;message=Apache-2.0&amp;labelColor=1E293B&amp;color=86198F"></a>
<a href="https://github.com/groupsum/ad-measurement-media-governance-pack/blob/master/README.md#notices"><img alt="Notice: not required" src="https://img.shields.io/static/v1?label=Notice&amp;message=not%20required&amp;labelColor=1E293B&amp;color=475569"></a>
</p>
<p align="center">
<a href="https://pypi.org/project/ad-measurement-media-governance-pack/"><img alt="Monthly PyPI downloads: ad-measurement-media-governance-pack" src="https://img.shields.io/pypi/dm/ad-measurement-media-governance-pack?labelColor=1E293B&amp;color=0E7490"></a>
<a href="https://github.com/groupsum/ad-measurement-media-governance-pack/blob/master/README.md"><img alt="README hits: ad-measurement-media-governance-pack" src="https://hits.sh/github.com/groupsum/ad-measurement-media-governance-pack/README.md.svg?label=README%20hits&amp;labelColor=1E293B&amp;color=0E7490"></a>
</p>
<p align="center">
<a href="https://github.com/groupsum/ad-measurement-media-governance-pack/actions/workflows/readme-standards.yml"><img alt="README standards: CI gate" src="https://img.shields.io/static/v1?label=README%20standards&amp;message=CI%20gate&amp;labelColor=1E293B&amp;color=1D4ED8"></a>
<a href="https://github.com/groupsum/ad-measurement-media-governance-pack/actions/workflows/readme-standards.yml"><img alt="Tests: package and example checks" src="https://img.shields.io/static/v1?label=Tests&amp;message=package%20and%20example%20checks&amp;labelColor=1E293B&amp;color=0F766E"></a>
<a href="https://github.com/groupsum/ad-measurement-media-governance-pack/blob/master/README.md#certification-status"><img alt="Certification: not certified" src="https://img.shields.io/static/v1?label=Certification&amp;message=not%20certified&amp;labelColor=1E293B&amp;color=92400E"></a>
<a href="https://github.com/groupsum/ad-measurement-media-governance-pack/blob/master/docs/governance/pack-authoring-guide.md"><img alt="Governance: pack governance" src="https://img.shields.io/static/v1?label=Governance&amp;message=pack%20governance&amp;labelColor=1E293B&amp;color=4338CA"></a>
<a href="https://github.com/groupsum/ad-measurement-media-governance-pack/actions/workflows/readme-standards.yml"><img alt="Evidence: README and wheel checks" src="https://img.shields.io/static/v1?label=Evidence&amp;message=README%20and%20wheel%20checks&amp;labelColor=1E293B&amp;color=6D28D9"></a>
</p>
<p align="center"><a href="#overview">Overview</a> · <a href="#installation">Installation</a> · <a href="#quick-start">Quick Start</a> · <a href="#usage">Usage</a> · <a href="#public-api-and-import-surfaces">API</a> · <a href="#contributing">Contributing</a> · <a href="#governance">Governance</a> · <a href="#license">License</a></p>
<!-- readme-standards:end branding -->

---

## Overview

### Summary

Installable SSOT governance pack for ad and media measurement, video ads, viewability, invalid traffic, podcast measurement, and MRC/IAB quality controls.

### Why This Package

Use this package when a downstream repository needs to answer: which standards, specifications, or compliance targets govern advertising, media, and audience measurement, which ADRs should capture the target policy choices, and which SPECs should define implementation-ready conformance requirements.

### When to Use

Use this pack when a downstream SSOT Registry needs reusable decisions and requirements for Advertising, Media, And Audience Measurement.

### Features

**Included ADRs**

- [`adr:openrtb-adcom-inventory-measurement-boundary`](https://github.com/groupsum/ad-measurement-media-governance-pack/blob/master/src/ssot_pack_ad_measurement_media/templates/adr/ADR-1001-openrtb-adcom-inventory-measurement-boundary.yaml) — OpenRTB AdCOM Inventory Measurement Boundary
- [`adr:vast-video-ad-measurement-events`](https://github.com/groupsum/ad-measurement-media-governance-pack/blob/master/src/ssot_pack_ad_measurement_media/templates/adr/ADR-1002-vast-video-ad-measurement-events.yaml) — VAST Video Ad Measurement Events
- [`adr:omid-open-measurement-viewability-verification`](https://github.com/groupsum/ad-measurement-media-governance-pack/blob/master/src/ssot_pack_ad_measurement_media/templates/adr/ADR-1003-omid-open-measurement-viewability-verification.yaml) — OMID Open Measurement Viewability Verification
- [`adr:iab-click-measurement-validity-policy`](https://github.com/groupsum/ad-measurement-media-governance-pack/blob/master/src/ssot_pack_ad_measurement_media/templates/adr/ADR-1004-iab-click-measurement-validity-policy.yaml) — IAB Click Measurement Validity Policy
- [`adr:iab-mrc-video-impression-measurement-policy`](https://github.com/groupsum/ad-measurement-media-governance-pack/blob/master/src/ssot_pack_ad_measurement_media/templates/adr/ADR-1005-iab-mrc-video-impression-measurement-policy.yaml) — IAB MRC Video Impression Measurement Policy
- [`adr:invalid-traffic-filtration-and-audit-policy`](https://github.com/groupsum/ad-measurement-media-governance-pack/blob/master/src/ssot_pack_ad_measurement_media/templates/adr/ADR-1006-invalid-traffic-filtration-and-audit-policy.yaml) — Invalid Traffic Filtration And Audit Policy
- [`adr:ad-measurement-reporting-granularity-policy`](https://github.com/groupsum/ad-measurement-media-governance-pack/blob/master/src/ssot_pack_ad_measurement_media/templates/adr/ADR-1007-ad-measurement-reporting-granularity-policy.yaml) — Ad Measurement Reporting Granularity Policy
- [`adr:click-video-and-viewability-measurement-are-owned-here`](https://github.com/groupsum/ad-measurement-media-governance-pack/blob/master/src/ssot_pack_ad_measurement_media/templates/adr/ADR-1008-click-video-and-viewability-measurement-are-owned-here.yaml) — Click Video And Viewability Measurement Are Owned Here

**Included SPECs**

- [`spc:openrtb-bid-request-measurement-field-requirements`](https://github.com/groupsum/ad-measurement-media-governance-pack/blob/master/src/ssot_pack_ad_measurement_media/templates/specs/SPEC-2001-openrtb-bid-request-measurement-field-requirements.yaml) — OpenRTB Bid Request Measurement Field Requirements
- [`spc:adcom-object-model-measurement-requirements`](https://github.com/groupsum/ad-measurement-media-governance-pack/blob/master/src/ssot_pack_ad_measurement_media/templates/specs/SPEC-2002-adcom-object-model-measurement-requirements.yaml) — AdCOM Object Model Measurement Requirements
- [`spc:vast-tracking-event-requirements`](https://github.com/groupsum/ad-measurement-media-governance-pack/blob/master/src/ssot_pack_ad_measurement_media/templates/specs/SPEC-2003-vast-tracking-event-requirements.yaml) — VAST Tracking Event Requirements
- [`spc:vast-video-ad-reporting-requirements`](https://github.com/groupsum/ad-measurement-media-governance-pack/blob/master/src/ssot_pack_ad_measurement_media/templates/specs/SPEC-2004-vast-video-ad-reporting-requirements.yaml) — VAST Video Ad Reporting Requirements
- [`spc:omid-session-and-verification-requirements`](https://github.com/groupsum/ad-measurement-media-governance-pack/blob/master/src/ssot_pack_ad_measurement_media/templates/specs/SPEC-2005-omid-session-and-verification-requirements.yaml) — OMID Session And Verification Requirements
- [`spc:omid-viewability-signal-requirements`](https://github.com/groupsum/ad-measurement-media-governance-pack/blob/master/src/ssot_pack_ad_measurement_media/templates/specs/SPEC-2006-omid-viewability-signal-requirements.yaml) — OMID Viewability Signal Requirements
- [`spc:iab-click-measurement-requirements`](https://github.com/groupsum/ad-measurement-media-governance-pack/blob/master/src/ssot_pack_ad_measurement_media/templates/specs/SPEC-2007-iab-click-measurement-requirements.yaml) — IAB Click Measurement Requirements
- [`spc:iab-digital-video-impression-requirements`](https://github.com/groupsum/ad-measurement-media-governance-pack/blob/master/src/ssot_pack_ad_measurement_media/templates/specs/SPEC-2008-iab-digital-video-impression-requirements.yaml) — IAB Digital Video Impression Requirements
- [`spc:mrc-viewability-measurement-requirements`](https://github.com/groupsum/ad-measurement-media-governance-pack/blob/master/src/ssot_pack_ad_measurement_media/templates/specs/SPEC-2009-mrc-viewability-measurement-requirements.yaml) — MRC Viewability Measurement Requirements
- [`spc:mrc-invalid-traffic-filtration-requirements`](https://github.com/groupsum/ad-measurement-media-governance-pack/blob/master/src/ssot_pack_ad_measurement_media/templates/specs/SPEC-2010-mrc-invalid-traffic-filtration-requirements.yaml) — MRC Invalid Traffic Filtration Requirements
- [`spc:ad-measurement-audit-evidence-requirements`](https://github.com/groupsum/ad-measurement-media-governance-pack/blob/master/src/ssot_pack_ad_measurement_media/templates/specs/SPEC-2011-ad-measurement-audit-evidence-requirements.yaml) — Ad Measurement Audit Evidence Requirements
- [`spc:ad-measurement-export-reconciliation-requirements`](https://github.com/groupsum/ad-measurement-media-governance-pack/blob/master/src/ssot_pack_ad_measurement_media/templates/specs/SPEC-2012-ad-measurement-export-reconciliation-requirements.yaml) — Ad Measurement Export Reconciliation Requirements

### Non-Goals

The pack supplies governance records. A downstream application implements the controls and collects its own conformance evidence.

---

## Getting Started

### Prerequisites

Use Python `>=3.10,<3.15`. Downstream synchronization also requires SSOT Registry and permission to write the target registry.

### Installation

If the desired PyPI release is a prerelease, use its exact version in the installer command.

#### uv

<!-- readme-standards:begin installation.uv -->
```bash
uv add ad-measurement-media-governance-pack
```
<!-- readme-standards:end installation.uv -->

#### pip

<!-- readme-standards:begin installation.pip -->
```bash
python -m pip install ad-measurement-media-governance-pack
```
<!-- readme-standards:end installation.pip -->

#### Poetry

<!-- readme-standards:begin installation.poetry -->
```bash
poetry add ad-measurement-media-governance-pack
```
<!-- readme-standards:end installation.poetry -->

### Quick Start

#### Example

<!-- readme-standards:begin example.quick-start -->
Source: [examples/quick_start.py](https://github.com/groupsum/ad-measurement-media-governance-pack/blob/master/examples/quick_start.py).

```python
"""Inspect the installed pack identity."""

from ssot_pack_ad_measurement_media import load_pack_metadata

metadata = load_pack_metadata()
assert metadata["origin"]["id"] == "pack:ad-measurement-media"
print(metadata["origin"]["id"])
```
<!-- readme-standards:end example.quick-start -->

#### Expected Result

The script prints `pack:ad-measurement-media` from the installed pack metadata.

---

## Usage

### Common Workflows

<!-- readme-standards:begin example.usage -->
Source: [examples/usage.py](https://github.com/groupsum/ad-measurement-media-governance-pack/blob/master/examples/usage.py).

```python
"""Find a specification and its downstream path in the installed manifest."""

from ssot_pack_ad_measurement_media import load_document_manifest

specification = next(
    row for row in load_document_manifest("spec")
    if row["id"] == "spc:openrtb-bid-request-measurement-field-requirements"
)
assert specification["target_path"] == ".ssot/specs/SPEC-2001-openrtb-bid-request-measurement-field-requirements.yaml"
```
<!-- readme-standards:end example.usage -->

Use the downstream environment that has both SSOT Registry and `ad-measurement-media-governance-pack` installed. Inspect the pack and preflight the target registry before approving synchronization.

```bash
uv run ssot pack inspect ssot_pack_ad_measurement_media
uv run ssot pack preflight . ssot_pack_ad_measurement_media --all
uv run ssot pack sync . ssot_pack_ad_measurement_media --all --trust --yes
uv run ssot validate .
```

### Configuration

Select the installed import package `ssot_pack_ad_measurement_media` in SSOT Registry. Review reservation owner `extension-pack:ad-measurement-media-governance-pack` and the target's trust policy before syncing.

### Error Handling

If preflight reports a schema, trust, or document-number conflict, resolve it in the target registry and repeat preflight before synchronization.

### Best Practices

Pin the pack version in downstream projects. Reference document IDs in local governance and inspect the change set before granting trust.

---

## Package Boundary

### What It Owns

Declared canonical ad measurement ownership relative to attribution.

### Public API and Import Surfaces

Import `load_pack_metadata`, `load_document_manifest`, and `read_packaged_document_text` from `ssot_pack_ad_measurement_media` to inspect packaged records.

### Entry Points

<!-- readme-standards:begin entry-points -->
This package declares no command-line, GUI, or plugin entry points in its manifest.
<!-- readme-standards:end entry-points -->

### Injected Dependencies

The package binds its metadata and document loaders through `ssot-pack-contracts`. The caller supplies the target registry to SSOT Registry when synchronizing.

### Protocol Consumers

SSOT Registry uses the pack metadata, document manifests, and bundled templates during inspect, preflight, and sync.

### Extensions

Define downstream policies as local records and reference the pack's document IDs. Send proposed changes to the canonical pack through repository review.

---

## Operations and Readiness

### Operational Requirements

Local inspection reads installed package resources. Synchronization requires an initialized downstream registry and explicit operator approval.

### Health and Observability

Review the preflight and sync output, then use `ssot validate` to check the resulting registry.

### Security and Resource Limits

Implicit trust is disabled. Review the exact distribution, version, records, and reserved IDs before enabling trust in a target registry.

### Compatibility

- Python `>=3.10,<3.15`
- SSOT Registry schema `>=0.4.0`
- SSOT pack contracts `>=0.2.17,<0.3.0`

---

## Verification

### Tests

Run `python -m unittest discover -s tests -v` with the pack installed. The [README workflow](https://github.com/groupsum/ad-measurement-media-governance-pack/actions/workflows/readme-standards.yml) checks the source README and runs both examples against an installed wheel.

### Certification Status

The pack has no external certification. Downstream adoption requires evidence for the controls an application implements.

### Evidence

See the [README workflow](https://github.com/groupsum/ad-measurement-media-governance-pack/actions/workflows/readme-standards.yml) for package and documentation verification and the [packaged records](https://github.com/groupsum/ad-measurement-media-governance-pack/blob/master/src/ssot_pack_ad_measurement_media/templates) for document-level sources.

---

## FAQ

### Why

**Why do document IDs matter?** Downstream records use them to trace an adopted decision or requirement to the pack that owns it.

### How

**How do I preview changes?** Use the registry's pack preflight before approving a sync.

### When

**When should I upgrade?** Read the changelog and preflight the new version against the target registry before applying it.

---

## Documentation and Related Packages

### More Documentation

See the [Pack guide](https://github.com/groupsum/ad-measurement-media-governance-pack/blob/master/docs/pack-guide.md), [changelog](https://github.com/groupsum/ad-measurement-media-governance-pack/blob/master/CHANGELOG.md), and [pack metadata](https://github.com/groupsum/ad-measurement-media-governance-pack/blob/master/src/ssot_pack_ad_measurement_media/metadata.json).

### Related Packages

[SSOT Registry](https://pypi.org/project/ssot-registry/) manages downstream registries. [SSOT Pack Contracts](https://pypi.org/project/ssot-pack-contracts/) provides the shared pack interface.

### Project Links

<!-- readme-standards:begin project-links -->
- [Homepage](https://github.com/groupsum/ad-measurement-media-governance-pack)
- [Issues](https://github.com/groupsum/ad-measurement-media-governance-pack/issues)
- [Repository](https://github.com/groupsum/ad-measurement-media-governance-pack)
- [pypi: ad-measurement-media-governance-pack](https://pypi.org/project/ad-measurement-media-governance-pack/)
<!-- readme-standards:end project-links -->

---

## Contributing

### How to Contribute

Open an [issue](https://github.com/groupsum/ad-measurement-media-governance-pack/issues) or pull request describing the affected records, their authority, and the expected downstream effect.

### Development Setup

Install the checkout with `python -m pip install -e .`, then run `python -m unittest discover -s tests -v`. On Python 3.11 or newer, run `uvx --from readme-standards==0.1.3 readme-standards check`.

### Notes for Maintainers

Keep source links, document identifiers, and committed manifest hashes aligned. Run `uvx --from readme-standards==0.1.3 readme-standards render --write` after changing generated README inputs.

---

## Governance

### Ownership and Decision Making

Groupsum maintains `pack:ad-measurement-media`. The pack's reservation owner is `extension-pack:ad-measurement-media-governance-pack`. Downstream registry operators approve synchronization.

### Standards and Policies

**Authority Sources**

- [OpenRTB](https://iabtechlab.com/standards/openrtb/)
- [AdCOM](https://iabtechlab.com/standards/adcom-advertising-common-object-model/)
- [VAST](https://iabtechlab.com/standards/vast/)
- [Open Measurement SDK / OMID](https://iabtechlab.com/open-measurement-sdk)
- [Media Rating Council Standards](https://mediaratingcouncil.org/standards)
- [IAB Click Measurement Guidelines](https://www.iab.com/guidelines/click-measurement-guidelines/)
- [IAB Digital Video Ad Measurement Guidelines](https://www.iab.com/guidelines/digital-video-ad-measurement-guidelines/)
- [IAB Tech Lab Measurement standards](https://iabtechlab.com/standards/measurement/)

### Lifecycle and Migration

Review [release changes](https://github.com/groupsum/ad-measurement-media-governance-pack/blob/master/CHANGELOG.md) and preflight the chosen version against each downstream registry.

---

## License and Attribution

### License

<!-- readme-standards:begin license -->
Licensed under `Apache-2.0`. See [LICENSE](https://github.com/groupsum/ad-measurement-media-governance-pack/blob/master/LICENSE).
<!-- readme-standards:end license -->

### Notices

<!-- readme-standards:begin notices -->
No separate NOTICE file is declared. Review the license and bundled third-party attributions.
<!-- readme-standards:end notices -->
