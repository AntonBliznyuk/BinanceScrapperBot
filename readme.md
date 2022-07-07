### Crypto Bot
#### Docker-compose 
- `docker-compose build` сборка образа
- `docker-compose up` поднять сборку
- `docker-compose down -v --remove-orphans` потушить контейнеры

#### Docker
- `docker ps` список контейнеров
- `docker exec -it cryptobot_scrapper_1 /bin/bash` подрубится к контейнеру
- `docker volume prune` очистить волюмы
- `docker system prune -a` очистить системный кэш

#### Git
- `git config -l` отобразить все конфигурации git
- `git remote set-url origin https://github.com/AntonBliznyuk/BinanceScrapperBot.git` сменить репозиторий
