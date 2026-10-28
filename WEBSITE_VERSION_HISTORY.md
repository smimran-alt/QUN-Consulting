# QUN Consulting — Website Version History

This file is the source of truth for change tracking and rollback of QUN Consulting website updates made in this conversation.

## Version policy

- Every future website change must receive a new version number (for example, **v1.0.1**, **v1.1.0**).
- Every update must record the date, affected file(s), activities performed, resulting GitHub commit SHA(s), and a rollback point.
- After each update, report the version number, activities completed, page links, and rollback instructions in the chat.
- For rollback, restore the exact file contents of the target commit to the current branch; **do not delete history or force-push**.
- Small styling/content fixes increment the patch version, new features increment the minor version, and major redesigns increment the major version.

---

## v1.1.1 — Detailed methodology infographic upgrade

**Date:** 2026-10-27

**Status:** Current

### Activities completed

1. Replaced all six infographics on `how-our-methodology-works.html` with cleaner, more readable scalable SVG diagrams.
2. Designed a different diagram for each phase: Discover stakeholder/context map; Assess risk heatmap; Design target-state layers; Implement delivery milestones; Validate assurance shield; Optimize continuous improvement loop.
3. Improved picture prominence, light backgrounds, contrast, typography, stage framing and responsive sizing.
4. Preserved all six phase descriptions, activities, deliverables and navigation.
5. Kept other website pages and the 20-methodology library unchanged.

### Files and commits

- `how-our-methodology-works.html` new file blob SHA: `65e4d62bc2fb307ee477eddd34d5d306327fe5e4`
- All other website files unchanged.

### Rollback to v1.1.0

Restore `how-our-methodology-works.html` from commit `b154cb3d0a2082976959d8f560785d13ec2c1bcc` (the previous release baseline), then commit it to `main`. Do not force-push. The earlier file blob SHA was `26a0f5e346ee2cae4115cbb754aa4ab984b0f1aa`.

---

## v1.1.0 — Eight dedicated specialist methodology pages

**Date:** 2026-10-27

**Status:** Current

### Activities performed

1. Created a standalone page for each of the eight featured methodologies: Enterprise Cyber Risk; ISO 27001 ISMS; ISO 42001 AI Governance; Penetration Testing; Incident Response; Zero Trust Architecture; Cyber Resilience; Data Protection & Insider Risk.
2. Wrote a structured six-stage service-specific delivery approach with a vector process infographic on every page.
3. Added four practical use cases and typical client deliverables per service.
4. Added a three-part **fictional illustrative client scenario** on every page: client pain point, how QUN would help, and potential value. These are **not** claims of real QUN client engagements or verified results.
5. Connected each of the eight featured cards on `methodologies.html` to its dedicated page.
6. Preserved the original 20-entry detailed methodology library, page search, filters, and existing signature delivery sections.
7. Kept the white, forest-green and lime-green QUN visual design and responsive navigation.

### Affected files

- `methodologies.html`
- `methodology-enterprise-cyber-risk.html`
- `methodology-iso-27001-isms.html`
- `methodology-iso-42001-ai-governance.html`
- `methodology-penetration-testing.html`
- `methodology-incident-response.html`
- `methodology-zero-trust-architecture.html`
- `methodology-cyber-resilience.html`
- `methodology-data-protection-insider-risk.html`
- `WEBSITE_VERSION_HISTORY.md`

### GitHub commits

- Main methodology page: `6a98d8715effe0aee972c7c0fb08b10f5df8246a`
- Enterprise Cyber Risk: `cf63f0a6e9cddaeed82c89d22946aaa5a17e3c07`
- ISO 27001 ISMS: `fd6f1c2f4a1b3e74ca17c59f83f2a19ffd3274da`
- ISO 42001 AI Governance: `55c099669e16dbedddcfff8947db9afad07adc33`
- Penetration Testing: `e0103aa057424fe675efa17f3733eb6962ad368e`
- Incident Response: `060afee6f463f43c8da339c89814baa27d1390aa`
- Zero Trust Architecture: `fb299367cb5509a8bb70d89e4b7a5edf20857efa`
- Cyber Resilience: `9e96b7b554cd36c1140ac74fcad2c591082dafa8`
- Data Protection & Insider Risk: `8974934df9e80fef8a36a0cddb34776994623c89`

### Rollback to v1.0.1

1. Restore `methodologies.html` to the content at the v1.0.1 commit `5135310c7c1b434b4b10bfcc58d8cb231268a126` (prior to the eight-page links).
2. Optionally delete the eight `methodology-*.html` pages created for v1.1.0 if complete removal is requested; leaving unlinked pages does not change the primary website.
3. Commit the rollback on `main` without force-pushing or rewriting history.
4. Record the rollback as a new version entry.

---

## v1.0.1 — Orientation and alignment refinement

**Date:** 2026-10-27

**Status:** Current

### Activities performed

1. Improved the hero content alignment and call-to-action wrapping.
2. Standardized heading and introduction alignment across methodology sections.
3. Equalized the layout and output-card positioning for all six signature stages.
4. Improved the six explanatory cards' alignment, heights, and content spacing.
5. Aligned the eight featured methodology cards, titles, arrows, and illustrations.
6. Refined detailed methodology card sizing and infographic containment.
7. Adjusted desktop, tablet, and mobile grid breakpoints for better orientation.
8. Preserved all existing content, interactions, 20 methodologies, and eight featured illustrations.

### Affected files

- `methodologies.html` (CSS-only alignment and responsive refinements)
- `WEBSITE_VERSION_HISTORY.md` (this version record)

### Version commit

- `5135310c7c1b434b4b10bfcc58d8cb231268a126`

### Rollback instructions

To return to **v1.0.0**, restore `methodologies.html` from commit `94d9582d94b80a794a77e99c55b08313ab9bb4f5` and commit that file onto `main`. Do not force-push or alter other files. The separate methodology guide was not changed in v1.0.1.

---

## v1.0.0 — Restored baseline

**Date:** 2026-10-27

**Status:** Current baseline / rollback completed

### Activities performed

1. Reverted the six clickable circular phase icons and related call-to-action changes on `methodologies.html`.
2. Restored the original `how-our-methodology-works.html` page, removing the latest Previous/Next navigation additions.
3. Preserved the existing dedicated methodology guide and links already present in the earlier page.
4. Preserved the eight featured specialist methodologies and all 20 detailed methodology entries.
5. Established a formal versioning and activity log for subsequent updates.

### Restored file contents (reference revisions)

- `methodologies.html` — source commit `ec8a357570029b8340039308d68f5101d01d574f`
- `how-our-methodology-works.html` — source commit `08b4447ad6e61343726a6390e05538c16b895223`

### Restore commits on `main`

- `methodologies.html`: `0654ee3ee14bfe94ab6126842c8fb8f91e944616`
- `how-our-methodology-works.html`: `94d9582d94b80a794a77e99c55b08313ab9bb4f5`

### Rollback reference

To restore v1.0.0 again, retrieve the two files at the **restore commit** `94d9582d94b80a794a77e99c55b08313ab9bb4f5` (which includes both restorations) and commit their contents to the current branch. Other website files should remain unchanged.

---
