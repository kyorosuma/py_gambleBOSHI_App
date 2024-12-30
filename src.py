import sqlite3
from tkinter import Tk, Button, messagebox, Toplevel
from tkcalendar import Calendar
from datetime import datetime

# SQLiteデータベースの設定
def setup_db():
    # データベースに接続（なければ作成されます）
    conn = sqlite3.connect('gambling_prevention.db')
    cursor = conn.cursor()

    # テーブルが存在しない場合は新しく作成
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS checks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            check_result TEXT NOT NULL
        )
    ''')

    # コミットしてデータベースに変更を反映
    conn.commit()
    conn.close()

# チェック結果をデータベースに保存
def save_check_result(date, result):
    conn = sqlite3.connect('gambling_prevention.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO checks (date, check_result) VALUES (?, ?)
    ''', (date, result))
    conn.commit()
    conn.close()

# チェック結果を取得
def fetch_check_results():
    conn = sqlite3.connect('gambling_prevention.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM checks')
    results = cursor.fetchall()
    conn.close()
    return results

# チェック結果を表示するビュー画面を作成
def create_view_window():
    # 新しいウィンドウを作成
    view_window = Toplevel()
    view_window.title("View Gambling Prevention Checks")

    # 新しいカレンダーを作成
    cal = Calendar(view_window, selectmode='none', date_pattern='yyyy-mm-dd')
    cal.pack(pady=20)

    # チェック結果を取得
    results = fetch_check_results()

    # ギャンブルしなかった日（"No gambling today"）を黒塗りにする
    for row in results:
        date_str = row[1]  # 文字列の日付
        result = row[2]
        if result == "No gambling today":
            # 文字列の日付をdatetime.date型に変換
            date_obj = datetime.strptime(date_str, '%Y-%m-%d').date()

            # 日付にイベントを追加して、黒塗りに設定
            cal.calevent_create(date_obj, "No Gambling", tags="no_gambling")
            cal.tag_config("no_gambling", background="black", foreground="white")
    
    # ビューウィンドウを表示
    view_window.mainloop()

# TkinterでUIを作成
def create_ui():
    root = Tk()
    root.title("Gambling Prevention Check Calendar")

    # SQLiteデータベースの初期設定
    setup_db()

    # カレンダーを作成
    cal = Calendar(root, selectmode='day', date_pattern='yyyy-mm-dd')
    cal.pack(pady=20)

    # データを保存するボタン
    def on_check_date_button_click():
        selected_date = cal.get_date()  # カレンダーで選択した日付
        result = "No gambling today"  # チェック結果（仮）
        # データを保存
        save_check_result(selected_date, result)

    check_button = Button(root, text="Save Check for Selected Date", command=on_check_date_button_click)
    check_button.pack(pady=10)

    # ビュー画面を表示するボタン
    view_button = Button(root, text="View Checks", command=create_view_window)
    view_button.pack(pady=10)

    # 終了ボタンを作成
    quit_button = Button(root, text="Quit", command=root.quit)
    quit_button.pack(pady=10)

    # Tkinterのメインループを開始
    root.mainloop()

if __name__ == '__main__':
    # UIを作成して実行
    create_ui()
