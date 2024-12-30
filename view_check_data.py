import sqlite3

# チェック結果を取得して表示
def fetch_check_results():
    # データベースに接続
    conn = sqlite3.connect('gambling_prevention.db')
    cursor = conn.cursor()

    # チェック結果をすべて取得
    cursor.execute('SELECT * FROM checks')
    results = cursor.fetchall()

    # 結果を表示
    if results:
        print(f"{'ID':<5}{'Date':<15}{'Check Result'}")
        print("-" * 40)
        for row in results:
            print(f"{row[0]:<5}{row[1]:<15}{row[2]}")
    else:
        print("No data found.")

    # データベース接続を閉じる
    conn.close()

# チェック結果を表示
fetch_check_results()
