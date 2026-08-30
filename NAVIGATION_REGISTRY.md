# NAVIGATION_REGISTRY

Version: 1.0
Status: ACTIVE
Site: Furusho Official
Canonical Base URL: https://noritap.github.io/furusho-official/

## Purpose

古庄里好 Official Website の Global Navigation を1つの正本として管理し、ページ追加時の Navigation Drift を防ぐ。

## Global Navigation Contract

NAV_VERSION: FURUSHO-NAV-1

Order:
1. Profile — /furusho-official/profile/
2. Career — /furusho-official/career/
3. Activities — /furusho-official/activities/
4. Projects — /furusho-official/projects/
5. Media — /furusho-official/media/
6. Contact — /furusho-official/contact/

Brand / Home:
- 古庄里好 / Noritaka Furusho → /furusho-official/

Primary CTA:
- Contact

## Scope

このContractを継承するPrimary Pages:
- /
- /profile/
- /career/
- /activities/
- /projects/
- /media/
- /contact/

## Drift Definition

以下はNavigation Drift:
- Projectsが一部ページにしかない
- 項目順がページごとに違う
- Contactの役割がページごとに違う
- Homeへの戻り先が不統一
- 古いURLが残る

## Change Rule

Global Navigationを変更する場合:
1. 本Registryを先に更新
2. 全Scope Pageを同一NAV_VERSIONへ同期
3. Navigation Auditを実行
4. PASS後にmerge

ページ固有導線はGlobal Navigationを置き換えず、Local Navigationまたは本文CTAとして追加する。

## Current Baseline

2026-08-30 auditで、`/projects/` と `/activities/` はProjectsを含むが、旧ページ群に未同期箇所があることを確認。Baseline remediation完了までは Drift Known 状態として扱う。

## DONE CONDITION

- Scope全ページがGlobal Navigation Contractを満たす
- Navigation Auditがstrict modeでPASS
- 新規Primary Page追加時にRegistryへScope登録される
