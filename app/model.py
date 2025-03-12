import pandas as pd
import streamlit as st
import io
import app.new_column_values as ncv
import typing as t
from datetime import datetime

# Upload the file
def upload_table() -> st.runtime.uploaded_file_manager.UploadedFile | None:
    """
    Allows the user to upload a file. Accepts various spreadsheet formats.
    
    Returns:
        UploadedFile | None: The uploaded file or None if no file is uploaded.
    """
     
    return st.file_uploader('Upload Table', type=['csv', 'xlsx', 'xls', 'xlsm', 'xlsb', 'odf', 'ods', 'odt'])

# Check if the file is a valid type
def file_type(file) -> bool:
    """
    Validates if the uploaded file has an accepted file extension.
    
    Args:
        file: The uploaded file object.
    
    Returns:
        bool: True if the file is of a valid type, False otherwise.
    """
    file.name.split('.')[-1]
    if file.name.split('.')[-1] in ['csv', 'xlsx', 'xls', 'xlsm', 'xlsb', 'odf', 'ods', 'odt']:
        return True
    return False

# Reads the file and transform it in a DataFrame
def file_to_csv(file) -> pd.DataFrame:
    """
    Reads an uploaded file and converts it into a Pandas DataFrame.
    
    Args:
        file: The uploaded file object.
    
    Returns:
        pd.DataFrame: The DataFrame containing the file's data.
    """
    if file is None:
        st.error("No file uploaded.")
        return None

    try:
        if file.name.endswith('.csv'):
            df = pd.read_csv(file, encoding='latin1', skip_blank_lines=True)
        elif file.name.endswith(('.xlsx', '.xls', '.xlsm', '.xlsb', '.odf', '.ods', '.odt')):
            df = pd.read_excel(file)
        else:
            st.error("Unsupported file format.")
            return None

        if df.empty:
            st.warning("The uploaded file is empty or does not contain readable data.")
            return None

        return df

    except pd.errors.EmptyDataError:
        st.error("The uploaded file is empty or contains no readable columns.")
        return None
    except pd.errors.ParserError:
        st.error("Error parsing the file. Please check the format.")
        return None
    except Exception as e:
        st.error(f"An unexpected error occurred: {e}")
        return None

# Allow the user to visualize and edit the table
def table_editor(df) -> pd.DataFrame:
    """
    Displays a data editor widget to allow users to view and edit the DataFrame.
    
    Args:
        df (pd.DataFrame): The DataFrame to be displayed and edited.
    
    Returns:
        pd.DataFrame: The modified DataFrame after user edits.
    """
    return st.data_editor(df, width=800, height=400, num_rows="dynamic")

def add_new_column(df):
    """
    Allows the user to add a new column to the DataFrame with a default value.
    
    The user specifies the column name and selects a default value type, which 
    is then assigned to the new column in the DataFrame.
    
    Args:
        df (pd.DataFrame): The DataFrame to which the new column will be added.
    
    Returns:
        pd.DataFrame: The DataFrame with the new column added.
    """
    column_name: str = st.text_input('Column Name')
    default_value: str = st.selectbox(
        'Default Value', 
        list(ncv.new_column_value['new_column_value'][0].keys()), 
        placeholder="Select the value type of the new column"
    )
    default_value: t.Union[int, float, str, bool, datetime.today, datetime.now] = ncv.new_column_value['new_column_value'][0][default_value]

    if st.button("Add Column"):
        if column_name:
            df[column_name] = default_value  
            st.success(f"Column '{column_name}' added successfully!")
        else:
            st.error("Please provide a column name.")
    return df
