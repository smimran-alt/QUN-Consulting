# QUN Consulting — Website Version History

This file is the source of truth for change tracking and rollback of QUN Consulting website updates made in this conversation.

## Version policy

- Every future website change must receive a new version number (for example, **v1.0.1**, **v1.1.0**).
- Every update must record the date, affected file(s), activities performed, resulting GitHub commit SHA(s), and a rollback point.
- After each update, report the version number, activities completed, page links, and rollback instructions in the chat.
- For rollback, restore the exact file contents of the target commit to the current branch; **do not delete history or force-push**.
- Small styling/content fixes increment the patch version, new features increment the minor version, and major redesigns increment the major version.

---

## v2.1.0 — Eight scientific consulting hero banners

**Date:** 2026-10-28

**Status:** Current specialist-page release. Main `methodologies.html` unchanged.

### Activities completed

1. Created eight new service-specific, responsive SVG banner assets in `assets/banners/`. Each uses the established forest-green, white, pale green and scientific-consulting visual identity, with topic-specific diagrams.
2. Replaced the previous mountain photo background on all eight specialist methodology pages with the corresponding scientific consulting SVG banner.
3. Ensured that page headings, descriptions and buttons remain legible over the new background; added mobile-specific image positioning and overlay.
4. Preserved the six-stage infographics, assessment/use case/deliverable panels, illustrated case studies, and detailed service methodology.
5. Retained the main Methodologies page and all eight links unchanged.
6. Prepared a separate ZIP containing eight optimized image-generated photographic consulting banners. These JPG photographs are **not hosted in GitHub or used by the live website**; the GitHub pages currently use the published SVG banners. An image-upload-capable workflow is needed to replace the SVGs with the photographic JPGs.

### Modified pages / update commits

- `methodology-enterprise-cyber-risk.html` — `153a54d9fdca71c9f4e9800ab2ca5195cc03f731`
- `methodology-iso-27001-isms.html` — `e19417fb4ccd4133bea73ea8708f9b8f3c842491`
- `methodology-iso-42001-ai-governance.html` — `1126df806fdc21519715bf1a72913ee00d9bce31`
- `methodology-penetration-testing.html` — `d8992c4ac8206b48ee5f67afc65433fbbbf64062`
- `methodology-incident-response.html` — `3119ee69c06b1f40562659891d851993c01b02c0`
- `methodology-zero-trust-architecture.html` — `e77728cfd2483e23a25f7b992d134ca8644fa88f`
- `methodology-cyber-resilience.html` — `5aa86e2670ebc4e073902943bf8bd8a9af394881`
- `methodology-data-protection-insider-risk.html` — `ca2ee947876c21202825dcc45ee7421f5e98debd`

### New banner assets

- `assets/banners/enterprise-cyber-risk-scientific.svg`
- `assets/banners/iso-27001-isms-scientific.svg`
- `assets/banners/iso-42001-ai-governance-scientific.svg`
- `assets/banners/penetration-testing-scientific.svg`
- `assets/banners/incident-response-scientific.svg`
- `assets/banners/zero-trust-architecture-scientific.svg`
- `assets/banners/cyber-resilience-scientific.svg`
- `assets/banners/data-protection-insider-risk-scientific.svg`

### Rollback to v2.0.0

Restore the eight `methodology-*.html` pages from GitHub commit `89ecd0600b6838fc1516226bd963891c15eda6d7` and commit their restored contents to `main` without force pushing. The eight unused SVG assets may optionally be removed separately. Do not alter `methodologies.html`.

---

## v2.0.0 — Transform eight specialist methodology pages to illustrated editorial design

**Date:** 2026-10-28

**Status:** Current specialist-page release. Main `methodologies.html` remains at v1.1.3.

### Activities completed

