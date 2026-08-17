# PROJECT_PROFILE

Version: 1.0
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

Current Phase: Phase 1 / Initial official homepage
Current Goal: Publish a credible, mobile-first official homepage with verified profile highlights, selected career, current activities, media links, and inquiry CTA.

## Validation

- PUBLIC claims must trace back to FURUSHO_PROFILE_OS.
- HTML must remain usable without JavaScript.
- Mobile layout must be first-class.
- External links must be explicit and safe.
- No internal-only information may appear in production copy.

## Next Handoff

1. Complete initial HOME.
2. Add approved profile image asset.
3. Add /profile, /career, /activities, /media, /contact pages.
4. Add GitHub Pages deployment.
5. Review the live site and iterate UI/UX, SEO, and conversion paths.
