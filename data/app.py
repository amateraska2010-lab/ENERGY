import streamlit as st
from backend.logic import get_match_report
from data.vacancies import VACANCIES

st.set_page_config(page_title="SkillBridge AI", layout="wide")

st.title("🚀 SkillBridge AI: Карьерный помощник")
st.subheader("Соединяем студентов колледжей и работодателей")

# Разделение экрана на две части
col1, col2 = st.columns(2)

with col1:
    st.header("Для студента")
    student_resume = st.text_area("Вставь свое резюме или список навыков:", height=200)
    
    if st.button("Найти подходящие вакансии"):
        if student_resume:
            st.success("Анализируем...")
            for job in VACANCIES:
                report = get_match_report(student_resume, job['description'])
                with st.expander(f"{job['title']} в {job['company']} — Совпадение: {report['match_percent']}%"):
                    st.write(f"**Описание:** {job['description']}")
                    st.write(f"**Недостающие навыки:** {', '.join(report['missing_skills'])}")
                    st.write("**Рекомендации:**")
                    for rec in report['recommendations']:
                        st.write(f"✅ {rec}")
        else:
            st.error("Сначала введи навыки!")

with col2:
    st.header("Для работодателя")
    new_job = st.text_area("Опубликовать новую вакансию:", placeholder="Требования, стек технологий...")
    if st.button("Разместить"):
        st.info("Функция будет доступна в полной версии")

st.sidebar.info("Разработано командой energo_life для BilimHack Almaty")
