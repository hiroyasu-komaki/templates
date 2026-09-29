# {エージェント名} エージェント with Claude Code

{このエージェントが何をするかを1〜2文で書く}

## 前提条件

- Claude Pro / Max / Teams / Enterprise アカウント
- Claude Code（ネイティブインストーラー推奨）
- Python 3.10+

## セットアップ

```bash
# 1. Claude Code のインストール
curl -fsSL https://claude.ai/install.sh | bash

# 2. プロジェクトフォルダに移動
cd ~/Documents/03_agents/{フォルダ名}

# 3. Python 仮想環境の構築
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt

# 4. Claude Code を起動（初回認証）
claude
```

## プロジェクト構成

```
{フォルダ名}/
├── .claude/commands/   ← Skills（カスタムコマンド）の定義
├── src/
│   ├── main.py         ← Python エントリポイント（input→mid→output パイプライン）
│   ├── config/         ← Python 用の設定（パス定数・既定パラメータ）
│   └── modules/        ← パイプラインを構成する処理単位（loader/processor/reporter/dashboard_sync）
├── direction/          ← スキル仕様・参照ドキュメント（判断基準・出力テンプレート等）
├── input/              ← 処理対象のファイルを置く場所
├── mid/                ← 中間ファイル（抽出結果・加工中のデータ）
├── output/             ← 最終成果物
├── index.html          ← ブラウザ用ダッシュボード（任意。不要なら削除可）
├── assets/
│   ├── css/style.css   ← ダッシュボードのスタイル
│   └── js/             ← data.js（自動生成）/ logic.js / ui.js / main.js
├── .venv/
├── requirements.txt
├── CLAUDE.md
└── README.md
```

> ダッシュボード（`index.html` + `assets/`）は任意のレイヤーです。画面表示が不要な
> エージェントでは `index.html` / `assets/` / `src/modules/dashboard_sync.py` を削除し、
> `main.py` から `dashboard_sync` の呼び出しを外してください。

## 使い方

`input/` にファイルを置いてから、Claude Code でスキルを実行する。

### 1. {スキル名}

```
/{コマンド名}
```

{何をするスキルか}

- 出力: `output/{ファイル名パターン}`
- 内容: {出力に含まれる内容}

Python パイプラインを直接動かす場合：

```bash
.venv/bin/python src/main.py run --input input/<ファイル名>
```

input → mid → output の処理に加え、ダッシュボード用の `assets/js/data.js` まで
自動同期する。処理後は `index.html` をブラウザで開いて結果を確認できる。

## アーキテクチャ

```
Skills が手順を定義
    → Claude Code が Python を実行
        → Python がファイル処理・データ変換を担当（config / modules）
            → dashboard_sync が assets/js/data.js を同期（ブラウザ表示用）
                → Claude Code が分析・判断・生成を担当
```

- **Skills**（`.claude/commands/`）— Claude Code への指示書。処理手順を定義する。
- **Python**（`src/`）— ファイル処理・データ変換。決定的な処理を担う道具。
  - `src/config/` — パス定数・既定パラメータ。数値の調整はコードでなくここで行う。
  - `src/modules/` — `loader`（読込・検証）→ `processor`（中核処理）→
    `reporter`（成果物生成）→ `dashboard_sync`（`assets/js/data.js` 同期）。
- **direction/** — 各スキルの判断基準・出力フォーマットを定義するドキュメント。
  数式・閾値を変えるときはコードと direction/ を両方更新し、乖離させない。
- **ダッシュボード**（`index.html` + `assets/`）— `data.js` は自動生成物（手編集禁止）。
  `logic.js` に Python 側のロジックを移植する場合は式を一致させる。
- **Claude Code** — Skills の手順に従い Python を実行し、結果を分析・判断・生成する頭脳。

## 注意事項

- Claude Code の利用には Pro 以上の有料プランが必要（追加の API 課金は不要）
- {成果物の性質に関する注意（参考情報である、専門家への相談を推奨する等）があれば記載}