1. Rebuilt eight specialist methodology pages to closely follow the approved visual references: full-width mountain-image hero, oversized editorial typography, white and green design, service-specific benefit labels and clear calls to action.
2. Replaced isolated hero diagrams with an illustrated six-step methodology row for each service. Every stage includes an icon, stage name and practical description.
3. Added three editorial information panels to each page: **What we assess**, **Common use cases**, and **What clients receive**, populated with service-specific content.
4. Retained each page's illustrative client scenario with three distinct parts: client pain point, how QUN would help and potential outcome, plus an explicit note that examples are fictional.
5. Added a landscape-backed **Business-first / Evidence-led / Action-oriented** principles panel.
6. Kept the original in-depth stage descriptions and detailed deliverables in an expandable section for readers seeking greater depth.
7. Applied responsive layout rules to adapt phase cards and information panels across desktop, tablet and mobile.
8. Preserved the navigation and contact calls to action. The main gallery's approved v1.1.3 layout is unchanged.

### Affected files and commits

- `methodology-enterprise-cyber-risk.html` — `cfccb57f028af506bf585fd7a1d67926f1faf051`
- `methodology-iso-27001-isms.html` — `2847d6ee5c53a3a6ca38545a02a8e7dc87378cbf`
- `methodology-iso-42001-ai-governance.html` — `5da2010b4b28fb34829b4df277f4b4344fa4c679`
- `methodology-penetration-testing.html` — `098a0776e48be5167565fa6fcad50f9d9d5a9f18`
- `methodology-incident-response.html` — `bbda79dd1963d75e37595141ec2f4242570410d3`
- `methodology-zero-trust-architecture.html` — `f19f83e2ccd5746bf703835d4c3520aefb9a2e80`
- `methodology-cyber-resilience.html` — `81c515688f45c56eebaf86dc8b51c4ec5f8b24db`
- `methodology-data-protection-insider-risk.html` — `6e16adb789e8e6b377c218e39bdda3c07b546f86`
- `WEBSITE_VERSION_HISTORY.md`

### Visual implementation note

The live HTML pages reproduce the reference layout through CSS, scalable custom vector icons, and an external mountain photo. The previously generated static reference images were used as visual direction and have not been embedded as full-page bitmaps.

### Rollback to v1.2.0

Restore the eight `methodology-*.html` files from commit `6c2dca5dbb63d62f815d55bc13dacfd0f83c269d`, which contains the prior eight-page state, then commit them on `main` without force-pushing. Leave the main `methodologies.html` page unchanged.

---

## v1.2.0 — Specialist methodology page visual and content overhaul

**Date:** 2026-10-27

**Status:** Current specialist-page release; main Methodologies page remains at v1.1.3

### Activities completed

1. Replaced the small, repeated hero timeline on all eight specialist pages with distinct, high-resolution responsive SVG infographics on a light background:
   - Enterprise Cyber Risk: risk exposure heatmap.
   - ISO 27001 ISMS: layered management-system controls.
   - ISO 42001 AI Governance: AI governance orbit.
   - Penetration Testing: authorized testing pathway.
   - Incident Response: continuous response-and-recovery cycle.
   - Zero Trust Architecture: context-aware access hub.
   - Cyber Resilience: recovery and dependency layers.
   - Data Protection & Insider Risk: information protection shield.
2. Increased the visual area, image contrast, type sizes, whitespace, and responsive scaling.
3. Replaced generic placeholder text beneath all four use cases on each page with service-specific explanations of what the use case helps a client assess or decide.
4. Added three clear outcome panels explaining what QUN examines, how it prioritizes, and what clients receive.
5. Preserved the detailed six-step methodology, output lists, four use cases, and **clearly labeled fictional client scenarios** on every page.
6. Kept `methodologies.html` and its approved v1.1.3 layout unchanged.

### Affected files and update commits

