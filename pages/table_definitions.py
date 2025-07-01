import streamlit as st
from data_connectors.file_connector import FileConnector
import pandas as pd

st.set_page_config(
    page_title="Table Definitions",
    page_icon="📚"
)

st.title("Table Definitions")

# Check if a file has been uploaded in the main app
if 'uploaded_file_path' in st.session_state and st.session_state['uploaded_file_path']:
    file_path = st.session_state['uploaded_file_path']
    st.write(f"Displaying schema for: {file_path}")

    try:
        connector = FileConnector(file_path)
        if connector.connect():
            schema = connector.get_schema()
            
            if schema:
                # Group schema by table (sheet name for Excel, file name for CSV)
                tables = {}
                for col_info in schema:
                    table_name = col_info['table']
                    if table_name not in tables:
                        tables[table_name] = []
                    tables[table_name].append(col_info)
                
                tab_titles = list(tables.keys())
                tbl_tabs = st.tabs(tab_titles)
                
                for i, table_name in enumerate(tab_titles):
                    with tbl_tabs[i]:
                        st.subheader(f"Table: {table_name}")
                        table_schema_str = f"{table_name} (\n"
                        for col_info in tables[table_name]:
                            table_schema_str += f"\t{col_info['column']} {col_info['type']},\n"
                        table_schema_str = table_schema_str.rstrip(',\n') + "\n)"
                        st.code(table_schema_str, language="sql")
            else:
                st.info("No schema information available for the uploaded file.")
        else:
            st.error(f"Could not connect to file: {file_path}. Please ensure it's a valid CSV or Excel file.")
    except Exception as e:
        st.error(f"An error occurred while processing the file: {e}")
else:
    st.info("No spreadsheet file uploaded. Please upload a file on the 'Home' page to view its schema.")