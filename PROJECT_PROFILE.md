# PROJECT_PROFILE

Version: 1.3
Status: ACTIVE

## Project Identity

Project Name: furusho-official

Japanese Name: 古庄里好 Official Website

Project Purpose: 古庄里好 / Noritaka Furusho の公式個人Webサイトを構築・公開し、プロフィール、実績、現在の活動、メディア、個人として請け負う仕事、問い合わせ導線を、正確かつ安全なPUBLIC情報だけで提供する。

Project Type:
- Official Homepage
- Personal Authority Site
- Editorial Portfolio
- Static Website

## Primary Repository

Primary Repository: noritap/furusho-official
Default Branch: main
Repository Strategy: Single Project Repository
Canonical Profile Path: /PROJECT_PROFILE.md
Primary WRITE Repository: noritap/furusho-official

## Source of Truth

Website implementation: GitHub main of noritap/furusho-official
Profile / evidence / publication control: noritap/FURUSHO_PROFILE_OS
Current redesign handoff: FURUSHO_PROFILE_OS/06_TASKS/64_FURUSHO_OFFICIAL_V3_EDITORIAL_REDESIGN_HANDOFF.md
Contact detail handoff: FURUSHO_PROFILE_OS/06_TASKS/63_OFFICIAL_WEBSITE_CONTACT_SYNC_HANDOFF.md
Rule source: noritap/AI_OS_CREATION_RULES

## Boundary

This repository owns PUBLIC website implementation only.
It does not become the source of truth for career evidence, verification status, business operations, customer data, payment, authentication, RS Wallet, Rhythm Speaker operations, or internal strategy.

古庄里好個人への依頼と Rhythm Speaker の運営サービスは、同じサイト内でも明確に区別する。
Rhythm Speaker のレッスン、スタジオ利用、予約など運営問い合わせは、原則として Rhythm Speaker 側の公式導線へ送る。

## Do Not Touch

- Do not publish VERIFY / INTERNAL / DO_NOT_USE information as fact.
- Do not invent career dates, awards, metrics, affiliations, endorsements, prices, delivery conditions, travel conditions, contracts, or staffing conditions.
- Do not store secrets, customer data, payment data, auth data, tokens, passwords, or .env contents.
- Do not copy internal operational details from FURUSHO_PROFILE_OS into public pages.
- Do not present third-party brands as endorsements.
- Do not fabricate or replace 古庄里好本人の外見 with AI-generated imagery.
- Do not accumulate permanent visual-preview-v22 / v23 style override layers as the canonical design system.

## Priorities

1. Factual accuracy
2. Publication safety
3. UX clarity
4. Mobile UX
5. Clear identity and authority
6. Personal work / Rhythm Speaker boundary clarity
7. Contact conversion
8. Accessibility
9. SEO foundation
10. Fast static delivery
11. Maintainability

## Development State

Current Phase: Phase 3 / FURUSHO OFFICIAL v3 — Editorial Authority

Current Goal: Build a credible editorial authority site where a first-time visitor can quickly understand who 古庄里好 is, what work can be commissioned directly, what belongs to Rhythm Speaker, review selected evidence, and reach the correct inquiry path with minimal friction.

Current design system:
- Working name: FURUSHO OFFICIAL v3 — Editorial Authority
- Primary style: STYLE-FAS-003 Minimal Suit Frame (70%)
- Secondary style: STYLE-MAG-001 Simple Rockin Editorial (30%)
- Visual character: refined / adult / artistic / calm authority / cultural / modern editorial
- Palette: warm off-white, rich black / charcoal, controlled gray, one restrained warm accent
- Typography: refined serif / Mincho for major editorial headings; clean sans for body, navigation, and utility text
- Layout: editorial asymmetry, generous whitespace, large uncaged real photography, near-zero border radius
- UI policy: reduce generic cards, bento grids, pills, gradients, and decorative UI that does not improve comprehension
- Core principle: 「情報は捨てない。WebサイトっぽいUIを捨てる。」

