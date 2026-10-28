# Sistema de Oficina Mecânica

## Descrição
Projeto desenvolvido em Python para cadastrar veículos, lançar serviços e gerenciar ordens de serviço em uma oficina mecânica, aplicando conceitos avançados de Programação Orientada a Objetos (POO), encapsulamento, herança, polimorfismo e tratamento de exceções.

## Funcionalidades
* Cadastrar veículos com validação de dados (placa, modelo e ano)[cite: 6].
* Registrar serviços específicos (Troca de Óleo e Alinhamento) utilizando classes abstratas e polimorfismo[cite: 7].
* Gerenciar ordens de serviço associando clientes, veículos e múltiplos serviços[cite: 8].
* Calcular o valor total dos orçamentos automaticamente[cite: 8].
* Listar todas as ordens de serviço e emitir resumos detalhados[cite: 8].
* Menu interativo no terminal com tratamento amigável de erros[cite: 5].

## Tecnologias Utilizadas
* **Python 3.x** (Não requer a instalação de bibliotecas externas).

## Estrutura de Arquivos
```text
oficina_mecanica/
│
├── main.py              # Ponto de entrada e menu interativo do sistema[cite: 5]
├── veiculo.py           # Classe Veiculo com validações e propriedades[cite: 6]
├── servico.py           # Classe abstrata Servico e serviços específicos[cite: 7]
├── ordem_servico.py     # Classe OrdemServico para controlo de atendimento[cite: 8]
└── README.md            # Documentação do projeto