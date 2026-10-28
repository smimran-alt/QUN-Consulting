# QUN Consulting — Website Version History

This file is the source of truth for change tracking and rollback of QUN Consulting website updates made in this conversation.

## Version policy

- Every future website change must receive a new version number (for example, **v1.0.1**, **v1.1.0**).
- Every update must record the date, affected file(s), activities performed, resulting GitHub commit SHA(s), and a rollback point.
- After each update, report the version number, activities completed, page links, and rollback instructions in the chat.
- For rollback, restore the exact file contents of the target commit to the current branch; **do not delete history or force-push**.
- Small styling/content fixes increment the patch version, new features increment the minor version, and major redesigns increment the major version.

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
