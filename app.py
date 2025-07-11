import streamlit as st
import json

# Load data dari file books.json
with open("scrapy_project/books.json", "r") as f:
    books = json.load(f)

st.title("📚 Book Search App")
st.write("Data hasil scraping dari [Books to Scrape](https://books.toscrape.com/)")

search = st.text_input("Cari judul buku...")

# Filter buku berdasarkan pencarian
filtered_books = [book for book in books if search.lower() in book['title'].lower()]

for book in filtered_books:
    st.subheader(book['title'])
    st.write(f"💲 Harga: {book['price']}")
    st.write(f"📦 Stok: {book['availability']}")
    st.write(f"⭐ Rating: {book['rating']}")
    st.markdown("---")
