# UNUSED SHARED CSS — UNIT 06 / ROUTE

Status: EVIDENCE GATE PASSED

## Baseline
- Repository: `noritap/furusho-official`
- Base main: `372a1b952c6fe379de8b72e27778d7d6166e9037`
- Target: `assets/css/style.css`

## Candidate legacy family
- `.route-section`
- `.route-heading`
- `.route-heading h2`
- `.route-heading p`
- `.route-grid`
- `.route-card`
- `.route-card:hover`
- `.route-card-primary`
- `.route-card-primary:hover`
- `.route-number`
- `.route-kicker`
- `.route-card-primary .route-number`
- `.route-card-primary .route-kicker`
- `.route-card strong`
- `.route-arrow`
- `.route-card:focus-visible` token in shared focus selector list
- matching max-width 980px and 720px Route responsive rules

## Evidence
- Default-branch GitHub code search returned no references for `route-grid`, `route-card`, or `route-section`.
- Current HOME was inspected directly at base main. Its active v3 route implementation uses `.v3-route`, `.v3-route-head`, `.v3-route-list`, and `.v3-route-link`, with `assets/css/home-v3.css`; it does not use the legacy shared Route selector family above.
- GitHub code search is supporting evidence, and direct HOME inspection provides page-level confirmation for the known route implementation.

## Protected scope
Do not alter in this unit:
- `.site-header` / `.nav` / `.nav-cta`
- `.hero` legacy/shared family unless separately audited
- `.section`, `.section-intro`, `.split-heading`, `.section-label`
- `.about-section`
- `.dark-section`
- `.contact-section`
- `.footer`
- `.mobile-action-bar`
- HOME v3 classes in `assets/css/home-v3.css`

The shared focus selector list must be rewritten only to remove `.route-card:focus-visible`; all other focus targets remain.

## Decision
Evidence gate passed for a controlled deletion unit. This audit changes no production CSS or HTML.

## Next action
Delete only the audited legacy Route family and its matching responsive/focus references from `assets/css/style.css`, run Navigation Contract Sync Check and Navigation Audit, then merge only on success.
