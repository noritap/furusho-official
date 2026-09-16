# FURUSHO OFFICIAL UX/UI v2 PLAN

Version: 1.1
Status: IMPLEMENTED
Updated: 2026-09-16

## Goal

古庄里好 Official Website を「プロフィールを読むサイト」から「訪問目的を判断し、正しい依頼先へ迷わず進める公式ハブ」へ更新する。

## Primary UX problems

1. Profile / Career / Activities / Projects / Media が同列で、初見ユーザーが次に押す場所を判断しにくい。
2. 古庄本人への仕事依頼と Rhythm Speaker のスタジオサービスの境界がホーム上で十分に見えない。
3. スマートフォンでは横スクロール型ナビゲーションへの依存が大きい。
4. Contact CTA は存在するが、依頼可能領域を理解してから相談する導線が弱い。

## v2 information architecture

HOME の優先順位：

1. WHO — 古庄里好は誰か
2. ROUTE — 何を探しているか
3. WORK WITH ME — 古庄本人へ依頼できる領域
4. CAREER — 実績確認
5. PROJECTS / ACTIVITIES — 現在の活動
6. MEDIA — 外部メディア
7. CONTACT — 問い合わせ

## Request routing

### 古庄本人への依頼
- タップダンスレッスン・ワークショップ
- インストラクター関連の依頼
- スタジオ運営コンサルティング
- 音楽制作

### Rhythm Speaker
- Studioが公式に提供するレッスン
- Studio利用・予約等

料金・対応地域・契約条件・納期など未確定事項はHOMEで補完しない。

## Implemented UI changes

- primary navigationを About / Work / Projects / Career / Contact へ簡略化
- Hero直下に START HERE routingを追加
- Work With Meを追加し、古庄個人への依頼領域を明示
- Rhythm SpeakerへのStudio導線を別ルートとして明示
- Mobileではheader navigationをContact中心に簡略化
- Mobile bottom action barを追加
- tap targetを原則44px以上へ拡張
- skip link / focus-visible / reduced-motion supportを追加
- 既存Career / Media / profile image / metadataを保持
- JavaScriptなしで利用可能なStatic HTML構成を維持

## Success criteria

- 初見で古庄本人への依頼領域が理解できる
- Rhythm Speakerへの問い合わせ誤送信を減らす
- HomeからContactまで1–2 actionで到達できる
- Mobileで横スクロールナビへの依存をなくす
- PUBLIC-safe wordingだけで依頼カテゴリを表示する

## Implementation files

- `index.html`
- `assets/css/style.css`

Public implementation Source of Truth:
- GitHub `main` of `noritap/furusho-official`
