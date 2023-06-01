import funcoes 
import globais

def soma(valor):
    # global globais.acumulador
    # global globais.memoria
    # global globais.backup
    globais.backup = globais.acumulador
    globais.acumulador = globais.acumulador + valor
def subitracao(valor):
    # global globais.acumulador
    # global globais.memoria
    # global globais.backup
    globais.backup = globais.acumulador
    globais.acumulador = globais.acumulador - valor    
def multiplicacao(valor):
    # global globais.acumulador
    # global globais.memoria
    # global globais.backup
    globais.backup = globais.acumulador
    globais.acumulador = globais.acumulador * valor   
def divisao(valor):
    # global globais.acumulador
    # global globais.memoria
    # global globais.backup
    globais.backup = globais.acumulador
    globais.acumulador = globais.acumulador / valor        
def memoriamr():
    valor = input("Digite um número: ")
    if valor != 'mr':
        valor = float(valor)
    elif valor == 'mr':
        valor = globais.memoria
    return valor

def main():

    # global globais.acumulador
    # global globais.memoria
    # global globais.backup
 
    print(f'Estado Inicial: Acumulador: {globais.acumulador}; Backup: {globais.backup}; Memória: {globais.memoria}')

    while True:
        
        operacao = (input('Digite a operação desejada: ')).lower()
       
        if operacao == '=':
            globais.backup = globais.acumulador
            break
        elif operacao == '+':
            valor = memoriamr()
            soma(valor)
        elif operacao == '-':
            valor = memoriamr()
            subitracao(valor)    
        elif operacao == '*':
            valor = memoriamr()
            multiplicacao(valor)        
        elif operacao == '/':
            valor = memoriamr()
            divisao(valor)
        elif operacao == 'ce':
            funcoes.ce()
        elif operacao =='c':
             funcoes.c()
        elif operacao == 'ms':
             funcoes.ms()
        elif operacao == 'mr':
             funcoes.mr()
        elif operacao == 'mc':
             funcoes.mc()
        elif operacao == 'm+':
             funcoes.mmais()
        elif operacao == 'm-':
             funcoes.mmenos()
        elif operacao == '+/-':
            globais.acumulador = globais.acumulador - globais.acumulador*2
        elif operacao == '1/x':
            globais.acumulador = 1 / globais.acumulador
        elif operacao == 'x^2':
            globais.acumulador **= 2
        elif operacao == 'r2x':
            globais.acumulador **= 0.5
        # elif  operacao == int:
        #      valor = float(input("Digite um número: "))   
        #      divisao(valor)
        elif operacao != str:
            globais.acumulador = float(operacao)     
        else:
            raise NotImplementedError("Outras operações não implementadas")

        print(f'Acumulador: {globais.acumulador}; Backup: {globais.backup}; Memória: {globais.memoria}')

    print(f'Resultado Final: Acumulador: {globais.acumulador}; Backup: {globais.backup}; Memória: {globais.memoria}')

if __name__=='__main__':
    main()
