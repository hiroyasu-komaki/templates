"""
main.py — {エージェント名} の Python エントリポイント。

パイプライン:
  input/ の対象ファイル
    -> [loader]        読み込み・検証
    -> [processor]     中核処理（抽出・変換・計算）      -> mid/
    -> [reporter]      成果物生成                        -> output/
    -> [dashboard_sync] index.html 用データ同期          -> assets/js/data.js

Skills（.claude/commands/）から呼び出される処理の実体。Claude が判断・生成を行い、
Python はファイル処理やデータ変換など決定的な処理を担当する。

使い方:
    .venv/bin/python src/main.py run --input input/<ファイル名>
"""
from __future__ import annotations
import argparse
import sys
from pathlib import Path

# src/ を import パスへ追加し、config / modules をパッケージとして解決する。
SRC_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SRC_DIR))

from config import settings                                    # noqa: E402
from modules import loader, processor, reporter, dashboard_sync  # noqa: E402


def cmd_run(args: argparse.Namespace) -> int:
    """input → mid → output → dashboard の一連を実行する。"""
    settings.MID_DIR.mkdir(exist_ok=True)
    settings.OUTPUT_DIR.mkdir(exist_ok=True)

    # 1) 読み込み・検証
    try:
        data = loader.load(Path(args.input))
    except loader.InputError as e:
        print(f"[入力エラー] {e}", file=sys.stderr)
        return 1

    # 2) 中核処理 -> mid/
    result = processor.process(data)
    # TODO: 中間結果を mid/ に保存する

    # 3) レポート -> output/
    report = reporter.build_report(result)
    # TODO: report を output/ に保存する（例: output/report_YYYYMMDD.md）
    _ = report

    # 4) ダッシュボード用データを同期 -> assets/js/data.js
    data_js_path = dashboard_sync.sync(data)
    print(f"完了。ダッシュボードデータ同期 -> {data_js_path.relative_to(settings.ROOT)}")

    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="{エージェント名}")
    sub = parser.add_subparsers(dest="command", required=True)

    p_run = sub.add_parser("run", help="パイプラインを実行する")
    p_run.add_argument("--input", default=str(settings.INPUT_DIR),
                       help="処理対象の入力パス")
    p_run.set_defaults(func=cmd_run)

    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
