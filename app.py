
pip install openpyxl

# At the top of your app.py
import streamlit as st
import pandas as pd
import plotly.express as px

# --- Load data from Excel or CSV ---
@st.cache_data
def load_data():
    students = pd.read_excel('students.xlsx')
    finance_summary = pd.read_excel('finance_summary.xlsx')
    subjects = pd.read_excel('subjects.xlsx')
    attendance_summary = pd.read_excel('attendance_summary.xlsx')
    return students, finance_summary, subjects, attendance_summary

students, finance_summary, subjects, attendance_summary = load_data()


# --- Sidebar Navigation ---
st.sidebar.title("🏫 Private School Dashboard")
page = st.sidebar.radio("Navigate", ["Home", "Students", "Finance", "Academic", "Alerts"])

# --- Page: Home ---
if page == "Home":
    st.title("🏫 Private School Dashboard - Home")
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("📚 Total Students", f"{len(students)}")
    with col2:
        st.metric("🕒 Attendance Rate", "94%")
    with col3:
        st.metric("💰 Fees Collected", "85%")
    with col4:
        st.metric("🎓 Avg. Grade", f"{students['average_grade'].mean():.2f}%")
    
    st.subheader("📈 Enrollment Trend (Placeholder)")
    st.line_chart([320, 330, 340, 345, 350])

# --- Page: Students ---
elif page == "Students":
    st.title("👨‍🎓 Students Overview")
    
    st.subheader("🕒 Absenteeism Report")
    st.dataframe(
        students[['name', 'class', 'absences']].style.set_properties(**{
            'text-align': 'left',
            'border-color': '#D5DBDB',
        })
    )

# --- Page: Finance ---
elif page == "Finance":
    st.title("💰 Finance Overview")
    
    st.subheader("💳 Fee Collection by Class")
    finance_summary['collection_rate'] = finance_summary['total_paid'] / finance_summary['total_due'] * 100
    st.dataframe(
        finance_summary.style.set_properties(**{
            'text-align': 'left',
            'border-color': '#D5DBDB',
        })
    )
    
    st.subheader("📊 Fee Collection Bar Chart")
    fig_finance = px.bar(finance_summary, x='class', y=['total_due', 'total_paid'], 
                         barmode='group', title="💸 Fee Payment Status")
    fig_finance.update_layout(template='plotly_white')
    st.plotly_chart(fig_finance)

# --- Page: Academic ---
elif page == "Academic":
    st.title("🎓 Academic Performance")
    
    st.subheader("📚 Average Grade by Subject")
    fig_subjects = px.bar(subjects, x='subject', y='average_grade', 
                          title="📖 Subject Performance")
    fig_subjects.update_layout(template='plotly_white')
    st.plotly_chart(fig_subjects)
    
    st.subheader("🏆 Top Students")
    top_students = students.sort_values(by='average_grade', ascending=False)
    st.dataframe(
        top_students[['name', 'class', 'average_grade']].style.set_properties(**{
            'text-align': 'left',
            'border-color': '#D5DBDB',
        })
    )

# --- Page: Alerts ---
elif page == "Alerts":
    st.title("🚨 Alerts Center")
    
    st.subheader("🛑 Absentee Alerts")
    absentee_alerts = students[students['absences'] > 3]
    st.dataframe(
        absentee_alerts[['name', 'class', 'absences']].style.set_properties(**{
            'text-align': 'left',
            'border-color': '#D5DBDB',
        })
    )
    
    st.subheader("⚠️ Unpaid Fees Alerts")
    unpaid_alerts = students[students['fees_due'] > 0]
    st.dataframe(
        unpaid_alerts[['name', 'class', 'fees_due']].style.set_properties(**{
            'text-align': 'left',
            'border-color': '#D5DBDB',
        })
    )

    st.subheader("📊 Attendance Overview")
    fig_attendance = px.pie(attendance_summary, names="status", values="Count", title="🕒 Attendance Breakdown")
    fig_attendance.update_traces(textposition='inside', textinfo='percent+label')
    fig_attendance.update_layout(template='plotly_white')
    st.plotly_chart(fig_attendance)
