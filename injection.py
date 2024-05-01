import sqlite3

def login(username, password):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    query = "SELECT * FROM users WHERE username = '" + username + "' AND password = '" + password + "'"
    c.execute(query)
    result = c.fetchone()
    conn.close()
    return result

username = input("請輸入使用者名稱：")
password = input("請輸入密碼：")

user = login(username, password)

if user:
    print("登入成功！")
else:
    print("登入失敗！")