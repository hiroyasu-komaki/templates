"""
processor — 中核となる決定的な処理（抽出・変換・計算）を担う。

判断根拠となる数式・閾値は direction/ のドキュメントに対応させ、コードだけを
変えて根拠と乖離させないこと。ブラウザ側にロジックを移植する場合は
assets/js/logic.js と式を一致させる。
"""
from __future__ import annotations
from config import settings


def process(data: dict, params: dict | None = None) -> dict:
    """
    loader が検証したデータを受け取り、中核処理を行った結果を返す。

    params が None の場合は settings.DEFAULT_PARAMS を使う。

    TODO:
      - data に対する抽出・変換・計算を実装する
      - 結果を後段（reporter）が扱いやすい形で返す
    """
    params = params or settings.DEFAULT_PARAMS

    # TODO: 実際の処理を実装する
    result: dict = {"params": params, "items": []}
    return result
