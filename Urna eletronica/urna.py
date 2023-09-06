numero_do_candidato =[]
nome_do_candidato = []
perguntas = []
def main():
    
    while True:
        nome = input("Digite o nome do candidato:")
        if nome.lower() == 'encerrar':
            break
        numero = int(input("Digite o numero do candidato:"))
        partido = input("digite o partido:")
        perguntas.append(f"Candidatos: {nome}, Numero: {numero}, Partido: {partido}")
        numero_do_candidato.append(numero)
        nome_do_candidato.append(nome)
        
    print("\nLista dos candidatos: ")        
    for pergunta in perguntas:
        print(pergunta)
    return perguntas    
#if __name__ == "__main__":

   

def realizar_votos():
    main()
    
   
    num_votos = int(input("Quantos alunos irão votar? "))
    
    for i in range(num_votos):    
        voto = int(input(f"Aluno {i+1}, Escolha o número do candidato: "))
            
        if voto in numero_do_candidato:
            if voto in votos:
                votos[voto] += 1
            else:
                votos[voto] = 1   
            print("Voto concluido")    
       
        else:
            print("Número de candidato inválido")

def resultados():
    print("Resultado da votação")
    for candidato_num in numero_do_candidato:
        total_votos = votos.get(candidato_num, 0)
    for candidato_nome in nome_do_candidato:
        print(f"Nome: {candidato_nome}, Votos:{total_votos}")
        
votos = {}

realizar_votos()
resultados()