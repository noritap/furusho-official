# PROJECT_PROFILE

Version: 1.1
Status: ACTIVE

## Project Identity

Project Name: furusho-official

Japanese Name: 古庄里好 Official Website

Project Purpose: 古庄里好 / Noritaka Furusho の公式個人Webサイトを構築・公開し、プロフィール、実績、現在の活動、メディア、出演・振付・講師・取材・提携の問い合わせ導線を、正確かつ安全なPUBLIC情報だけで提供する。

Project Type:
- Official Homepage
- Personal Authority Site
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
Phase 1 plan: FURUSHO_PROFILE_OS/06_TASKS/62_FURUSHO_OFFICIAL_WEBSITE_PHASE1_PLAN.md
Rule source: noritap/AI_OS_CREATION_RULES

## Boundary

This repository owns PUBLIC website implementation only.
It does not become the source of truth for career evidence, verification status, business operations, customer data, payment, authentication, RS Wallet, Rhythm Speaker operations, or internal strategy.

## Do Not Touch

- Do not publish VERIFY / INTERNAL / DO_NOT_USE information as fact.
- Do not invent career dates, awards, metrics, affiliations, or endorsements.
- Do not store secrets, customer data, payment data, auth data, tokens, passwords, or .env contents.
- Do not copy internal operational details from FURUSHO_PROFILE_OS into public pages.
- Do not present third-party brands as endorsements.

## Priorities

1. Factual accuracy
2. Publication safety
3. Mobile UX
4. Clear identity and authority
5. Contact conversion
6. Accessibility
7. SEO foundation
8. Fast static delivery
9. Maintainability

## Development State

Current Phase: Phase 2 / UX・Visual System consolidation

Current Goal: Maintain a credible mobile-first official hub where visitors can identify 古庄里好, review selected work and projects through consistent visual cards, distinguish personal work from Rhythm Speaker studio use, and reach the correct inquiry path with minimal friction.

Current implementation baseline:
- HOME UX v2 purpose-based routing
- Global Navigation contract FURUSHO-NAV-2
- /profile, /career, /activities, /projects, /media, /contact pages published
- shared visual card / image preview system
- Visual Asset Registry and automated review generation
- Navigation Audit / Navigation Contract Sync / Visual Asset Registry CI checks
- GitHub Pages public delivery

## Validation

- PUBLIC claims must trace back to FURUSHO_PROFILE_OS.
- HTML must remain usable without JavaScript.
- Mobile layout must be first-class.
- External links must be explicit and safe.
- No internal-only information may appear in production copy.
- Global Navigation must satisfy NAVIGATION_REGISTRY.md.
- Visual assets must remain traceable through assets/data/media-assets.json.
- REVIEW_REQUIRED assets must not be promoted into public use without explicit confirmation.

## Next Handoff

1. Continue live visual QA across HOME and all primary subpages.
2. Replace typography fallback cards with approved real assets when suitable source images become available.
3. Improve Career / Projects / Media visual consistency without weakening publication safety.
4. Review responsive spacing, card cropping, CTA hierarchy, and accessibility on real devices.
5. Keep PROJECT_PROFILE.md, NAVIGATION_REGISTRY.md, Visual Asset Registry, and public implementation synchronized with main.
