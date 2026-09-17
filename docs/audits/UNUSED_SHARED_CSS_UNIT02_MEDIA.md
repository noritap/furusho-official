# Unused Shared CSS Audit — Unit 02 / Media legacy family

Status: EVIDENCE GATE PASSED
Base main: `4f09358ae8469b53b942a278731611eca984323b`
Target: `assets/css/style.css`

## Candidate legacy selector family

The shared stylesheet still contains the older media-index family:

- `.media-section`
- `.link-list`
- `.media-link`
- `.media-icon`
- `.media-icon svg`
- `.media-type`
- `.media-link strong`
- `.media-link:hover .media-icon`
- `.media-link:hover strong`
- `.media-link:focus-visible`
- responsive `.media-link` / `.media-icon` / `.media-type` rules at max-width 720px

## Evidence

Default-branch code search returned no current references for:

- `media-link`
- `link-list`
- combined `link-list media-link media-icon media-type`

The current Media v3 implementation uses its page-specific editorial stylesheet (`media/media.css`) rather than this legacy shared selector family.

## Protected scope

A future deletion unit must not remove or alter neighboring shared rules that are still part of the v3 system, including:

- `.activity-grid`
- `.contact-section`
- `.contact-inner`
- `.contact-actions`
- `.button.light`
- `.footer`
- `.mobile-action-bar`

No production CSS or HTML is changed by this audit unit.

## Next action

Delete only the audited legacy Media selector family from `assets/css/style.css`, including its matching responsive references, then run repository checks before merge.
