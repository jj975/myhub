#! /bin/bash
clear

sudo apt install -y apache2
sudo systemctl enable apache2


if [ -f /var/www/html/index.html ]; then
  echo "apache2 успішно встановлено"
  # видалення bash скрипт
  rm "$0"
else
  echo "Помилка: apache2 не встановлено спробуй ще раз"
fi
