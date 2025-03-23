# stackoverflow_scraper
Para o uso do scraper, iniciar um ambiente virtual na raíz do projeto com o comando a seguir:

source venv/bin/activate

A partir disso, instalar todos os pacotes necessários para rodar o código:

python -m pip install -r requirements.txt

Após instalado os requirements, o programa pode ser rodado com o comando python stackoverflow.py. Esse comando irá extrair as informações dos últimos 50 comentários realizados no Stack Overflow e salvar todos no banco de dados dados.db.

## Sqlite - justificativa de uso

O Sqlite foi escolhido pela sua leveza e simplicidade. Ele é um banco de dados leve e já vem embutido com o python, o que significa que ele não requer a instalação de um servidor separado para funcionar. Dessa maneira, sua configuração e seu uso é muito simples e direto, principalmente para aplicações pequenas (como essa). 
