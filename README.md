# 設計書

## 基本設計

**概要:** このプログラムは、Python のコードファイルを解析し、関数・クラスの情報を抽出して設計書を自動生成するシステムです。解析結果をもとに、設計書を GitHub で管理しやすい形式（README.md）に出力します。

**入力:** 解析対象の Python ファイル (.py) のパスを入力

**出力:** README.md 形式の設計書ファイル（関数・クラスの詳細を含む）

**使用技術:** Python 3.x, OpenAI API, 正規表現, JSON 処理

**主要ライブラリ:** os, json, openai, re, time, random

## 詳細設計

### 関数一覧
- **setup_db**: SQLiteデータベースの初期設定を行う関数。データベースに接続し、テーブルが存在しない場合は新しく作成する。
- **save_check_result**: チェック結果をデータベースに保存する関数。指定された日付と結果をデータベースに挿入する。
- **fetch_check_results**: データベースからチェック結果を取得する関数。すべての結果を取得して返す。
- **create_view_window**: チェック結果を表示するビュー画面を作成する関数。データベースから結果を取得し、カレンダーに表示する。
- **create_ui**: Tkinterを使用してUIを作成する関数。メインウィンドウにカレンダーやボタンを配置し、各種操作を可能にする。
- **on_check_date_button_click**: データを保存するボタンがクリックされた際に呼び出される関数。選択された日付と結果を保存する。

### クラス一覧

### メモ
各関数は、データベース操作やUI作成など特定の機能を担当しており、単一の責務を持つように設計されている。UI関連の関数はTkinterを使用してウィンドウやボタンを操作する。データベース関連の関数はSQLiteを使用してデータの保存や取得を行う。
