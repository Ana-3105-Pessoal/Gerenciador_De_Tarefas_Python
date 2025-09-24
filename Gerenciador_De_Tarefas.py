#Cores
reset = "\033[0m"
cyan = "\033[96m"
verde = "\033[92m"
red = "\033[91m"
roxo = "\033[94m"
amarelo = "\033[93m"

def menu(): #Exibe o menu para o usuário
  print(f'{cyan}--- Gerenciador de Tarefas ---{reset}')
  print(f'{cyan}1.{reset}{verde} Adicionar uma nova tarefa {reset}')
  print(f'{cyan}2.{reset}{verde} Marcar uma tarefa como concluída {reset}')
  print(f'{cyan}3.{reset}{verde} Listar todas as tarefas {reset}')
  print(f'{cyan}4.{reset}{verde} Listar todas as tarefas pendentes {reset}')
  print(f'{cyan}5.{reset}{verde} Listar todas as tarefas concluídas {reset}')
  print(f'{cyan}6.{reset}{verde} FIM {reset}')

def adicionar_tarefa(lista_tarefas):
  while True:
      tarefa = input('Descrição da nova tarefa (0 para voltar): ')
      if tarefa == '0':
        print(f'{red}Voltando ao menu...{reset}')
        break
      if not tarefa.strip(): #Verifica se não está vazia ou com espaços
        print(f'{red}A descrição está vazia!{reset}')
      else:
        nova_tarefa = {'tarefa': tarefa, 'concluida': False}
        lista_tarefas.append(nova_tarefa)
        print(f'{verde}Tarefa adicionada com sucesso!{reset}')
  print(f'{cyan}-{reset}'*50)
  print('\n')
  return lista_tarefas

def marcar_concluida(lista_tarefas):
  print(f'{cyan}--- Marcar Tarefa como Concluída ---{reset}')
  if not listar_tarefas(lista_tarefas, pendentes=True, concluidas=False):
    print(f'{amarelo}Nenhuma tarefa pendente para marcar.{reset}')
    print(f'{cyan}-{reset}'*50)
    print('\n')
    return lista_tarefas

  while True:
    try:
      escolha = int(input('Qual o número da tarefa a ser marcada como concluída? (0 para voltar): '))
      if escolha == 0:
        print(f'{red}Voltando ao menu...{reset}')
        break

      indice = escolha - 1


      if 0 <= indice < len(lista_tarefas):
        if lista_tarefas[indice]['concluida']:
          print(f'{red}Essa tarefa já está concluída!{reset}')
        else:
          lista_tarefas[indice]['concluida'] = True
          print(f'{verde}Tarefa concluída com sucesso!{reset}')
          break
      else:
        print(f'{red}Número de tarefa inválido!{reset}')
    except ValueError:
      print(f'{red}ENTRADA INVÁLIDA! Digite um número{reset}')
  print(f'{cyan}-{reset}'*50)
  print('\n')
  return lista_tarefas

def listar_tarefas(lista_tarefas, pendentes=True, concluidas=True):
  tarefas_encontrada = False
  for i, tarefa in enumerate(lista_tarefas):
    if (tarefa['concluida'] and concluidas) or (not tarefa['concluida'] and pendentes):
      status = f'{verde}Concluída{reset}' if tarefa['concluida'] else f'{red}Pendente{reset}'
      print(f'{i+1}.{tarefa["tarefa"]} - {status}')
      tarefas_encontrada = True
  return tarefas_encontrada


def main():
  minhas_tarefas = []

  while True:
    menu()
    print(f'{cyan}-{reset}'*50)
    opcao = input('Escolha uma opção: ')
    print(f'{cyan}-{reset}'*50)

    if opcao == '1':
      minhas_tarefas = adicionar_tarefa(minhas_tarefas)
    elif opcao == '2':
      minhas_tarefas = marcar_concluida(minhas_tarefas)
    elif opcao == '3':
      print(f'{cyan}--- Todas as Tarefas ---{reset}')
      if not listar_tarefas(minhas_tarefas):
        print(f'{amarelo}Nenhuma tarefa cadastrada.{reset}')
      print(f'{cyan}-{reset}'*50)
      print('\n')
    elif opcao == '4':
      print(f'{cyan}--- Tarefas Pendentes ---{reset}')
      if not listar_tarefas(minhas_tarefas,pendentes=True, concluidas=False):
        print(f'{roxo}Parabéns! Nenhuma tarefa pendente.{reset}')
      print(f'{cyan}-{reset}'*50)
      print('\n')
    elif opcao == '5':
      print(f'{cyan}--- Tarefas Concluídas ---{reset}')
      if not listar_tarefas(minhas_tarefas,pendentes=False, concluidas=True):
        print(f'{roxo}Nenhuma tarefa foi concluída ainda.{reset}')
      print(f'{cyan}-{reset}'*50)
      print('\n')
    elif opcao == '6':
      print(f'{red}Encerrando o programa...{reset}')
      break
    else:
      print(f'{red}OPÇÃO INVÁLIDA! Tente novamente.{reset}')


if __name__ == "__main__":
    main()
