# Bot de Automação de Busca de SKUs no Mercado Livre

Este projeto é uma automação em Python usando Selenium para realizar a busca de SKUs no Mercado Livre e verificar a existência de anúncios para cada código. Ele foi desenvolvido para facilitar a busca em massa de produtos e identificar rapidamente a disponibilidade de anúncios na plataforma.

[![Assista ao vídeo no YouTube](https://img.youtube.com/vi//IbqwswYYAKs/maxresdefault.jpg)](https://youtube.com/shorts/IbqwswYYAKs?feature=share)


## Funcionalidades

- **Automação de Busca**: Insere e pesquisa automaticamente uma lista de SKUs na barra de busca do Mercado Livre.
- **Verificação de Disponibilidade**: Para cada SKU, verifica se há anúncios disponíveis através da presença de uma checkbox específica habilitada ou desabilitada.
- **Feedback Automático**: Exibe no console se o anúncio foi encontrado ou não para cada SKU, com base na resposta da página.
- **Lógica de Limpeza**: Limpa automaticamente o campo de pesquisa após cada busca para inserir o próximo SKU.

## Pré-requisitos

- **Python 3.x**
- **Selenium**: Ferramenta de automação de navegador.
- **Google Chrome** com depuração remota habilitada
- **ChromeDriver** compatível com a versão do Google Chrome

## Configuração e Uso

1. Clone o repositório e instale o Selenium:
   ```bash
   pip install selenium
2. Abra o Chrome em modo de depuração:
"C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222 --user-data-dir="C:/chrome_dev"
3. Configure o script para se conectar à instância do Chrome aberta.
4. Execute o script busca_sku_mercadolivre.py e verifique os resultados no console.

Observações
Este script foi desenvolvido para uso interno, em cenários onde há grande quantidade de SKUs a serem pesquisados. É recomendável usá-lo em conformidade com os termos de serviço da plataforma.
