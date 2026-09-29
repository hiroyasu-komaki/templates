"""
modules パッケージ — main.py のパイプラインを構成する処理単位。

    loader        input/ の読み込み・検証
    processor     決定的な中核処理（抽出・変換・計算）
    reporter      output/ 向けの成果物生成
    dashboard_sync ブラウザ用 assets/js/data.js の同期

各モジュールは単機能に保ち、main.py が input → mid → output の順に呼び出す。
"""
from . import loader, processor, reporter, dashboard_sync

__all__ = ["loader", "processor", "reporter", "dashboard_sync"]
