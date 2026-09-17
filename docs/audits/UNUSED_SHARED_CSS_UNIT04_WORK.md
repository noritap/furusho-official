# Unused Shared CSS Audit — Unit 04 / Work legacy family

Status: EVIDENCE GATE PASSED
Base main: `b358d4e05fe6b9fafad6a2dcb414a229da930bb3`
Target: `assets/css/style.css`

## Candidate legacy selector family

The shared stylesheet still contains the older work-card family:

- `.work-section`
- `.work-grid`
- `.work-card`
- `.work-index`
- `.work-card h3`
- `.work-card p`
- `.work-card a`
- `.work-card a:hover`
- `.work-card a:focus-visible` as part of the shared focus selector list
- responsive `.work-grid` rules at max-width 980px and 720px
- responsive `.work-card` rules at max-width 720px

## Evidence

Default-branch code search returned no current references for:

- `work-grid`
- `work-card`
- `work-section`

This supports treating the old shared work-card implementation as a legacy family. Search is supporting evidence rather than proof by itself; deletion remains constrained to this exact audited family.

## Protected scope

A future deletion unit must not remove or alter neighboring shared v3 rules without a separate audit, including:

- `.route-grid` / `.route-card`
- `.boundary-note`
- `.boundary-label`
- `.about-section`
- `.dark-section`
- `.contact-section`
- `.footer`
- `.mobile-action-bar`

The shared focus selector list must be rewritten only to remove `.work-card a:focus-visible`; all other focus targets must remain unchanged.

No production CSS or HTML is changed by this audit unit.

## Next action

Delete only the audited Work selector family from `assets/css/style.css`, including its matching responsive references and the `.work-card a:focus-visible` token, then run repository checks before merge.
