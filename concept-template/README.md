# concept-template — コンセプト資料の標準フォルダ構成

新しいテーマのコンセプト資料を起こすときの雛形です。
このフォルダをコピーしてテーマ名にリネームし、`{{ }}` の箇所を埋めていきます。

```bash
cp -R concept-template <concept-name>
```

既存フォルダ（`vmo/` `guardrails/` `multi-sourcing/` など）を作り直す必要はありません。
このテンプレートは**これから作るもの**に適用します。

---

## 1. フォルダ構成

```
<concept-name>/
├── README.md            ← そのコンセプトの説明（このファイルを書き換える）
├── .gitignore
│
├── chapters/            ← 【本体】資料の中身。章ごとに Markdown を分割
│   └── _chapter-template.md
│
├── proposal/            ← 【提案】意思決定者に出す成果物（企画書・スライド・試算）
│   └── _proposal-template.md
│
├── appendix/            ← 【補足】様式・算定根拠・理論的背景
│   └── _appendix-template.md
│
├── images/              ← chapters/ と proposal/ から参照する図版
│
├── index.html           ← 【公開】社内公開用トップページ（目次）
├── html/                ← index.html からリンクされる公開ページ
│   └── _page-template.html
└── assets/css/style.css ← index.html と html/ の共通スタイル
```

### 各フォルダの役割

| フォルダ | 何を置くか | 判断基準 |
|---|---|---|
| `chapters/` | 資料の本文。理論 → 診断 → 提言 → 運用、のように章立てして分割する | 「読み物」として通読される内容はここ |
| `proposal/` | 経営会議・委員会に提出する企画書、スライド（.pptx/.pdf）、効果試算（.xlsx） | 「提出物」として単体で完結するものはここ |
| `appendix/` | 業務様式、数式の定式化、スコアリング設計、設計思想の解説 | 本文に置くと流れを切るが、根拠として必要なもの |
| `images/` | 図版・グラフの画像ファイル | `chapters/` `proposal/` `html/` から相対パスで参照される |
| `html/` | `index.html` からリンクする公開ページ | 章の HTML 版。`chapters/` と 1:1 で対応させる |
| `assets/css/` | 共通スタイルシート | 色を変えるときは `style.css` の `:root` だけ書き換える |

### 必要になったときだけ作るフォルダ

以下は全コンセプトには不要なので、**最初は作らず、必要になった時点で下の名前で作成**します。
名前だけ標準化しておくことで、フォルダ間で意味がぶれないようにします。

| フォルダ | 用途 | 既存例 |
|---|---|---|
| `sources/` | 参照した外部フレームワーク・文献の要約 | `maturity/sources/`（IT-CMF ほか） |
| `sample/` | 記入済みサンプル、サンプルデータ（.md / .csv） | `guardrails/sample/`、`stage-gating/sample/` |
| `template/` | 読み手が複製して使うテンプレート | `maturity/template/`、`ppm/template/`、`raci/template/` |
| `data/` | 台帳・テーブル定義などの構造データ | `vmo/data/`、`rmo/data/` |
| `implementation/` | 実装検討（プロトタイプ、設計メモ、見積） | `multi-sourcing/implementation/` |
| `survey/` | アンケート設計・集計 | `guardrails/survey/` |

`_` で始まる雛形ファイル（`_chapter-template.md` など）は、実ファイルを作ったら削除して構いません。

---

## 2. 命名規則

既存フォルダで揺れていた点をここで揃えます。

| 対象 | ルール | 良い例 | 避ける例 |
|---|---|---|---|
| フォルダ名 | 小文字ケバブケース、単数/複数は上表に従う | `images/` `chapters/` | `image/` `Chapters/` |
| 章ファイル | `NN_kebab-case.md`（2桁ゼロ埋め、01 始まり） | `01_problem.md` | `1. problem.md` `1_problem.md` |
| 公開ページ | 対応する章と同じ連番・同じ主題 | `html/01_problem.html` | `html/Problem.html` |
| 図版 | `NN_内容.png`（参照する章の番号を接頭に） | `03_npv-irr-3years.png` | `グラフ4.png` |
| 提案書 | `<concept-name>_proposal.md` / `.pptx` / `.pdf` | `multi-sourcing_proposal.md` | `施策企画書.md` |
| 付録 | `A_` `B_` … または `form1_` `form2_` | `A_mathematical-formulation.md` | `付録1.md` |
| 言語違い | 末尾に `_ja` / `_en` | `maturity_01_governance_en.md` | `maturity EN.md` |

**共通の約束**

- ファイル名に日本語・空白は使わない（相対パス参照とツール連携が壊れやすいため）。見出しやタイトルは日本語で構いません。
- 同一内容の Markdown / PPTX / PDF は**同じベース名**にする（例：`maturity.md` / `maturity.pptx` / `maturity.pdf`）。どれが正本かは README に書く。
- `.DS_Store` は `.gitignore` 済み。

---

## 3. 新しいコンセプトを作る手順

1. **複製する** — `cp -R concept-template <concept-name>`
2. **README.md を書き換える** — テンプレートの説明を消し、下の「README に必ず書くこと」を埋める
3. **chapters/ を書く** — `_chapter-template.md` を複製して `01_...md` から順に
4. **図版を images/ に置く** — 章から相対パス `../images/xxx.png` で参照
5. **proposal/ を作る** — 提出先が決まったら `_proposal-template.md` を複製
6. **必要なら appendix/ と公開 HTML** — 様式や算定根拠が出てきた時点で
7. **不要なフォルダと `_` 雛形を削除する** — 空フォルダを残さない

### README に必ず書くこと

各コンセプトの README には、最低限この3つを書きます（`multi-sourcing/README.md` が参考になります）。

1. **1段落の概要** — 何を扱い、何を扱わないか
2. **ディレクトリツリー** — 各ファイルに1行の説明を添えたもの
3. **どれが正本か / どこから読むか** — 同じ内容が複数形式であるとき、どれを更新すべきか

---

## 4. 章立ての型

既存のコンセプトはおおむねこの流れになっています。テーマによって取捨してください。

| # | 章 | 中身 |
|---|---|---|
| 00 | 理論 | 依拠する理論・フレームワーク。なぜこの見方をするのか |
| 01 | 診断 | 現状の構造的問題。数字と事実 |
| 02 | 提言 | 打ち手の設計。制度・プロセスとして書く |
| 03 | 判断基準 | 誰が何を根拠に判断するか（RACI・ゲート・スコアリング） |
| 04 | 運用 | 定着させる仕組み。KPI・レビューサイクル |
| 05 | ロードマップ | 段階的な移行計画 |

---

## 5. スタイルの調整

`assets/css/style.css` の先頭 `:root` にある色変数だけを書き換えれば、コンセプトごとの見た目を変えられます。

```css
:root {
  --navy: #12305e;  /* 見出し・アクセント色 */
  --ink:  #1b2430;  /* 本文 */
  --bg:   #eef1f5;  /* 背景 */
}
```

日英併記が不要な場合は、`index.html` の `.lang` ブロック・`<script>`・`data-en` 属性を削除してください。
