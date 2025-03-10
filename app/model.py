import pandas as pd
import streamlit as st
import io
import app.new_column_values as ncv

def upload_table() -> st.runtime.uploaded_file_manager.UploadedFile | None:
    return st.file_uploader('Upload Table', type=['csv', 'xlsx', 'xls', 'xlsm', 'xlsb', 'odf', 'ods', 'odt'])

def csv_encode(df) -> io.BytesIO:
    csv_data = df.to_csv(index=False)
    return io.BytesIO(csv_data.encode())
    

def file_type(file) -> bool:
    file.name.split('.')[-1]
    if file.name.split('.')[-1] in ['csv', 'xlsx', 'xls', 'xlsm', 'xlsb', 'odf', 'ods', 'odt']:
        return True
    return False

def file_to_csv(file) -> pd.DataFrame:
    if file.name.split('.')[-1] in ['csv']:
        return pd.read_csv(file)
    elif file.name.split('.')[-1] in ['xlsx', 'xls', 'xlsm', 'xlsb', 'odf', 'ods', 'odt']:
        return pd.read_excel(file)
    return None

def new_file_specs() -> str:
    table_name = st.text_input('Table Name')
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
    column_name = st.text_input('Column Name')
    default_value = st.selectbox(
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