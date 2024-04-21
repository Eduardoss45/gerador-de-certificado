# Aplicação de Geração de Certificados

Este é um exemplo de aplicação Python para geração automatizada de certificados com base em dados de um arquivo Excel.

## Funcionalidades

- Leitura de dados de um arquivo Excel.
- Geração de certificados personalizados com base nos dados fornecidos.
- Suporte a diferentes fontes e estilos de certificados.
- Interface simples e fácil de usar.

## Instalação

1. Clone este repositório:

    ```
    git clone https://github.com/Eduardoss45/gerador_de_certificado.git
    ```

2. Instale as dependências:

    ```
    pip install -r requirements.txt
    ```

## Utilização

1. Certifique-se de ter um arquivo Excel contendo os dados necessários para geração de certificados.

2. Execute o script `app.py`:

    ```
    python gerar_certificados.py
    ```

3. Siga as instruções para fornecer o caminho do arquivo Excel e visualizar os certificados gerados.

## Estrutura do Projeto

- `app.py`: Script principal para execução da aplicação.
- `planilha_alunos.xlsx`: Arquivo de exemplo contendo os dados dos alunos.
- `certificado_padrao.jpg`: Modelo do certificado.
- `fonts/`: Diretório contendo as fontes necessárias para renderização de texto nos certificados.

## Contribuindo

Se você quiser contribuir para este projeto, sinta-se à vontade para abrir uma issue ou enviar um pull request. Toda contribuição é bem-vinda!

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).
