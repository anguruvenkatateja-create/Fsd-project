from flask import render_template, request, redirect, url_for, flash, current_app, session
from . import database

@current_app.route('/')
def index():
    """Student View: Complaint Form."""
    return render_template('index.html')

@current_app.route('/submit_complaint', methods=['POST'])
def submit_complaint():
    """Saves student complaint to MySQL."""
    name = request.form.get('name')
    room = request.form.get('room')
    issue = request.form.get('issue')

    try:
        conn = database.get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO complaints (name, room, issue) VALUES (%s, %s, %s)", (name, room, issue))
        conn.commit()
        cursor.close()
        conn.close()
        flash("Complaint submitted successfully!", "success")
    except Exception as e:
        flash(f"Database Error: {str(e)}", "error")
    return redirect(url_for('index'))

@current_app.route('/admin/login', methods=['GET', 'POST'])
def admin_login():
    """Admin Login Page."""
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # Default Credentials
        if username == 'admin' and password == 'hostel123':
            session['admin_logged_in'] = True
            return redirect(url_for('admin_dashboard'))
        else:
            flash("Invalid credentials!", "error")
            
    return render_template('login.html')

@current_app.route('/admin')
def admin_dashboard():
    """Admin Dashboard: View all complaints."""
    if not session.get('admin_logged_in'):
        return redirect(url_for('admin_login'))

    try:
        conn = database.get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM complaints ORDER BY id DESC")
        complaints = cursor.fetchall()
        cursor.close()
        conn.close()
        return render_template('admin.html', complaints=complaints)
    except Exception as e:
        return f"Error: {str(e)}"

@current_app.route('/logout')
def logout():
    session.pop('admin_logged_in', None)
    return redirect(url_for('index'))