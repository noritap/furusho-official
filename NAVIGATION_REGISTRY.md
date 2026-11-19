# NAVIGATION_REGISTRY

Version: 1.2
Status: ACTIVE
Site: Furusho Official
Canonical Base URL: https://noritap.github.io/furusho-official/

## Purpose

古庄里好 Official Website の Global Navigation を1つの正本として管理し、ページ追加・UX更新時の Navigation Drift を防ぐ。

## Global Navigation Contract

NAV_VERSION: FURUSHO-NAV-3

1. プロフィール — /furusho-official/profile/
2. 経歴・実績 — /furusho-official/career/
3. 映像・写真 — /furusho-official/media/
4. 活動 — /furusho-official/projects/
5. 仕事の相談 — /furusho-official/contact/

ロゴはトップへ戻る。スマートフォンでも同じ項目をメニューから開ける。
現在のページに対応するリンクには `aria-current="page"` を付ける。
旧 /activities/ は統合先への案内として共通メニューを表示する。

## Change Rule

Global Navigationを変更する場合:
1. 本Registryを先に更新
2. `tools/navigation_sync.py` で全Scope Pageを同一Contractへ同期
3. `tools/navigation_audit.py --strict` を実行
4. Navigation Contract Sync Checkで生成差分が0であることを確認
5. PASS後にmerge

ページ固有導線はGlobal Navigationを置き換えず、Local Navigationまたは本文CTAとして追加する。

## Automation

- `tools/navigation_sync.py` = Canonical NavigationをPrimary HTMLへ生成・同期
- `tools/navigation_audit.py --strict` = Required Navigationの欠落・順序・URL Driftを検出しFAIL
- `.github/workflows/navigation-sync.yml` = PR上で生成結果との差分を検査
- `.github/workflows/navigation-audit.yml` = PR / mainでstrict auditを実行
