import streamlit as st
import app.model as model
import pandas as pd
import io

st.title('Ease Query')

# Inicializa a variável df como None
df = None

# Tente carregar a tabela do session_state, se já existir
if 'table' not in st.session_state:
    table = model.upload_table()
    if table is not None:
        if model.file_type(table):
            # Lê o arquivo e transforma em DataFrame
            df = model.file_to_csv(table)
            # Armazena o DataFrame no session_state
            st.session_state.table = df
else:
    df = st.session_state.table

def main():
    global df
    if df is not None:
        # Adiciona nova coluna ao DataFrame
        df = model.add_new_column(df)
        # Edita a tabela
        df = model.table_editor(df)
        # Atualiza o session_state com a nova versão do DataFrame
        st.session_state.table = df

if __name__ == '__main__':
    main()
