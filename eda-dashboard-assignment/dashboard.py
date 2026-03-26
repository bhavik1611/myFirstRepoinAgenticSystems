import streamlit as st
import plotly.express as px

# Import fetch_and_clean_posts from fetch_data.py
from fetch_data import fetch_and_clean_posts

st.set_page_config(page_title="Post Data Dashboard", layout="centered")

st.title("Simple Post Data Dashboard")

# Fetch and clean data
@st.cache_data
def load_data():
    return fetch_and_clean_posts()

df = load_data()

# --- Exploratory Analysis ---

# Count posts per user
posts_per_user = df.groupby("user_id").size().reset_index(name="post_count")

# Add post_length column
df["post_length"] = df["body"].astype(str).apply(len)

# --- Streamlit Dashboard ---

st.header("Dataset Preview")
st.dataframe(df.head())

# Visualization: Posts Per User
st.header("Number of Posts per User")
bar_chart = (
    posts_per_user
    .set_index("user_id")["post_count"]
)
st.bar_chart(bar_chart)

# Visualization: Distribution of Post Length
st.header("Post Length Distribution")
fig = px.histogram(df, x="post_length", nbins=20, title="Post Length Distribution")
st.plotly_chart(fig)

st.markdown("""
---
**Dashboard Features:**
- Data fetched from a public API and cleaned.
- Number of posts per user visualized as a bar chart.
- Distribution of post lengths shown as a histogram.
""")
