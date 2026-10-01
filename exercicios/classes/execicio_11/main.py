from controle_remoto import ControleRemoto

if __name__ == '__main__':

    controle = ControleRemoto(12, 15)

    try:
        print(controle.canal_atual)
        controle.trocar_canal(10)

    except SystemError as e:
        print(f"[ERROR]: {e}")
    finally:
        controle.ligar_tv()
        controle.trocar_canal(10)
        print(controle.canal_atual)

    