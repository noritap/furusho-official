# 古庄里好 Official Website

Official website of Noritaka Furusho / 古庄里好.

## Purpose

This repository contains the PUBLIC website implementation for 古庄里好.

Profile facts, evidence, publication status, media rights, and canonical profile copy are managed separately in `noritap/FURUSHO_PROFILE_OS`.

## Website principles

- Mobile-first static HTML/CSS
- No JavaScript dependency for core navigation/content
- PUBLIC-safe content only
- Profile/evidence claims trace back to `noritap/FURUSHO_PROFILE_OS`
- UI/UX favors clear routing, contact conversion, accessibility, and fast static delivery

## Adopted visual identity (2026-11-18)

- This remains **古庄里好's personal official website**, not a Nonry Service Jr. shop. Preserve the public career, commission and Rhythm Speaker routes.
- The approved header/favicon motif is a text-free dancer silhouette: `assets/icons/furusho-mark.svg`. Its 160px embedded WebP is a web preview, not an editable vector or print master.
- Palette: navy `#07152F`, paper `#F5F2EA`, cream `#F7EDCF`, bright decorative turquoise `#08B9B9`. Readable text/link accent on light backgrounds: `#087478`.
- The brand approval record is on the **unmerged** `noritap/FURUSHO_PROFILE_OS` PR #36 branch: `05_BRAND_AND_MESSAGE/nonry_service_jr/BRAND_MARK_APPROVAL_20261118.md`. The original 1920px JPEG is not in GitHub main.
- Preserve the existing HTML/CSS structure; update canonical page styles instead of accumulating visual override layers.
- After each release verify public-content generation, navigation, media registry, deployed GitHub Pages and real user routes. A successful Actions run alone does not confirm viewport-specific visual QA.

## Source of Truth

- Website implementation: this repository
- Profile/evidence/publication control: `noritap/FURUSHO_PROFILE_OS`
- Project identity: `/PROJECT_PROFILE.md`

## Visual Asset Collector

`tools/collect_visual_assets.py` scans the public HTML and builds a visual-asset registry at:

```text
assets/data/media-assets.json
```

Default run:

```bash
python3 tools/collect_visual_assets.py
```

To also inspect external pages for `og:image` candidates:

```bash
python3 tools/collect_visual_assets.py --fetch-og
```

Preview without writing:

```bash
python3 tools/collect_visual_assets.py --stdout
```

The collector normalizes duplicate visual references:

- YouTube video links and `i.ytimg.com` / `img.youtube.com` thumbnail URLs resolve to one YouTube asset entry.
- Absolute `noritap.github.io/furusho-official/...` image URLs resolve back to the matching repository-local asset when possible.
- `generated_at` changes only when the actual registry content changes.

### Human review view

`tools/render_visual_asset_review.py` converts the JSON registry into a human-readable review file:

```text
.github/visual-asset-review.md
```

Run both generators locally with:

```bash
python3 tools/collect_visual_assets.py
python3 tools/render_visual_asset_review.py
```

The review file groups assets into:

- `REVIEW_REQUIRED`
- `MISSING_LOCAL_FILE`
- `AUTO_EXTERNAL_PREVIEW`
- `EXISTING_PUBLIC_ASSET`

This makes rights/context decisions visible without reading raw JSON.

### Automatic sync and validation

`.github/workflows/visual-asset-registry.yml` keeps both generated files synchronized.

- On pull requests, GitHub Actions regenerates the registry and review and fails if committed generated files are stale.
- On `main`, the workflow regenerates both files and commits only those generated files when their actual content changed.
- External OGP discovery is intentionally not part of every automatic run.
- Broader OGP discovery can be launched from **Actions → Visual Asset Registry Sync → Run workflow** with `fetch_og` enabled.

This keeps ordinary updates low-risk while still allowing broader candidate discovery when needed.

### Safety policy

The collector does **not** download or copy external images.

- Existing YouTube video links → `AUTO_EXTERNAL_PREVIEW`
- Repository-local images → indexed as `EXISTING_PUBLIC_ASSET`, but rights are not inferred
- Other remote images / fetched `og:image` → `REVIEW_REQUIRED`
- Unknown external assets are never promoted to auto-publish merely because they were discovered

The registry is discovery/routing metadata, not a copyright or licensing authority.

## Current structure

```text
/
├── PROJECT_PROFILE.md
├── README.md
├── index.html
├── profile/
├── career/
├── activities/
├── projects/
├── media/
├── contact/
├── assets/
│   ├── css/
│   ├── data/
│   │   └── media-assets.json
│   └── images/
├── .github/
│   ├── visual-asset-review.md
│   └── workflows/
│       └── visual-asset-registry.yml
└── tools/
    ├── navigation_audit.py
    ├── navigation_sync.py
    ├── collect_visual_assets.py
    └── render_visual_asset_review.py
```

## Current UX direction

The official site acts as a public routing hub rather than merging every business/project into one operation.

Primary routes:

1. Furusho personal/professional work requests
2. Rhythm Speaker studio services
3. Projects / activities / media
4. Career / profile evidence presentation

Visual previews should use verified existing media first. Missing assets remain typographic fallbacks until an approved image source is available.