- `methodology-enterprise-cyber-risk.html` — `ab77ce0fb8a4ad54e748aca3db848e1587c9521d`
- `methodology-iso-27001-isms.html` — `b097600e9edb439cd621f5f147c7b72f6415eec3`
- `methodology-iso-42001-ai-governance.html` — `146dd04a3a0f00541cf51d4024a5967ea550f61a`
- `methodology-penetration-testing.html` — `c536bc7a0700a7ed6b713cdd9244ddbfe39c7030`
- `methodology-incident-response.html` — `eab19516119813fe4691c6eef924e95d4e065970`
- `methodology-zero-trust-architecture.html` — `421f6d57720b1998d2aeb472a7f1a36678517220`
- `methodology-cyber-resilience.html` — `03e243020d5589f3436fd4c5c367d971df00c645`
- `methodology-data-protection-insider-risk.html` — `0d8548cdac946a84b1e6481d98984bd0363ff3e4`
- `WEBSITE_VERSION_HISTORY.md` — release record

### Rollback to previous specialist-page release (v1.1.0)

Restore the eight `methodology-*.html` files from the repository commit `67e6267b777646c3a18922e2f813130d8a141c75` (before this release), commit those restored contents onto `main`, and record the rollback. Do not force-push. The main Methodologies page need not be changed.

---

## Rollback — v1.1.4 → v1.1.3 (current)

**Date:** 2026-10-27

**Status:** v1.1.3 restored as active Methodologies page

### Activities completed

1. Restored `methodologies.html` exactly to its v1.1.3 content.
2. Reversed the v1.1.4 hero copywriting, featured-service descriptions, enlarged illustration treatments and three-principle strip.
3. Preserved all eight featured service cards and links to their dedicated methodology pages.
4. Kept the long 20-card technical gallery removed, as specified by v1.1.3.
5. Left all other website pages unchanged.

### GitHub rollback commit

- `ce73598841002675f7c5365fc9e885a6518e6d68`

### Restore options

- To return to v1.1.4, restore `methodologies.html` from commit `8b8a7e188801f644844461d05c9757c445091b91`.
- To return to v1.1.3 again, restore `methodologies.html` from commit `ce73598841002675f7c5365fc9e885a6518e6d68`.
- Commit a rollback on `main`; do not force-push.

---

## Rollback — v1.1.5 → v1.1.4 (current)

**Date:** 2026-10-27

**Status:** v1.1.4 restored as active page

### Activities completed

1. Reverted the v1.1.5 larger-font, larger-image, and two-column card layout changes.
2. Restored `methodologies.html` exactly from the previous v1.1.4 snapshot.
3. Preserved all eight featured methodology links and service detail pages.
4. Left the separate methodology guide and all other website files unchanged.

### GitHub rollback commit

- `8b8a7e188801f644844461d05c9757c445091b91`

### Roll-forward reference

To restore the former v1.1.5 design, retrieve `methodologies.html` at commit `37bd91f7b8603802ac6e86cd280bd1504f2a9f67` and commit its contents to `main` without force-pushing.

---

## v1.1.5 — Larger fonts and methodology illustrations

**Date:** 2026-10-27

**Status:** Current

### Activities completed

1. Increased hero heading, paragraph, navigation, section heading, phase-description, and CTA font sizes.
2. Changed the eight featured methodologies to a spacious two-column desktop gallery instead of four small cards per row.
3. Expanded the featured illustrations and their layout space, placing artwork beside each service's text in larger horizontal cards.
4. Increased the service-card heading, category label, description, and navigation-arrow sizes.
5. Improved spacing, card heights, contrast, and responsive tablet/mobile layouts.
6. Retained all eight service links, the six-stage methodology and detailed guide links.

### Affected files

- `methodologies.html`
- `WEBSITE_VERSION_HISTORY.md`

### Commit and rollback

- Page update commit: `1b89c3bb28f53f80ab5fd4b45667d30f81b4a8f2`.
- To restore **v1.1.4**, restore `methodologies.html` from commit `d7c4c9ca16a8d250ac67a1bb8ffc71c02d2dd75e` and commit those contents on `main`, without force-pushing.
- Other pages are unchanged.

