def Calculo_juros(valor=0,dia=0,mes=0,ano=0):
    from datetime import datetime

    #Recebe datas
    calendario = datetime.now()
    data = calendario.date()
    data_vencimento = datetime(ano,mes,dia).date()
    data_difernca = (data - data_vencimento)
    dias= data_difernca.days
#calcuando valor total
    valor = valor
    multa = (valor * 0.025) * dias
    total_pagar = valor + multa

    if dias < 0:
         print(f'VALIDA - vence no dia {data_vencimento} : Total a pagar {valor}')
    elif dias == 0 :
         print(f"VENCE HOJE : valor a pagar {valor}")
    else:
         print(f'VENCEU A {dias} dias : Total a pagar {total_pagar}')



Calculo_juros(100,2,12,2025)