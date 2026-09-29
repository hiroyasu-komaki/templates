# CLAUDE.md

このファイルは Claude Code がリポジトリで作業する際のガイドです。

## ディレクトリの役割

| ディレクトリ | 用途 |
|-------------|------|
| `input/` | 入力ファイルの置き場所。{何を置くか} |
| `mid/` | 中間ファイル。{何が入るか（ファイル名パターン）} |
| `output/` | 最終出力。{何が保存されるか（ファイル名パターン）} |
| `src/` | Python ソースコード。`main.py` がエントリポイント。Skills から呼び出される処理の実体。 |
| `src/config/` | Python 用の設定（`settings.py`：パス定数・既定パラメータ）。数値調整はここで行う。 |
| `src/modules/` | パイプラインを構成する処理単位（loader / processor / reporter / dashboard_sync）。 |
| `direction/` | スキル仕様・参照ドキュメント。各スキルの判断基準や出力フォーマット定義。 |
| `.claude/commands/` | Skills（カスタムコマンド）の定義。Markdown ファイル 1 つが 1 つの Skill。 |
| `index.html` / `assets/` | ブラウザ用ダッシュボード（任意）。`assets/js/data.js` は `dashboard_sync` が自動生成する（手編集禁止）。 |

## Python 実行ルール

Python は必ず仮想環境内で実行すること。コマンドは `.venv/bin/python` を直接指定する。

```bash
# ✅ 正しい（仮想環境のPythonを直接指定）
.venv/bin/python src/main.py {サブコマンド}

# ❌ 避ける（activate 忘れのリスクがある）
python src/main.py {サブコマンド}
```

パッケージの追加も仮想環境内で行う：

```bash
.venv/bin/pip install <パッケージ名>
.venv/bin/pip freeze > requirements.txt
```

## Python コマンド（src/main.py）

```bash
.venv/bin/python src/main.py run --input input/<ファイル名>   # input→mid→output と assets/js/data.js 同期
```

パイプラインの実体は `src/modules/`（loader→processor→reporter→dashboard_sync）、
設定は `src/config/settings.py`。数式・閾値を変えるときはコードと `direction/` を
両方更新し、ブラウザ側に移植したロジック（`assets/js/logic.js`）とも一致させること。

## カスタムコマンド（Skills）

`.claude/commands/` に定義済み。`/コマンド名` で呼び出せる。

| コマンド | 主な入力 | 主な出力 | 動作概要 |
|---------|---------|---------|---------|
| `/{コマンド名}` | `input/*` | `output/*` | {処理内容} |
