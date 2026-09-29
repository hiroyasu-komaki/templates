/*
 * ui.js — DOM 描画（スキャフォールド）。
 * logic.js の計算結果を画面に反映する。ロジック本体には触れず表示だけを担当する。
 */

const $ = (id) => document.getElementById(id);

// 操作パネルの初期値を描画する。
function renderControls(params) {
  // TODO: params を各コントロールの初期値に反映する
}

// KPI / サマリーを描画する。
function renderKpis(rows, params) {
  // TODO: 主要指標を計算して表示する
}

// 結果テーブルを描画する。
function renderTable(rows) {
  const tbody = $("mainTable").querySelector("tbody");
  tbody.innerHTML = rows
    .map((r) => {
      // TODO: 行のセルを組み立てる
      return `<tr><td>${r.name ?? ""}</td></tr>`;
    })
    .join("");
}
