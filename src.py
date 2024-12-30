import sqlite3
from tkinter import Tk, Button, messagebox
from tkcalendar import Calendar

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

# チェック結果を取得して表示
def fetch_check_results():
    conn = sqlite3.connect('gambling_prevention.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM checks')
    results = cursor.fetchall()

    # 結果を表示
    for row in results:
        print(f"Date: {row[1]}, Result: {row[2]}")
    
    conn.close()

# チェック結果をバックグラウンドで保存
def save_data_in_background(date, result):
    save_check_result(date, result)
    messagebox.showinfo("Success", f"Data for {date} saved successfully!")

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
        # データをバックグラウンドで保存
        save_data_in_background(selected_date, result)

    check_button = Button(root, text="Save Check for Selected Date", command=on_check_date_button_click)
    check_button.pack(pady=10)

    # 終了ボタンを作成
    quit_button = Button(root, text="Quit", command=root.quit)
    quit_button.pack(pady=10)

    # Tkinterのメインループを開始
    root.mainloop()

if __name__ == '__main__':
    # UIを作成して実行
    create_ui()

    # データベースの内容を表示（オプション）
    fetch_check_results()
