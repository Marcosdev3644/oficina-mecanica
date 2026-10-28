from veiculo import Veiculo
from servico import TrocaOleo, Alinhamento
from ordem_servico import OrdemServico

veiculos = []
ordens = []

def cadastrar_veiculo():
    print("\n--- CADASTRO DE VEÍCULO ---")
    try:
        placa = input("Placa: ")
        modelo = input("Modelo: ")
        ano = int(input("Ano: "))
        v = Veiculo(placa, modelo, ano)
        veiculos.append(v)
        print("Veículo cadastrado com sucesso!")
    except ValueError as e:
        print(f"Erro: {e}")

def lancar_servico():
    print("\n--- LANÇAR SERVIÇO ---")
    if not veiculos:
        print("Nenhum veículo cadastrado. Cadastre um veículo primeiro.")
        return
    
    print("Veículos disponíveis:")
    for i, v in enumerate(veiculos):
        print(f"{i + 1} - {v.modelo} ({v.ano}) - Placa: {v.placa}")
    
    try:
        idx_veiculo = int(input("Escolha o número do veículo: ")) - 1
        if idx_veiculo < 0 or idx_veiculo >= len(veiculos):
            print("Veículo inválido.")
            return
        
        veiculo_escolhido = veiculos[idx_veiculo]
        cliente = input("Nome do cliente: ")
        
        ordem = OrdemServico(cliente, veiculo_escolhido)
        
        while True:
            print("\nSelecione o serviço:")
            print("1 - Troca de Óleo")
            print("2 - Alinhamento")
            print("0 - Concluir serviços")
            op_servico = input("Opção: ")
            
            if op_servico == "1":
                mao_de_obra = float(input("Valor da mão de obra: "))
                materiais = float(input("Valor dos materiais: "))
                servico = TrocaOleo(mao_de_obra, materiais)
                ordem.adicionar_servico(servico)
                print("Serviço de Troca de Óleo adicionado!")
            elif op_servico == "2":
                mao_de_obra = float(input("Valor da mão de obra: "))
                taxa = float(input("Taxa do equipamento: "))
                servico = Alinhamento(mao_de_obra, taxa)
                ordem.adicionar_servico(servico)
                print("Serviço de Alinhamento adicionado!")
            elif op_servico == "0":
                break
            else:
                print("Opção inválida!")
        
        ordens.append(ordem)
        print("Ordem de serviço registrada com sucesso!")
    except ValueError as e:
        print(f"Erro: {e}")

def listar_ordens():
    print("\n--- LISTAR ORDENS DE SERVIÇO ---")
    if not ordens:
        print("Nenhuma ordem de serviço registrada.")
        return
    
    for i, o in enumerate(ordens):
        print(f"\n[{i + 1}] Cliente: {o.cliente} | Veículo: {o.veiculo.modelo} ({o.veiculo.placa}) | Total: R$ {o.calcular_total():.2f}")

def exibir_orcamento():
    print("\n--- EXIBIR ORÇAMENTO ---")
    if not ordens:
        print("Nenhuma ordem de serviço registrada.")
        return
    
    for i, o in enumerate(ordens):
        print(f"{i + 1} - Cliente: {o.cliente} | Veículo: {o.veiculo.modelo} ({o.veiculo.placa})")
    
    try:
        idx = int(input("Escolha o número da ordem de serviço: ")) - 1
        if 0 <= idx < len(ordens):
            ordens[idx].resumo()
        else:
            print("Ordem de serviço inválida.")
    except ValueError as e:
        print(f"Erro: {e}")

def menu():
    while True:
        print("\n--- OFICINA MECÂNICA ---")
        print("1 - Cadastrar veículo")
        print("2 - Lançar serviço")
        print("3 - Listar ordens de serviço")
        print("4 - Exibir orçamento")
        print("0 - Sair")
        
        opcao = input("Opção: ")
        
        try:
            if opcao == "1":
                cadastrar_veiculo()
            elif opcao == "2":
                lancar_servico()
            elif opcao == "3":
                listar_ordens()
            elif opcao == "4":
                exibir_orcamento()
            elif opcao == "0":
                print("Encerrando o sistema...")
                break
            else:
                print("Opção inválida!")
        except Exception as e:
            print(f"Erro: {e}")

if __name__ == "__main__":
    menu()