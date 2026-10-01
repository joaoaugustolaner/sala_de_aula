class ControleRemoto:

    tv_ligada:bool
    canal_atual: int
    volume: int

    def __init__(self, canal_atual:int, volume:int):
        self.canal_atual = canal_atual
        self.volume = volume
        self.tv_ligada = False
    
    def trocar_canal(self, numero_canal: int):
        if not self.tv_ligada:
            raise SystemError("É necessário ligar a tv para trocar de canal")
        
        self.canal_atual = numero_canal
    
    def ligar_tv(self):
        self.tv_ligada = True