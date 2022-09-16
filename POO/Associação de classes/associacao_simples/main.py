from classes import Caneta, Escritor, MaquinaDeEscrever

escritor = Escritor("Jhonata")
caneta = Caneta("Bic")
maquina = MaquinaDeEscrever()

# Tipo de associação mais fraca, se escritor for apagado, quebra a associação.
escritor.ferramenta = caneta
escritor.ferramenta.escrever()
