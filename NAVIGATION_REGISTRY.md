# NAVIGATION_REGISTRY

Version: 1.2
Status: ACTIVE
Site: Furusho Official
Canonical Base URL: https://noritap.github.io/furusho-official/

## Purpose

古庄里好 Official Website の Global Navigation を1つの正本として管理し、ページ追加・UX更新時の Navigation Drift を防ぐ。

## Global Navigation Contract

NAV_VERSION: FURUSHO-NAV-2

Order:
1. About — /furusho-official/#about
2. Work — /furusho-official/#work
3. Projects — /furusho-official/projects/
4. Career — /furusho-official/career/
5. Contact — /furusho-official/contact/

Brand / Home:
- 古庄里好 / Noritaka Furusho → /furusho-official/

Primary CTA:
- Contact

## UX Intent

Global Navigation は「サイト内の全ページ名を列挙する目次」ではなく、初見ユーザーが主要目的へ最短で進むための5導線とする。

- About = HOME内の人物理解導線
- Work = HOME内の古庄個人への依頼導線
- Projects = 活動・企画・制作物の集約導線
- Career = 主な出演・振付・実績導線
- Contact = 問い合わせ導線

以下の既存Primary Pageは削除しないが、Global Navigationの独立項目にはしない。

- /profile/ = Aboutから到達する詳細プロフィール
- /activities/ = Projects / 本文導線から到達する活動詳細
- /media/ = Career / Projects / 本文導線から到達するMedia詳細

## Scope

このContractを継承するPrimary Pages:
- /
- /profile/
- /career/
- /activities/
- /projects/
- /media/
- /contact/

## Current-page Rule

`aria-current="page"` は、Global Navigationに独立項目を持つ以下のページだけに付与する。

- /projects/ → Projects
- /career/ → Career
- /contact/ → Contact

/profile/ /activities/ /media/ はGlobal Navigation項目ではないため、Global Navigation上ではcurrentを付けない。

## Drift Definition

以下はNavigation Drift:
- 5項目の欠落
- 項目順の不一致
- About / WorkがHOME内Anchor以外へ向く
- Projects / Career / ContactのURL不一致
- Contact CTAの役割がページごとに違う
- Brand / Homeの戻り先が不統一
- 旧FURUSHO-NAV-1の6項目構成がPrimary Pageに残る

## Change Rule

Global Navigationを変更する場合:
1. 本Registryを先に更新
2. `tools/navigation_sync.py` で全Scope Pageを同一Contractへ同期
3. `tools/navigation_audit.py --strict` を実行
4. Navigation Contract Sync Checkで生成差分が0であることを確認
5. PASS後にmerge

ページ固有導線はGlobal Navigationを置き換えず、Local Navigationまたは本文CTAとして追加する。

## Current Baseline

2026-09-16 UX v2 alignmentでGlobal Navigationを `FURUSHO-NAV-2` へ更新。
HOMEで先行採用していた `About / Work / Projects / Career / Contact` を正式Contract化し、Profile / Activities / Mediaは詳細ページとして保持する。

## Automation

- `tools/navigation_sync.py` = Canonical NavigationをPrimary HTMLへ生成・同期
- `tools/navigation_audit.py --strict` = Required Navigationの欠落・順序・URL Driftを検出しFAIL
- `.github/workflows/navigation-sync.yml` = PR上で生成結果との差分を検査
- `.github/workflows/navigation-audit.yml` = PR / mainでstrict auditを実行

## DONE CONDITION

- Scope全ページがFURUSHO-NAV-2を満たす
- Navigation Auditがstrict modeでPASS
- Navigation Sync Checkで未コミット差分が0
- Profile / Activities / Mediaへの本文導線を保持する
- 新規Primary Page追加時にRegistryへScope登録される
