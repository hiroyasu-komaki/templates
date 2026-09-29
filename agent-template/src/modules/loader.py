"""
loader — input/ の対象ファイルを読み込み、検証する。

入力規律をここで強制する（必須項目の欠落・型・値域を検査し、違反したら
InputError で処理を止める）。検証済みのデータだけを後段へ渡すことで、
processor / dashboard_sync が生データを二重にパースせずに済む。
"""
from __future__ import annotations
from pathlib import Path


class InputError(Exception):
    """入力データの規律違反。処理を止めるべきエラー。"""


def load(path: Path) -> dict:
    """
    input/ のファイルを読み込んで検証し、後段が扱いやすい形（dict / list）で返す。

    TODO:
      - ファイル存在チェック（無ければ InputError）
      - 必須フィールド・型・値域の検証
      - 検証済みデータを返す
    """
    if not path.exists():
        raise InputError(f"入力ファイルが見つかりません: {path}")

    # TODO: 実際の読み込み・検証を実装する
    data: dict = {}
    return data
