import pandas as pd
import streamlit as st
import io
import app.new_column_values as ncv
import typing as t
from datetime import datetime

# Upload the file
def upload_table() -> st.runtime.uploaded_file_manager.UploadedFile | None:
    return st.file_uploader('Upload Table', type=['csv', 'xlsx', 'xls', 'xlsm', 'xlsb', 'odf', 'ods', 'odt'])

# Transform DataFrame in a byte-like object to allow downloading the file 
def csv_encode(df) -> io.BytesIO: 
    towrite = io.BytesIO()
    df.to_excel(towrite)  
    towrite.seek(0) 
    return towrite

# Check if the file is a valid type
def file_type(file) -> bool:
    file.name.split('.')[-1]
    if file.name.split('.')[-1] in ['csv', 'xlsx', 'xls', 'xlsm', 'xlsb', 'odf', 'ods', 'odt']:
        return True
    return False

# Reads the file and transform it in a DataFrame
def file_to_csv(file) -> pd.DataFrame:
    if file.name.split('.')[-1] in ['csv']:
        return pd.read_csv(file)
    elif file.name.split('.')[-1] in ['xlsx', 'xls', 'xlsm', 'xlsb', 'odf', 'ods', 'odt']:
        return pd.read_excel(file)
    return None

def new_file_specs() -> str:
    table_name : str = st.text_input('Table Name')
    return table_name

def download_to_csv(file,table_name) -> None:
        st.download_button(
            label="Download Table to csv",
            data=file,
            file_name=f"{table_name}.csv", 
            mime="text/csv",
            icon=":material/download:"
        )

def table_editor(df) -> pd.DataFrame:
    return st.data_editor(df, width=800, height=400, num_rows="dynamic")

def add_new_column(df):
    """
    column_namme -> receives a string wtih the name of the new column
    default_value -> receives a value to be the default value of the new column
                     it can be a string, integer, float, boolean, date or time   
    """
    column_name : str = st.text_input('Column Name')
    default_value : t.Union[int, float, str, bool, datetime.today, datetime.now] = st.selectbox(
        'Default Value', 
        list(ncv.new_column_value['new_column_value'][0].keys()), 
        placeholder="Select the value type of the new column"
    )
    default_value = ncv.new_column_value['new_column_value'][0][default_value]

    if st.button("Add Column"):
        if column_name:
            df[column_name] = default_value  
            st.success(f"Column '{column_name}' added successfully!")
        else:
            st.error("Please provide a column name.")
    return df