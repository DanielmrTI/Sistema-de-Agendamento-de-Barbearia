class Agendamento:
    def __init__(self, nome, data, hora, servico):
        self.nome = nome
        self.data = data
        self.hora = hora
        self.servico = servico

    def __str__(self):
        return f"Nome: {self.nome}, Data: {self.data}, Hora: {self.hora}, Serviço: {self.servico}"

class Sistema:
    def __init__(self):
        self.agendamentos = []

    def agendar(self):
        nome = input("Digite o nome do cliente: ")
        data = input("Digite o dia que deseja agendar: ")
        hora = input("Digite o horário: ")
        servico = input("Digite qual serviço o cliente deseja: ")

        novo_agendamento = Agendamento(nome, data, hora, servico)
        self.agendamentos.append(novo_agendamento)
        print("Agendamento realizado!")

    def cancelar(self):

        nome = input("Digite o nome do cliente para cancelar o agendamento: ")
        for i in self.agendamentos:
            if i.nome == nome:
                self.agendamentos.remove(i)
                print("Agendamento cancelado!")
                return
        print("Agendamento não encontrado!")

    def visualizar_agendamento(self): 
        if not self.agendamentos:
            print("Nenhum agendamento encontrado.")
        else:
            for i in self.agendamentos:
                print(i)    
        
sistema = Sistema()

while True:
    print("1 - Agendar Visita")
    print("2 - Cancelar Visita ") 
    print("3 - Visualizar Agendamentos")
    print("4 - Sair")

    op = input("Escolha uma opção: ") 

    if op == "1":
        sistema.agendar()

    elif op == "2":
        sistema.cancelar()

    elif op == "3":
        sistema.visualizar_agendamento()  

    elif op == "4":
        print("Saindo do sistema...")    
        break

    else:
        print("Opção inválida")






        

  































