/*
 * logic.js — ダッシュボードの計算ロジック（スキャフォールド）。
 *
 * Python 側（src/modules/processor.py）のロジックをブラウザに移植する場合は、
 * 式・閾値を一致させること（direction/ のドキュメントが根拠の正）。
 * data.js の DEFAULT_PARAMS / FIXED_PARAMS / DATA を入力として使う。
 */

// UIで動かせるパラメータ（params）を受け取り、DATA を処理して結果配列を返す。
function compute(params) {
  const items = (DATA.items || []).map((item) => {
    // TODO: item と params から必要な指標を計算する
    return { ...item };
  });

  // TODO: 並べ替え・フィルタなど
  return items;
}
