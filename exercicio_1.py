#v_couro é o valor do couro para fabricação unitária
v_couro=float(input("Digite o valor do COURO:"))

#v_solado é o valor do solado para fabricação unitaria
v_solado=float(input("Digite o valor do SOLADO:"))

#v_cordoes é o valor de cordoes e ilhoeses para fabricação unitária
v_cordoes=float(input("Digite o valor de CORDOES E ILHOESES:"))

#v_insumos é o valor de insumos para fabricação unitária
v_insumos=float(input("Digite o valor de insumos:"))

#v_MaoObra é o valor de mão de obra para fabricação unitária
v_MaoObra=float(input("Digite o valor de Mão de Obra:"))

#v_marketing é o valor de Marketing e propaganda dividido pela produção
v_marketing=float(input("Digite o valor de Marketing:"))

#v_vendas é o valor do custo de vendas dividido pela produção
v_vendas=float(input("Digite o valor dos custos de venda:"))


#CALCULO DO PREÇO DE CUSTO
Preco_custo=(v_couro*0.30)+(v_solado*0.20)+(v_cordoes*0.05)+(v_insumos*0.05)
+(v_MaoObra*0.20)+(v_marketing*0.10)+(v_vendas*0.10)
print('O preço de custo unitário deste modelo de sapato é:',Preco_custo)

#CALCULANDO O PREÇO FINAL
#CALCULO DO PREÇO ADICIONANDO O LUCRO DO FABRICANTE
Preco_lucro=Preco_custo*1.30

#CALCULO DO PREÇO ADICIONANDO PERDAS DE CAPITAL
Preco_perdas=Preco_lucro*1.15

#CALCULO DO PREÇO ADICIONANDO IMPOSTOS FEDERAIS
Preco_impostos=Preco_perdas*1.15

#CALCULO DO PREÇO ADICIONANDO MARGEM DE VENDAS
Preco_vendas=Preco_impostos*1.25

#CALCULO DO PREÇO ADICIONANDO IMPOSTOS ESTADUAIS E MUNICIPAIS
Preco_ICMS_INSS=Preco_vendas*1.30

#PREÇO FINAL, ACRESCIDO DE TODOS OS IMPOSTOS E MARGENS DE LUCRO
Preco_final=Preco_ICMS_INSS
print('O preço final ao consumidor deste modelo de sapato é:',Preco_final)
