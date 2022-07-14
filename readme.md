### Binance Scrapper Bot
#### Docker-compose 
- `docker-compose build` сборка образа
- `docker-compose up` включить сборку
- `docker-compose down -v --remove-orphans` выключить контейнеры

#### Docker
- `docker ps` список контейнеров
<<<<<<< HEAD
- `docker exec -it binancescrapperbot_scrapper_1 /bin/bash` подключение к контейнеру
=======
- `docker exec -it binancescrapperbot_scrapper_1 /bin/bash` подключиться к контейнеру
>>>>>>> 9c88b7bbd092ef566c9e875c175e83010c9a740b
- `docker volume prune` очистить тома
- `docker system prune -a` очистить системный кэш

#### Git
- `git config -l` отобразить все конфигурации git
- `git remote set-url origin https://github.com/AntonBliznyuk/BinanceScrapperBot.git` сменить репозиторий
