"""
reporter — processor の結果から output/ 向けの成果物を生成する。

出力フォーマットは direction/ の出力仕様に対応させる。人が読んで判断できる形
（根拠が追える形）で書き出すこと。
"""
from __future__ import annotations


def build_report(result: dict) -> str:
    """
    processor の結果を受け取り、レポート文字列（Markdown 等）を組み立てて返す。

    TODO:
      - 見出し・要約・明細など、direction/ の出力仕様に沿って組み立てる
      - 各判断の根拠を追える形にする
    """
    lines: list[str] = []
    lines.append("# {レポートタイトル}")
    lines.append("")
    # TODO: result の内容を整形して追記する
    return "\n".join(lines)
