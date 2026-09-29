/*
 * main.js — UIコントロールと計算(logic.js)・描画(ui.js)を結線する。
 *
 * ダッシュボードで動かせるパラメータは意図的に絞ること。説明が難しい値は
 * FIXED_PARAMS として固定表示にとどめ、UIには露出しない。
 */

let currentParams = { ...DEFAULT_PARAMS };

// パラメータを反映して再計算 → 再描画する。
function recompute() {
  const rows = compute(currentParams);
  renderTable(rows);
  renderKpis(rows, currentParams);
}

function init() {
  currentParams = { ...DEFAULT_PARAMS };
  renderControls(currentParams);

  // TODO: 各コントロールに change/input リスナを付け、
  //       currentParams を更新して recompute() を呼ぶ。

  recompute();
}

document.addEventListener("DOMContentLoaded", init);
