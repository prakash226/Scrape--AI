import streamlit as st
from web_scraper import scrape_site
from web_scraper import clean_body_content
from web_scraper import extract_body_content
from web_scraper import split_dom_content
from parse import parse_with_ollama



st.title("SHALL WE SCRAPE ?")
url = st.text_input('Enter Website URL:')

if st.button("LET'S SCRAPE"):
    st.write("Scraping the website")
    result = scrape_site(url)
    body_content = extract_body_content(result)
    cleaned_content = clean_body_content(body_content)

    st.session_state.dom_content = cleaned_content


    with st.expander('Page Content'):
        st.text_area('DOM Content', cleaned_content, height=300)


if "dom_content" in st.session_state:
    parse_description = st.text_area("Describe what you want to parse")

    if st.button("Parse Content"):
        if parse_description:
            st.write("Parsing the content...")

            # Parse the content with Ollama
            dom_chunks = split_dom_content(st.session_state.dom_content)
            parsed_result = parse_with_ollama(dom_chunks, parse_description)
            st.write(parsed_result)


