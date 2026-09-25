# StudySpend – Student Budget & Study Expense Tracker

## Elevator Pitch
StudySpend helps students track their study-related expenses efficiently, visualize spending, and stay organized with deadlines for each expense.

## Inspiration
As a student, I realized that managing study expenses and keeping track of spending is often confusing. I wanted a simple tool to track expenses, see totals, and manage deadlines in one place.

## What it does
- Add expenses with a name, amount, and date added.
- Optionally, set deadlines for expenses.
- View all expenses in a clear, organized list showing name, amount, date & time, and reviewed status.
- Mark expenses as reviewed and track total spending.
- Navigate easily between adding and viewing expenses.

## How I built it
- **Backend:** Python Flask handles routing, form processing, and rendering dynamic templates.
- **Frontend:** HTML & CSS with Jinja2 templates display the expenses clearly.
- **Logic:** Each expense stores name, amount, date_added, and reviewed status for easy tracking.
- **Design:** Clean, responsive UI ensures expenses are readable on all devices.

## Challenges I ran into
- Handling the date and time for each expense.
- Keeping a simple, clutter-free UI while displaying all necessary info.
- Implementing the “reviewed” status correctly.

## Accomplishments that I'm proud of
- Successfully implemented expense addition and viewing.
- Enabled marking expenses as reviewed and displaying total spending.
- Built a fully functional student-focused expense tracker using Flask without a database.

## What I learned
- How to use Flask routing, Jinja templates, and forms for dynamic web pages.
- Managing dates, times, and status flags for data entries.
- Structuring a small project efficiently for easy expansion.

## What's next for StudySpend
- Add persistent storage using SQLite or MongoDB.
- Categorize expenses by type or priority.
- Highlight overdue or pending expenses.
- Improve UI with charts to visualize spending trends.

## Built With
- Python
- Flask
- HTML
- CSS

