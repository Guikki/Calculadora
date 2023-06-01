import globais     

def c():
    # global globais.acumulador
    # global globais.memoria
    # global globais.backup
    print(globais.acumulador, globais.backup, globais.memoria)
    globais.backup = 0
    globais.acumulador = 0  

def ce():
    # global globais.acumulador
    # global globais.memoria
    # global globais.backup
    globais.acumulador = globais.backup

def ms():
    # global globais.acumulador
    # global globais.memoria
    # global globais.backup
    globais.memoria = globais.acumulador

def mr():
    # global globais.acumulador
    # global globais.memoria
    # global globais.backup
    globais.acumulador = globais.memoria

def mc():
    # global globais.acumulador
    # global globais.memoria
    # global globais.backup
    globais.memoria = 0

def mmais():
    # global globais.acumulador
    # global globais.memoria
    # global globais.backup
    globais.memoria = globais.acumulador + globais.memoria

def mmenos():
    # global globais.acumulador
    # global globais.memoria
    # global globais.backup
    globais.memoria = globais.memoria - globais.acumulador

def calculomemoria():
    # global globais.acumulador
    # global globais.memoria
    # global globais.backup
    globais.acumulador = globais.acumulador + globais.memoria
