# 設計書

## 基本設計

**概要:** ギャンブル予防チェックカレンダーアプリケーション。ユーザーはカレンダーから日付を選択し、その日のギャンブル状況を記録できる。また、過去のチェック結果を表示することができる。

**入力:** ユーザーが選択した日付、チェック結果

**出力:** チェック結果のデータベースへの保存、過去のチェック結果の表示

## 詳細設計

### 関数一覧
- {'name': 'setup_db', 'description': 'SQLiteデータベースを初期設定する関数。データベースに接続し、必要なテーブルが存在しない場合は作成する。', 'parameters': [], 'return': None}
- {'name': 'save_check_result', 'description': 'チェック結果をデータベースに保存する関数。指定された日付とチェック結果をデータベースに挿入する。', 'parameters': [{'name': 'date', 'type': 'TEXT', 'description': 'チェックを行った日付'}, {'name': 'result', 'type': 'TEXT', 'description': 'チェック結果'}], 'return': None}
- {'name': 'fetch_check_results', 'description': 'データベースからすべてのチェック結果を取得する関数。', 'parameters': [], 'return': '取得したチェック結果のリスト'}
- {'name': 'create_view_window', 'description': 'チェック結果を表示するビュー画面を作成する関数。過去のチェック結果をカレンダーに表示し、ギャンブルしなかった日を特別なスタイルで表示する。', 'parameters': [], 'return': None}
- {'name': 'create_ui', 'description': 'Tkinterを使用してUIを作成する関数。カレンダーとボタンを配置し、データの保存やビュー画面の表示を可能にする。', 'parameters': [], 'return': None}
- {'name': 'on_check_date_button_click', 'description': 'チェック日付保存ボタンがクリックされたときに呼び出される関数。選択された日付とチェック結果を保存する。', 'parameters': [], 'return': None}

### クラス一覧

### メモ
このアプリケーションは、SQLiteデータベースを使用してチェック結果を保存し、Tkinterを使用してGUIを構築している。ユーザーはカレンダーから日付を選択し、チェック結果を記録できる。過去のチェック結果は特別なスタイルで表示される。
