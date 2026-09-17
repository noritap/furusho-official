# Unused Shared CSS Audit — Unit 03 / Activity legacy family

Status: EVIDENCE GATE PASSED
Base main: `3921514868c1581a6a141bb8f943e6c84b2f6332`
Target: `assets/css/style.css`

## Candidate legacy selector family

The shared stylesheet still contains the older activity-grid family:

- `.activity-grid`
- `.activity-grid article`
- `.number`
- `.activity-grid h3`
- `.activity-grid p:last-child`
- responsive `.activity-grid` rules at max-width 980px and 720px
- responsive `.activity-grid article` rule at max-width 720px

## Evidence

Default-branch code search returned no current references for `activity-grid`.

The current Activities v3 page was previously migrated to its page-specific editorial implementation and no longer relies on this shared grid family.

## Protected scope

A future deletion unit must not remove or alter neighboring shared v3 rules, including:

- `.about-section`
- `.dark-section`
- `.dark-section .section-label`
- `.contact-section`
- `.work-grid` / `.work-card` until separately audited
- `.route-grid` / `.route-card` until separately audited
- `.footer`
- `.mobile-action-bar`

No production CSS or HTML is changed by this audit unit.

## Next action

Delete only the audited Activity selector family from `assets/css/style.css`, including its matching responsive references, then run repository checks before merge.
