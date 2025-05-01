import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

conn = st.connection("snowflake")
df = conn.query("SELECT * FROM application_c limit 10;", ttl="10m")
for row in df.itertuples():
    st.write(f"{row.ID}")
