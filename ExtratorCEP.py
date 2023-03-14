endereco = "Avenida João Machado Soares, Apartamento 420, Santa Maria, Rio Grande do Sul, 97110-000"

import re

padrao = re.compile("[0-9]{5}[-]{0,1}[0-9]{3}")
busca = padrao.search(endereco)
if busca:
    cep = busca.group()
    print(cep)

