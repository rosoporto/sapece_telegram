# Постинг снимков космоса в Telegram

## Описание проекта

Скрипт автоматизирует скачивание фото на тему космоса и размещает их в Telegram. Данные на фото берутся по Api с SpaceX и NASA. Документация по перечисленным ресурсам:
* [SpaceX](https://github.com/r-spacex/SpaceX-API "Репозиторий на Github API SpaceX")
* [NASA](https://api.nasa.gov/ "Сайт NASA")

## Требование к окружению

Проект писался в Windows среде на Python 3.9

## Как установить
Испоьзовать pip для установки зависимостей:
```python
pip install -r requirements.txt
```
Получите токен у [NASA](https://api.nasa.gov/ "Сайт NASA") и [Telegram](https://t.me/botfather). В корне проекта создайте файл `.env` с данными (токен) для авторизации запросов на api:
```python
NASA_KEY=ТОКЕН_NASA
TELEGRAM_KEY=ТОКЕН_Telegram
```
### Как запустить

Запустите выполнение программы из консоли командой:
```python
python main.py images sx apod epic 4
```
или воспользуйтесь справкой через команду:
```python
python main.py -h
```
чтобы узнать подробно какие аргументы командной строки за что отвечают.
### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org).