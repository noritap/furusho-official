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
└── tools/
    ├── navigation_audit.py
    ├── navigation_sync.py
    └── collect_visual_assets.py
```

## Current UX direction

The official site acts as a public routing hub rather than merging every business/project into one operation.

Primary routes:

1. Furusho personal/professional work requests
2. Rhythm Speaker studio services
3. Projects / activities / media
4. Career / profile evidence presentation

Visual previews should use verified existing media first. Missing assets remain typographic fallbacks until an approved image source is available.
