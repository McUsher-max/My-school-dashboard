import pandas as pd
import plotly.express as px
import streamlit as st

# ----- Mock Data Setup -----
students = pd.DataFrame({
    "student_id": [1, 2, 3, 4],
    "name": ["Ali", "Sana", "Youssef", "Mariam"],
    "class": ["3A", "3A", "3B", "3B"],
    "gender": ["M", "F", "M", "F"],
})

attendance = pd.DataFrame({
    "student_id": [1, 1, 2, 2, 3, 3, 4, 4],
    "date": pd.date_range(start="2024-04-01", periods=8),
    "status": ["Present", "Absent", "Present", "Present", "Late", "Present", "Absent", "Present"]
})

fees = pd.DataFrame({
    "student_id": [1, 2, 3, 4],
    "total_due": [500, 500, 500, 500],
    "total_paid": [500, 250, 500, 0],
})

grades = pd.DataFrame({
    "student_id": [1, 1, 2, 2, 3, 3, 4, 4],
    "subject": ["Math", "Arabic"] * 4,
    "grade": [85, 90, 70, 75, 95, 92, 60, 65],
})

# ----- Streamlit Dashboard -----
st.title("📊 Private School Dashboard")

# Enrollment Stats
st.header("📚 Enrollment Overview")
class_counts = students["class"].value_counts().reset_index()
class_counts.columns = ["Class", "Number of Students"]
st.write(class_counts)

# Attendance
st.header("🕒 Attendance Summary")
attendance_summary = attendance.groupby("status").size().reset_index(name="Count")
fig_attendance = px.pie(attendance_summary, names="status", values="Count", title="Attendance Breakdown")
st.plotly_chart(fig_attendance)
