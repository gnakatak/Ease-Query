import streamlit as st
import app.model as model

st.title('Ease Query')

table = model.upload_table()

def main():
    if table is not None:
        if model.file_type(table):
            # Read the file, transform in csv and trasnform in a DataFrame
            df = model.file_to_csv(table)
            # ADd new column to the DataFrame
            df = model.add_new_column(df)
            # Edit the table
            new_table = model.table_editor(df)
            # transform in csv and encode it 
            encoded_table = model.csv_encode(new_table)
            # New table name
            table_name = model.new_file_specs()
            # Download the table
            model.download_to_csv(encoded_table,table_name)

if __name__ == '__main__':
    main()