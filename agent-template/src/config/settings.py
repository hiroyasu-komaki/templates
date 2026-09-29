"""
settings — プロジェクト全体で参照する設定を集約する。

パス定数と既定パラメータをここに置くことで、各モジュールがディレクトリ構成や
チューニング値をハードコードせずに済む。数値の調整はコードではなくここ
（または input/ 配下の設定ファイル）で行う方針。

ここに定義した DEFAULT_PARAMS は dashboard_sync 経由で assets/js/data.js にも
書き出され、ブラウザ側（logic.js）と同じ既定値を共有できる。
"""
from __future__ import annotations
from pathlib import Path

# ---- パス定数 -------------------------------------------------------------
# settings.py = <ROOT>/src/config/settings.py なので parents[2] がプロジェクトルート。
ROOT = Path(__file__).resolve().parents[2]

INPUT_DIR = ROOT / "input"
MID_DIR = ROOT / "mid"
OUTPUT_DIR = ROOT / "output"
ASSETS_DIR = ROOT / "assets"
DATA_JS_PATH = ASSETS_DIR / "js" / "data.js"


# ---- 既定パラメータ -------------------------------------------------------
# {エージェント固有のチューニング値をここに定義する}。
# ブラウザ側（logic.js）と一致させたい値は dashboard_sync がここから data.js へ
# 書き出す。UIで露出したくない固定値は FIXED_PARAMS に分けておく。
DEFAULT_PARAMS: dict = {
    # "example_threshold": 0.5,
}

# UIで調整させず固定表示にとどめるパラメータ（説明が難しい値など）。
FIXED_PARAMS: dict = {
    # "example_fixed": 1.0,
}
