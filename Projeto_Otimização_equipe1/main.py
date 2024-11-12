import streamlit as st

#________________________Funções__________________________
#Monta uma função como string
def montaFuncao(coeficiente):
    for i in range(numVariaveis):
        funcao = " "
        for i in range(numVariaveis):
            if coeficiente[i] >= 0:
                funcao = funcao + " + " + str(round(coeficiente[i], 2)) + 'x' + str(i + 1) + "  "
            else:
                funcao = funcao + str(round(coeficiente[i], 2)) + 'x' + str(i + 1) + "  "
    return funcao

#Realiza a entrada de dados para a função objetiva
def FuncaoObj(numVariaveis):
    if numVariaveis > 0:
        st.title("Função Objetiva")
        st.write("\nInsira abaixo os coeficientes da função objetiva: ")

        # Vetor para armazenamento dos coeficiente da função obj
        coefFuncaoObj = []

        # Entrada dos coeficientes da função
        for i in range(numVariaveis):
            coef = st.number_input(f"Coeficiente de x{i + 1}: ")
            coefFuncaoObj.append(coef)

        return coefFuncaoObj


#Realiza a entrada de dados das restrições
def Restricoes(numRestricoes, numVariaveis):
    if numVariaveis > 0:
        if numRestricoes > 0:
            st.title("Restrições ")
            st.write("\nInsira abaixo as restrições do modelo: ")

            #Vetor com os coeficientes de todas as restrições
            coefRestricoes = []

            #Entrada dos coeficientes das restrições
            for i in range(numRestricoes):
                st.markdown(f'<h3 style="color:black; font-size:20px;">{i+1}° Restrição</h3>', unsafe_allow_html=True)

                linha = []  #armazena os coeficientes de uma unica restrição

                for j in range(numVariaveis):
                    coefRestricao = st.number_input(f"Coeficiente de x{j+1}:",  key=f"coef_{i}_{j}")
                    linha.append(coefRestricao)

                coefRestricoes.append(linha)
                coefDelta = st.number_input("Coeficiente delta: ", key=f"coef_{i}")

                st.write(f"**Restrição {i + 1}:**")
                funcaoRestricao = montaFuncao(linha) + "  ≤  " + str(coefDelta)
                st.markdown(f'<h3 style="border: 1px grey; padding: 10px; border-radius: 5px; background-color: #f0f0f0;text-align:center; color:#1E3A8A; font-size:30px;">{funcaoRestricao}</h3>',unsafe_allow_html=True)

            return coefRestricoes


#__________________________Main_____________________________
# Título do aplicativo
st.title("Simplex Tableau")

# Texto
st.write("Insira os dados abaixo para resolução do PPL: ")

#Entrada de dados
numVariaveis = st.number_input("N° Variàveis:", min_value=2, max_value=4, step=1, value=2)
numRestricoes = st.number_input("\nN° de restrições: ", min_value=0, max_value=10, step=1, value=0)

st.write("_______________________________________________________________________________")

#Funcao Objetiva
coefFuncaoObj = FuncaoObj(numVariaveis)
#Mostrando a função objetiva
funcaoObj = "Z = " + montaFuncao(coefFuncaoObj)
st.write("**Função Objetiva:**")
st.markdown(f'<h3 style="border: 1px grey; padding: 10px; border-radius: 5px; background-color: #f0f0f0;text-align:center; color:#1E3A8A; font-size:30px;">{funcaoObj}</h3>',unsafe_allow_html=True)

st.write("_______________________________________________________________________________")

#Restrições
#Solicitando os coeficientes das restrições por meio da função Restricoes
coefRestricao = []
coefRestricao.append(Restricoes(numRestricoes, numVariaveis))


#______________________________Resolução do PPL________________________
#...















