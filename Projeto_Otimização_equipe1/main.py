import streamlit as st
from scipy.optimize import linprog

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

#Realiza a entrada de dados para a função objetiva por meio da interface
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

#Realiza a entrada de dados das restrições por meio da interface
def Restricoes(numRestricoes, numVariaveis):
    if numVariaveis > 0:
        if numRestricoes > 0:
            st.title("Restrições ")
            st.write("\nInsira abaixo as restrições do modelo: ")

            #Vetor com os coeficientes de todas as restrições
            coefRestricoes = []
            coefLimites = []

            #Entrada dos coeficientes das restrições
            for i in range(numRestricoes):

                st.markdown(f'<h3 style="color:black; font-size:20px;">{i+1}° Restrição</h3>', unsafe_allow_html=True)

                linha = []  #armazena os coeficientes de uma unica restrição

                for j in range(numVariaveis):
                    coefRestri = st.number_input(f"Coeficiente de x{j+1}:",  key=f"coef_{i}_{j}")
                    linha.append(coefRestri)

                coefRestricoes.append(linha)

                coefLim = st.number_input("Coeficiente limite da restrição: ", key=f"coef_{i}")
                coefLimites.append(coefLim)

                st.write(f"**Restrição {i + 1}:**")
                funcaoRestricao = montaFuncao(linha) + "  ≤  " + str(coefLim)
                st.markdown(f'<h3 style="border: 1px grey; padding: 10px; border-radius: 5px; background-color: #f0f0f0;text-align:center; color:#1E3A8A; font-size:30px;">{funcaoRestricao}</h3>',unsafe_allow_html=True)

            return coefRestricoes, coefLimites


#__________________________Main_____________________________
# Título do aplicativo
st.title("Simplex Tableau")
st.write("Insira os dados abaixo para resolução do PPL: ")

#Entrada de dados via interface
numVariaveis = st.number_input("N° Variàveis:", min_value=2, max_value=4, step=1, value=2)
numRestricoes = st.number_input("\nN° de restrições: ", min_value=1, max_value=10, step=1, value=1)

st.write("_______________________________________________________________________________")

#Solicitando os coeficientes da função objetiva
coefFuncaoObj = FuncaoObj(numVariaveis)

#mostrando a função objetiva
funcaoObj = "Z = " + montaFuncao(coefFuncaoObj)
st.write("**Função Objetiva:**")
st.markdown(f'<h3 style="border: 1px grey; padding: 10px; border-radius: 5px; background-color: #f0f0f0;text-align:center; color:#1E3A8A; font-size:30px;">{funcaoObj}</h3>',unsafe_allow_html=True)

st.write("_______________________________________________________________________________")

#Solicitando os coeficientes por meio da função Restricoes
coefRestricoes, coefLimites = Restricoes(numRestricoes, numVariaveis)


#______________________________Resolução do PPL________________________
st.write("Coeficientes da função Objetivo: ", coefFuncaoObj)
st.write("Coeficiente limites: ", coefLimites)
st.write("coeficientes das Restrições: ", coefRestricoes)

if st.button("Calcular Solução"):

    x_bounds = [(0, None)] * numVariaveis

    # calculando o PPL pelo método Simplex
    resultado = linprog([-c for c in coefFuncaoObj], A_ub=coefRestricoes, b_ub=coefLimites, bounds=x_bounds, method='simplex')

    # Exibir resultados
    if resultado.success:
        st.title("Solução ótima: ")
        st.write(f"Ponto Otimo de Operação:")
        for i in range(numVariaveis):
            st.write(f"x{i + 1} = {round(resultado.x[i], 2)}")
        st.write(f"Valor ótimo de Z = {round((resultado.fun *-1), 2)}")  # Negativo para reverter a maximização

        # Exibindo os preços sombra (dual) das restrições
        st.subheader("Preços Sombra das restrições:")
        for i in range(numRestricoes):
            st.write(f"Restrição {i + 1}: Preço Sombra = {round(resultado.resultine.dual[i], 2)}")

    else:
        st.write("Erro:", resultado.message)


