import streamlit as st
import app.model as model

st.title('Ease Query')

table = model.upload_table()

def main():
    if table is not None:
        if model.file_type(table):
            # Read the file, transform in csv and trasnform in a DataFrame
            df = model.file_to_csv(table)
            
            df = model.add_new_column(df)

            new_table = model.table_editor(df)

            encoded_table = model.csv_encode(new_table)

            table_name = model.new_file_specs()

            model.download_to_csv(encoded_table,table_name)

if __name__ == '__main__':
    main()