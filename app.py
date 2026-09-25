from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

# Temporary storage for expenses
expenses = []

# Home route
@app.route('/')
def home():
    return render_template('home.html')

# Add Expense route
@app.route('/add', methods=['GET', 'POST'])
def add_expense():
    if request.method == 'POST':
        name = request.form['name']
        amount = float(request.form['amount'])
        # Optional: deadline or target date
        date_added = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        expense = {
            'name': name,
            'amount': amount,
            'date_added': date_added,
            'reviewed': False
        }
        expenses.append(expense)
        return redirect(url_for('view_expenses'))
    return render_template('add_expense.html')

# View Expenses route
@app.route('/expenses')
def view_expenses():
    total_amount = sum(expense['amount'] for expense in expenses)
    return render_template('view_expenses.html', expenses=expenses, total_amount=total_amount)

# Optional: mark an expense as reviewed
@app.route('/review/<int:expense_id>')
def review_expense(expense_id):
    if 0 <= expense_id < len(expenses):
        expenses[expense_id]['reviewed'] = True
    return redirect(url_for('view_expenses'))


if __name__ == '__main__':
    app.run(debug=True, port=5001)