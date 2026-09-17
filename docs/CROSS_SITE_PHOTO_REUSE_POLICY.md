# Cross-site Photo Reuse Policy

Status: ACTIVE
Date: 2026-09-18

## User authorization

For FURUSHO OFFICIAL UX/UI development, photo assets already used on the user's other websites may be considered for reuse.

This authorization expands the candidate asset pool; it does not make every image appropriate for every context.

## Source priority

1. Existing approved Furusho real-person photography already used on owned/managed sites.
2. Existing real studio / activity / performance photography when it materially explains the section.
3. Existing project artwork where the project itself is being represented.
4. Platform preview imagery such as YouTube thumbnails for evidence links.
5. Generated imagery only for generic concepts where no real-person identity is implied.

## Identity rule

- Never fabricate or replace 古庄里好本人の appearance with AI-generated imagery.
- For person-focused sections, prefer real Furusho photographs over decorative/generated substitutes.
- Crop, focal position, brightness, contrast and saturation may be adjusted without altering identity.

## UX rule

Photos are evidence and context, not filler. Add an image only when it improves at least one of:
- identity / authority
- understanding of the work
- understanding of the environment or activity
- confidence before contacting
- visual navigation between major content groups

Do not turn the site into a gallery or generic card catalog. Preserve Editorial Authority v3: large, intentional, uncaged or minimally framed imagery with generous whitespace.

## Cross-site candidates confirmed during audit

Rhythm Speaker currently contains reusable candidate assets including:
- `tap-dance-instructor-furusho-noritaka.jpg` — approved Furusho instructor photo
- `instructor-action.jpg` — action-oriented instructor image candidate
- `hero.jpg` — Rhythm Speaker environment/hero candidate
- class / studio imagery under `classes/` and `assets/images/`

The Rhythm Speaker instructor implementation explicitly labels the Furusho source as an approved photo and its framing layer permits crop/position/light/contrast/saturation tuning without identity alteration.

## Import / linking policy

Preferred for important FURUSHO OFFICIAL identity imagery:
- import a controlled local copy into `furusho-official/assets/images/` when binary transfer is available;
- give it a semantic filename;
- register it through the Visual Asset Registry;
- use `<img>` for meaningful evidence imagery where practical.

Temporary cross-site direct URLs may be used only when the source is stable and controlled by the user, but local canonical assets are preferred for performance and independence.

## Quality gate

Before publishing a reused photo:
1. Confirm it is the intended person/place/activity.
2. Confirm it is appropriate for the target section.
3. Check crop and focal point on desktop and mobile.
4. Check brightness/contrast and avoid overly processed appearance.
5. Supply meaningful alt text when the image carries content.
6. Preserve lazy loading for below-the-fold images.
7. Do not duplicate the same photo repeatedly when another approved image can communicate the section better.
8. Run Visual Asset Registry, Navigation Contract and Navigation Audit checks.

## Next implementation direction

Use the expanded photo pool to reduce repeated use of `furusho-profile-main.jpg`, starting with a controlled real-photo upgrade to one page/section at a time. Prefer Furusho-specific real photography for Profile/About/Work contexts and project-specific photography for project/activity contexts.
