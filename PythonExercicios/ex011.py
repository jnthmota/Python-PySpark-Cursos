# *** 011 FAÇA UM PROGRAMA QUE LEIA A LARGURA E A ALTURA DE UMA PAREDE EM METROS, CALCULE A SUA ÁREA E A
# QUANTIDADE DE TINTA NECESSARIA PARA PINTA-LA, SABENDO QUE A CADA LITRO DE TINTA, PINTA UMA ÁREA DE 2M2*

l = float(input('Digite a largura da sua parede: '))
a = float(input('Digite a altura da sua parede: '))
area = l * a
t = area / 2
print('Largura da parede {}x{} e sua área é de {}m² \n Para pinta-la você vai precisar de {}l de tinta'.format(l, a, area, t))