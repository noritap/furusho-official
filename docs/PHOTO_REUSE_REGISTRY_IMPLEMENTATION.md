# Photo Reuse Registry Implementation

Status: READY

The owner-authorized source registry is now canonical at `tools/approved_remote_image_sources.json`.

Next implementation step: teach `tools/collect_visual_assets.py` to read this registry before falling back to `REVIEW_REQUIRED`, then regenerate `assets/data/media-assets.json` and `.github/visual-asset-review.md` through the existing workflow.

This keeps authorization explicit and data-driven instead of hard-coding a blanket exception for all remote images.
