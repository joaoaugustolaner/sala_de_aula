class Relogio:

    hora: int
    minuto: int

    def __init__(self, hora:int, minuto:int):
        self.hora = hora
        self.minuto = minuto

    def _passar_hora(self):
        self.hora += 1

        if self.hora == 24:
            self.hora = 0

    def passar_minuto(self):
        if self.minuto < 60:
            self.minuto += 1
        else:
            self.minuto = 0
            self._passar_hora()
    

    def mostrar_horario(self):
        print(f"São {self.hora}h{self.minuto}")

relogio = Relogio(hora=20, minuto=57)
relogio.passar_minuto()
relogio.passar_minuto()
relogio.passar_minuto()
relogio.mostrar_horario()


