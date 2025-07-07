##streamlit 
# pip install streamlit
##python lib 
##webpages for ml and data sci projects
#html and css no requirement
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import altair as alt 
import time

##page configuration 
st.set_page_config(
    page_title="streamlit function demo",
    page_icon= "😎",
    layout="centered"
)
##title and text elemnts 
st.title("hello world")
st.header("1. Text elements")
st.subheader("markdown,code,latex")
st.markdown("**bold text**,*italic text*,`code`text")
st.code("print('hello everyone')",language="python")
st.latex(r"a^2+b^2=c^2")

st.divider()

##metrices and messages 
st.header("2. metrices and messages")
st.metric(label="Revenue",value=1234,delta="+10%",delta_color="normal")
st.error("this is an error message")
st.warning("this is a warning message")
st.info("this is an info message")
st.success("this is a success message")
st.exception(ValueError("this is an exception message"))

st.divider()

##data display 
st.header("3. data display")
df=pd.DataFrame(np.random.randn(10,2),columns=["a","b"])
st.dataframe(df)
st.table(df.head(3))
st.json(df.to_dict())
st.divider()

#charts 
st.header("4.Charts")
st.line_chart(df)
st.bar_chart(df)
st.area_chart(df)
chart = alt.Chart(df.reset_index()).mark_line().encode(x="index",y="a")
st.altair_chart(chart,use_container_width=True)
fig , ax = plt.subplots()
ax.plot(df.index,df.a)
st.pyplot(fig)
st.divider()

#widgets
st.header("5. widgets")
with st.form("Input form"):
    name = st.text_input("NAME",type='password')
    age = st.number_input("AGE")
    mood = st.radio("select your mood",("happy","sad","neutral"))
    languages = st.multiselect("select your languages",("english","French","Hindi","Marathi"))
    submit = st.form_submit_button("SUBMIT")
    if submit:
        st.success(f"Name: {name}, Age : {int(age)}, Mood: {mood}, languages:{languages}")

col1,col2,col3=st.columns(3) #form ki positioning aet krne k liye usey column me divide kr dia
with col1:
    st.text("NAME")
    age = st.number_input("AGE")
with col2:
    mood = st.radio("select your mood",("happy","sad","neutral"))
    languages = st.multiselect("select your languages",("english","French","Hindi","Marathi"))
with col3:
        st.text("output")

col1,col2=st.columns(2)
with col1:
    number=st.slider("Select a number",0,100)
with col2:
    color=st.color_picker("Select a color",'#DC8080')

st.text_area("Enter your message")
st.date_input("Select a date")
st.time_input("select a time")
st.file_uploader("Upload a file")

#media element
st.header("6. MEDIA")
st.image(r"C:\Users\Gargi\OneDrive\Pictures\IMG_20210705_190831.jpg")
st.video(r"E:\SERIES\F.R.I.E.N.D.S\Season 6\Friends_S06_E13_720P_The_One_with_Rachel's_Sister_With_Subtitles.mkv")
st.audio(r"F:\PYTHON PROGRAM\Projects\Playlist\Songs\128-Laal Peeli Akhiyaan - Teri Baaton Mein Aisa Uljha Jiya 128 Kbps.mp3")

st.sidebar.header("hola amigo")
st.sidebar.write("kaise ho theek ho!")
st.sidebar.button("theek h?")
option=st.sidebar.selectbox("select an option",("option1","option2","option3"))
#tab padhna h 
# tab1,tab2
with st.container():
    st.write("this is a container")
    #submit = st.form_submit_button("SUBMIT")
    #koi bhi error ek particular container me aayegi

with st.expander("expander header"):
     st.write("This is an expander")

with st.spinner("loading data..."):
     time.sleep(3)
st.success("data loaded")
st.toast("wanna earn some money!",icon="😎")

st.page_link('https://www.netflix.com/in/login?nextpage=https%3A%2F%2Fwww.netflix.com%2Fbrowse',label='netflix and chill',icon='💕')