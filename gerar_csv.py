import csv
import random
from faker import Faker
from datetime import datetime, timedelta

fake = Faker('pt_BR')  # Configura para gerar dados em português brasileiro


def gerar_cpf():
    # Gera os 9 primeiros dígitos
    cpf = [random.randint(0, 9) for _ in range(9)]

    # Calcula o primeiro dígito verificador
    soma = sum((i + 1) * cpf[i] for i in range(9))
    digito1 = soma % 11
    digito1 = digito1 if digito1 < 10 else 0
    cpf.append(digito1)

    # Calcula o segundo dígito verificador
    soma = sum((i + 2) * cpf[i] for i in range(10))
    digito2 = soma % 11
    digito2 = digito2 if digito2 < 10 else 0
    cpf.append(digito2)

    # Formata no padrão brasileiro
    return f"{cpf[0]}{cpf[1]}{cpf[2]}.{cpf[3]}{cpf[4]}{cpf[5]}.{cpf[6]}{cpf[7]}{cpf[8]}-{cpf[9]}{cpf[10]}"


def gerar_vencimento():
    start_date = datetime(2022, 1, 1)
    end_date = datetime(2027, 12, 31)
    delta = end_date - start_date
    random_days = random.randint(0, delta.days)
    return (start_date + timedelta(days=random_days)).strftime('%d/%m/%Y')


def formatar_valor(valor):
    # Formata com 2 casas decimais e vírgula
    return f"{valor:,.2f}".replace(".", "X").replace(",", ".").replace("X", ",")


with open('dados_ficticios.csv', mode='w', newline='', encoding='utf-8') as arquivo_csv:
    escritor = csv.writer(arquivo_csv, delimiter=';')
    escritor.writerow(['Nome', 'Valor', 'CPF', 'Vencimento'])

    for _ in range(5000):
        nome = fake.name()  # Gera nome completo
        valor = formatar_valor(random.uniform(
            10, 1000))  # Valor entre 10 e 1000
        cpf = gerar_cpf()  # CPF formatado
        vencimento = gerar_vencimento()  # Data formatada

        escritor.writerow([nome, valor, cpf, vencimento])

print("Arquivo 'dados_ficticios.csv' gerado com sucesso!")
