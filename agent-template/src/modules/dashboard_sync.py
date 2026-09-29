"""
dashboard_sync — ブラウザダッシュボード（index.html）用の assets/js/data.js を
main.py のパイプライン実行と同時に再生成する。

loader が検証済みのデータと settings の既定値をそのまま書き出すため、ブラウザ側で
CSV/JSON を独自に二重パースする必要がなく、Python 側と表示データがずれない。
`assets/js/data.js` は自動生成物なので手で編集しないこと。
"""
from __future__ import annotations
import json
from pathlib import Path

from config import settings


def sync(data: dict, params: dict | None = None,
         out_path: Path | None = None) -> Path:
    """
    assets/js/data.js を再生成し、書き込んだパスを返す。

    - DEFAULT_PARAMS / FIXED_PARAMS: settings と同じ既定値をブラウザへ渡す。
    - DATA: loader 検証済みのデータを JS 側が読める形で埋め込む。

    TODO:
      - data をブラウザ側（logic.js）が期待する形へ整形する
    """
    out_path = out_path or settings.DATA_JS_PATH
    params = params or settings.DEFAULT_PARAMS

    lines = [
        "// このファイルは src/modules/dashboard_sync.py が",
        "// `python src/main.py` の実行時に input/ の内容から自動生成します。",
        "// 直接編集しないでください。",
        "",
        f"const DEFAULT_PARAMS = {json.dumps(params, ensure_ascii=False, indent=2)};",
        f"const FIXED_PARAMS = {json.dumps(settings.FIXED_PARAMS, ensure_ascii=False, indent=2)};",
        f"const DATA = {json.dumps(data, ensure_ascii=False, indent=2)};",
        "",
    ]

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text("\n".join(lines), encoding="utf-8")
    return out_path
