import pandas as pd
import streamlit as st
import io

def file_type(file):
    file.name.split('.')[-1]
    if file.name.split('.')[-1] in ['csv', 'xlsx', 'xls', 'xlsm', 'xlsb', 'odf', 'ods', 'odt']:
        return True
    return False

def file_to_csv(file):
    if file.name.split('.')[-1] in ['csv']:
        return pd.read_csv(file)
    elif file.name.split('.')[-1] in ['xlsx', 'xls', 'xlsm', 'xlsb', 'odf', 'ods', 'odt']:
        return pd.read_excel(file)
    return None

def new_file_specs():
    table_name = st.text_input('Table Name')
    return table_name

def download_to_csv(file,table_name):

        st.download_button(
            label="Download Table to csv",
            data=file,
            file_name=f"{table_name}.csv",  # Usa o nome da tabela fornecido pelo usuário
            mime="text/csv",
            icon=":material/download:"
        )

def add_new_column(df):
    column_name = st.text_input('Column Name')
    column_data = st.text_input('Column Data')
    df[column_name] = column_data
    return df

def table_editor(df):
    return st.data_editor(df, width=800, height=400, num_rows="dynamic")