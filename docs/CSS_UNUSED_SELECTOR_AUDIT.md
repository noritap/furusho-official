# Shared CSS Unused Selector Audit

Status: ACTIVE
Baseline: `main` at `b6ba88d65dfbfc7b7de2d271cacf53f7f8e22b56`
Target: `assets/css/style.css`

## Audit policy

Remove shared CSS only in small families after confirming that the selector is absent from current public HTML. Page-specific stylesheets are not treated as evidence that a historical shared selector is still required.

## Unit 01 — legacy career grid family

Repository-wide code search on the current baseline returned no public-file matches for:

- `.career-grid`
- `.career-links`
- `.career-link`

These selectors remain in `assets/css/style.css` as pre-v3 shared styling, while Career v3 uses its dedicated `career/career.css` implementation.

### Candidate removal scope

The controlled removal unit is limited to:

- desktop `.career-grid` layout rules and descendants
- `.career-links` / `.career-link` rules, including hover and focus states
- `.career-grid` references inside the 980px and 720px responsive rules
- mobile-only `.career-link` / `.career-links` rules

Do not remove `.activity-grid`, `.dark-section`, `.section-label`, `.number`, or other neighboring shared selectors in the same change unless independently proven unused.

### Result

Audit: PASS — candidate family is isolated for the next deletion commit.
Visual change expected: none, because no current public HTML references the audited family.
