#Agenda pickle RAONNY SANTOS
#O módulo pickle mantém o controle dos objetos que já serializou, para que referências posteriores ao mesmo objeto não sejam serializadas novamente. marshal não faz isso.
 


import pickle

class Evento:
    def __init__(self, titulo, data, hora_inicio, hora_fim):
        self.titulo = titulo
        self.data = data
        self.hora_inicio = hora_inicio
        self.hora_fim = hora_fim

    def __str__(self):
        return f"Título: {self.titulo}\nData: {self.data}\nHora de Início: {self.hora_inicio}\nHora de Término: {self.hora_fim}\n"


class Agenda:
    def __init__(self, nome_agenda):
        self.nome_agenda = nome_agenda
        self.arquivo_agenda = f"{nome_agenda}.dat"
        self.carregar_eventos()

    def carregar_eventos(self):
        try:
            with open(self.arquivo_agenda, "rb") as file:
                self.eventos = pickle.load(file)
        except FileNotFoundError:
            self.eventos = []

    def salvar_eventos(self):
        with open(self.arquivo_agenda, "wb") as file:
            pickle.dump(self.eventos, file)

    def adicionar_evento(self, evento):
        self.eventos.append(evento)
        self.salvar_eventos()

    def visualizar_eventos(self):
        if not self.eventos:
            print("Nenhum evento agendado.")
        else:
            for i, evento in enumerate(self.eventos, 1):
                print(f"Evento {i}:\n{evento}")

    def editar_evento(self):
        self.visualizar_eventos()
        if self.eventos:
            num_evento = int(input("Digite o número do evento que deseja editar: "))
            if 1 <= num_evento <= len(self.eventos):
                evento = self.eventos[num_evento - 1]
                titulo = input("Novo título do evento: ")
                data = input("Nova data do evento: ")
                hora_inicio = input("Nova hora de início do evento: ")
                hora_fim = input("Nova hora de término do evento: ")
                evento.titulo = titulo
                evento.data = data
                evento.hora_inicio = hora_inicio
                evento.hora_fim = hora_fim
                self.salvar_eventos()
                print("Evento editado com sucesso.")
            else:
                print("Número de evento inválido.")
        else:
            print("Não há eventos para editar.")

    def excluir_evento(self):
        self.visualizar_eventos()
        if self.eventos:
            num_evento = int(input("Digite o número do evento que deseja excluir: "))
            if 1 <= num_evento <= len(self.eventos):
                del self.eventos[num_evento - 1]
                self.salvar_eventos()
                print("Evento excluído com sucesso.")
            else:
                print("Número de evento inválido.")
        else:
            print("Não há eventos para excluir.")

    def menu_interativo(self):
        while True:
            print("\nMenu Principal:")
            print("1. Adicionar Evento")
            print("2. Visualizar Eventos")
            print("3. Editar Evento")
            print("4. Excluir Evento")
            print("5. Sair do Programa")
            escolha = input("Escolha uma opção: ")

            if escolha == '1':
                titulo = input("Título do evento: ")
                data = input("Data do evento: ")
                hora_inicio = input("Hora de início do evento: ")
                hora_fim = input("Hora de término do evento: ")
                novo_evento = Evento(titulo, data, hora_inicio, hora_fim)
                self.adicionar_evento(novo_evento)
            elif escolha == '2':
                self.visualizar_eventos()
            elif escolha == '3':
                self.editar_evento()
            elif escolha == '4':
                self.excluir_evento()
            elif escolha == '5':
                print("Encerrando o programa...")
                break
            else:
                print("Opção inválida. Por favor, escolha novamente.")


if __name__ == "__main__":
    nome_agenda = input("Digite o nome da agenda: ")
    minha_agenda = Agenda(nome_agenda)
    minha_agenda.menu_interativo()
