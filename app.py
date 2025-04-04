from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# Initialize databases
def init_comment_db():
    conn = sqlite3.connect('comments.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS comments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            content TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def init_reply_db():
    conn = sqlite3.connect('replies.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS replies (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            content TEXT NOT NULL,
            comment_id INTEGER,
            FOREIGN KEY (comment_id) REFERENCES comments (id)
        )
    ''')
    conn.commit()
    conn.close()

# Initialize both databases
init_comment_db()
init_reply_db()

@app.route('/')
def index():
    # Fetch comments from the comments database
    conn = sqlite3.connect('comments.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM comments')
    comments = cursor.fetchall()
    conn.close()

    # Fetch replies from the replies database
    conn = sqlite3.connect('replies.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM replies')
    replies = cursor.fetchall()
    conn.close()

    # Organize replies by comment ID
    reply_dict = {}
    for reply in replies:
        if reply[2] not in reply_dict:
            reply_dict[reply[2]] = []
        reply_dict[reply[2]].append(reply)

    return render_template('index.html', comments=comments, reply_dict=reply_dict)

@app.route('/comment', methods=['POST'])
def comment():
    content = request.form['content']
    conn = sqlite3.connect('comments.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO comments (content) VALUES (?)', (content,))
    conn.commit()
    conn.close()
    return redirect('/')

@app.route('/reply/<int:comment_id>', methods=['POST'])
def reply(comment_id):
    content = request.form['content']
    conn = sqlite3.connect('replies.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO replies (content, comment_id) VALUES (?, ?)', (content, comment_id))
    conn.commit()
    conn.close()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