---

## v1.1.4 — Methodologies page content and image improvement

**Date:** 2026-10-27

**Status:** Current

### Activities completed

1. Rewrote the hero introduction to emphasize business outcomes, risk-based decisions, practical safeguards, and measurable improvement.
2. Clarified how the six-stage delivery framework translates assessment findings into decisions and client deliverables.
3. Refined the service-library introduction and the final contact call to action.
4. Replaced all eight featured service-card summaries with service-specific, client-facing value propositions.
5. Improved all eight featured vector illustrations with layered green artwork, larger image areas and higher visual emphasis.
6. Improved hero photo treatment, readability, typography, card spacing and responsive presentation.
7. Added a concise three-principle strip: Business-first, Evidence-led, Action-oriented.
8. Kept the eight service-detail page links, separate methodology guide and overall page structure intact.

### Affected files

- `methodologies.html`
- `WEBSITE_VERSION_HISTORY.md`

### GitHub commit and rollback

- Page update: `ef2797c8a24718b22df53a67f6e216b4ee6d41a7`
- To restore **v1.1.3**, restore `methodologies.html` from commit `c11346fc426018a81387d2d222333499c7dbe97e` and commit the restored file to `main`. This leaves all dedicated service pages unchanged. Do not force-push.
- The artwork comprises editable, scalable SVG illustrations rather than raster image files.

---

## v1.1.3 — Remove detailed 20-methodology gallery

**Date:** 2026-10-27

**Status:** Current

### Activities completed

1. Removed the large 20-card detailed methodology gallery shown below the eight featured methodology cards on `methodologies.html`.
2. Removed its search box, capability filters, result counter, and 'Explore all 20 methodologies' expandable control.
3. Removed now-unused diagram expansion modal and supporting JavaScript.
4. Preserved the eight illustrated featured methodology cards and their dedicated service-detail page links.
5. Kept the signature six-stage methodology and the 'How Our Methodology Works' guide intact.
6. Linked the library heading's supporting action to the existing delivery-approach guide.
7. Kept the responsive mobile navigation functionality.

### Affected files

- `methodologies.html`
- `WEBSITE_VERSION_HISTORY.md`

### Commit and rollback

- Main page update commit: `56ee600ce7021e11a0eb8b4c996ababfb961a744`.
- To revert this change and restore **v1.1.2**, restore `methodologies.html` from commit `247c61b8a0d1d16a8ebdebe2ece6bd02c306c4b0` (state just before v1.1.3), and commit its contents to `main` without force pushing.
- Other pages are unchanged.

---

## v1.1.2 — Visual transformation of How Our Methodology Works

**Date:** 2026-10-27

**Status:** Current

### Activities completed
1. Rebuilt the guide's opening as a mountain-image editorial hero inspired by the approved reference, with QUN's white, dark green and lime-green colour palette.
2. Added six prominent, linked circular phase icons with clear typical outcomes.
3. Created six illustrated summary cards, each linking to its full phase explanation and displaying a high-resolution scalable SVG diagram.
4. Preserved all six full phase explanations, activities, client deliverables, and decision questions below the new overview.
5. Improved responsive layout and spacing across desktop, tablet, and mobile.
6. Kept other methodology and service pages unchanged.

### Affected files
- `how-our-methodology-works.html`
- `WEBSITE_VERSION_HISTORY.md`

### Commit and rollback
- Guide update commit: `18c143cf93476629e2ef827dd37c80edf16caf9e`
- To revert the guide to **v1.1.1**, restore `how-our-methodology-works.html` from commit `ad25d9fa2449fe86e6145f2dc2ba624cec6654ae` (or its identical v1.1.1 file revision) and commit that content onto `main`. Do not force-push.
- This version is a webpage reconstruction of the reference image, not a literal pixel-for-pixel image upload.

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
