import streamlit as st
import pandas as pd
import app.model as model
import io

st.title('Ease Query')

table = st.file_uploader('Upload Table', type=['csv', 'xlsx', 'xls', 'xlsm', 'xlsb', 'odf', 'ods', 'odt'])

if table is not None:
    if model.file_type(table):
        # Converte o arquivo para um DataFrame
        df = model.file_to_csv(table)
        
        # Exibe o editor de dados para edição
        new_table = model.table_editor(df)

        # Converte o DataFrame editado de volta para CSV
        csv_data = new_table.to_csv(index=False)

        # Converte os dados CSV para bytes
        csv_bytes = io.BytesIO(csv_data.encode())

        # Solicita o nome do arquivo
        table_name = model.new_file_specs()

        # Adiciona o botão para download
        st.download_button(
            label="Download Table to csv",
            data=csv_bytes,
            file_name=f"{table_name}.csv",  # Usa o nome da tabela fornecido pelo usuário
            mime="text/csv",
            icon=":material/download:"
        )