Current HOME information architecture:
1. HERO
2. ROUTE
3. WORK WITH FURUSHO
4. SELECTED WORKS
5. STATEMENT
6. PROJECTS
7. ABOUT
8. CONTACT

Current implementation baseline:
- HOME v3 Editorial Authority published
- Global Navigation contract FURUSHO-NAV-2 retained
- /profile, /career, /activities, /projects, /media, /contact pages published
- Profile v3 editorial index refinement published
- Career v3 editorial hierarchy and featured stories published
- Media v3 editorial index published
- Projects v3 editorial directory published
- Contact synchronized to Email + LINE routing
- Work with Furusho separated from Rhythm Speaker operational routes
- Selected Works initial top three: 映画「座頭市」 / CITIZEN デュラテクトCM / DREAMS COME TRUE「連れてって 連れてって」
- NF TAP brand mark integrated into header, favicon / touch icon, and web app manifest
- real portrait asset `assets/images/furusho-profile-main.jpg` used as the primary identity image
- Visual Asset Registry and automated review generation
- Navigation Audit / Navigation Contract Sync / Visual Asset Registry CI checks
- sitemap and OGP baseline for primary public pages
- GitHub Pages public delivery

## Navigation Contract

NAV_VERSION: FURUSHO-NAV-2

Global navigation:
1. About — /furusho-official/#about
2. Work — /furusho-official/#work
3. Projects — /furusho-official/projects/
4. Career — /furusho-official/career/
5. Contact — /furusho-official/contact/

Brand / Home → /furusho-official/
Primary CTA → Contact

Do not change the global navigation architecture without evidence of a navigation problem.

## Contact Contract

Public personal contact:
- Email: furushonoritaka@gmail.com
- LINE: https://lin.ee/zC5YLe7

Routing:
- Formal business / corporate / production / school / facility inquiries → Email recommended
- Individual / simple / existing LINE communication → LINE available
- Rhythm Speaker operational inquiries → Rhythm Speaker / project-specific official channels by default

## Validation

- PUBLIC claims must trace back to FURUSHO_PROFILE_OS.
- HTML must remain usable without JavaScript.
- Mobile layout must preserve information priority rather than simply shrink desktop UI.
- No horizontal overflow or important hover-only meaning.
- Primary CTA must remain obvious without aggressive sales styling.
- External links must be explicit and safe.
- No internal-only information may appear in production copy.
- Global Navigation must satisfy NAVIGATION_REGISTRY.md.
- Visual assets must remain traceable through assets/data/media-assets.json.
- REVIEW_REQUIRED assets must not be promoted into public use without explicit confirmation.
- Person-focused images placed in landscape contexts must use intentional focal points.
- Focus-visible, semantic heading order, tap targets, contrast, and reduced-motion behavior must remain usable.
- HOME must not regress into a generic card catalog.
- Verified work evidence should carry authority; invented quotes, logos, or endorsements are prohibited.
- Do not claim business outcome improvement without measured evidence.

## Technical Debt / Consolidation

- `assets/css/style.css` still imports the additive `visual-preview-v21.css` layer.
- v3 should consolidate obsolete preview-era styling into deliberate canonical shared CSS rather than stacking new permanent preview override files.
- Projects currently contains page-local style rules that should be moved into a maintainable canonical stylesheet during cleanup.
- Shared subpage styling should be visually verified before obsolete selectors are removed.

## Next Handoff

1. Complete Activities v3 editorial clarification, especially TAP DANCE PLANET and current activity hierarchy.
2. Consolidate shared CSS and remove obsolete preview-era layering without visual regression.
3. Move Projects page-local styling into a canonical stylesheet during CSS cleanup.
4. Run total Visual QA across HOME and primary subpages: desktop / mobile / keyboard / focus / links / no-JS / accessibility / asset registry.
5. Replace typography fallback imagery only when approved real assets become available.
6. Keep PROJECT_PROFILE.md, NAVIGATION_REGISTRY.md, Visual Asset Registry, and public implementation synchronized with main.
