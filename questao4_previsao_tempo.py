"""
Parte 3 — Mini Projeto: Previsão do Tempo com Python
Consome a API pública do Open-Meteo para exibir a previsão dos próximos 7 dias.
Com terminal interativo
"""

import requests
from datetime import datetime


def buscar_cidade(nome):
    """Busca coordenadas de uma cidade pelo nome usando a API de geocodificação do Open-Meteo."""
    url = "https://geocoding-api.open-meteo.com/v1/search"
    params = {"name": nome, "count": 5, "language": "pt"}

    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()

    dados = response.json()
    if "results" not in dados or len(dados["results"]) == 0:
        return None

    return dados["results"]


def buscar_previsao(latitude, longitude):
    """Busca a previsão dos próximos 7 dias para as coordenadas informadas."""
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "daily": "temperature_2m_max,temperature_2m_min",
        "timezone": "America/Sao_Paulo",
        "forecast_days": 7,
    }

    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()

    return response.json()


def formatar_data(data_str):
    """Converte 'YYYY-MM-DD' para 'DD/MM'."""
    data = datetime.strptime(data_str, "%Y-%m-%d")
    return data.strftime("%d/%m")


def formatar_data_completa(data_str):
    """Converte 'YYYY-MM-DD' para 'DD/MM/YYYY'."""
    data = datetime.strptime(data_str, "%Y-%m-%d")
    return data.strftime("%d/%m/%Y")


def exibir_previsao(nome_cidade, dados):
    """Exibe a previsão formatada no terminal."""
    diario = dados["daily"]
    datas = diario["time"]
    maximas = diario["temperature_2m_max"]
    minimas = diario["temperature_2m_min"]

    # Calcula estatísticas do período
    todas_temps = maximas + minimas
    temp_media = sum(todas_temps) / len(todas_temps)

    max_periodo = max(maximas)
    min_periodo = min(minimas)
    dia_max = formatar_data(datas[maximas.index(max_periodo)])
    dia_min = formatar_data(datas[minimas.index(min_periodo)])

    periodo_inicio = formatar_data_completa(datas[0])
    periodo_fim = formatar_data_completa(datas[-1])

    print()
    print("=" * 40)
    print(f"  Previsão para: {nome_cidade}")
    print("=" * 40)
    print(f"  Período: {periodo_inicio} a {periodo_fim}")
    print(f"  Temperatura média: {temp_media:.1f}°C")
    print(f"  Máxima do período: {max_periodo}°C ({dia_max})")
    print(f"  Mínima do período: {min_periodo}°C ({dia_min})")
    print("-" * 40)

    for i in range(len(datas)):
        data = formatar_data(datas[i])
        print(f"  {data}  Min: {minimas[i]}°C  Max: {maximas[i]}°C")

    print("=" * 40)
    print()


def selecionar_cidade(resultados):
    """Permite ao usuário escolher entre múltiplos resultados de busca."""
    if len(resultados) == 1:
        cidade = resultados[0]
        nome = cidade.get("name", "")
        admin = cidade.get("admin1", "")
        pais = cidade.get("country", "")
        print(f"\nCidade encontrada: {nome}, {admin} - {pais}")
        return cidade

    print("\nVárias cidades encontradas:")
    for i, cidade in enumerate(resultados, 1):
        nome = cidade.get("name", "")
        admin = cidade.get("admin1", "")
        pais = cidade.get("country", "")
        print(f"  {i}. {nome}, {admin} - {pais}")

    while True:
        escolha = input("\nDigite o número da cidade desejada: ").strip()
        if escolha.isdigit() and 1 <= int(escolha) <= len(resultados):
            return resultados[int(escolha) - 1]
        print("Opção inválida. Tente novamente.")


def main():
    print("=" * 40)
    print("  Previsão do Tempo — Open-Meteo API")
    print("=" * 40)

    while True:
        nome = input("\nDigite o nome de uma cidade (ou 'sair' para encerrar): ").strip()

        if nome.lower() == "sair":
            print("Até logo!")
            break

        if not nome:
            print("Por favor, digite um nome de cidade válido.")
            continue

        try:
            # Busca a cidade
            resultados = buscar_cidade(nome)
            if resultados is None:
                print(f"Nenhuma cidade encontrada com o nome '{nome}'. Tente novamente.")
                continue

            # Seleção da cidade
            cidade = selecionar_cidade(resultados)
            nome_exibicao = cidade.get("name", "")
            admin = cidade.get("admin1", "")
            if admin:
                nome_exibicao += f", {admin}"

            # Busca a previsão
            previsao = buscar_previsao(cidade["latitude"], cidade["longitude"])
            exibir_previsao(nome_exibicao, previsao)

        except requests.exceptions.ConnectionError:
            print("Erro: sem conexão com a internet. Verifique sua rede.")
        except requests.exceptions.Timeout:
            print("Erro: a requisição demorou demais. Tente novamente.")
        except requests.exceptions.HTTPError as e:
            print(f"Erro na API: {e}")
        except (KeyError, IndexError):
            print("Erro: resposta inesperada da API. Tente novamente.")


if __name__ == "__main__":
    main()
