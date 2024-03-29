# Тема: Практические задачи по Linux

## Практическая работа

1. Переходим на
   сайт [https://overthewire.org/wargames/bandit/bandit0.html](https://overthewire.org/wargames/bandit/bandit0.html)
2. Там указан ip-адрес сервера и порт, на котором он слушает. Подключаемся к нему по ssh.
    1. Имя пользователя: bandit0
    2. Пароль: bandit0
    3. Чтобы подключиться, нужно написать в терминале: `ssh bandit0@bandit.labs.overthewire.org -p 2220`

Пояснения к заданиям:
0 -> 1: найти файл `readme` в домашней директории пользователя - внутри файла есть пароль для следующего уровня

Переключение на следующий уровень: `ssh bandit<номер следующего уровня>@bandit.labs.overthewire.org -p 2220` (пароль для подключения - найденный пароль)

1 -> 2:
найти файл с паролем

Тут нужно использовать команду `ls` - она показывает список файлов в текущей директории. Видим, что в директории есть
файл `-
`. Попробуем прочитать его содержимое командой `cat -`. Видим, что это не просто файл, а специальный файл, который
содержит пароль для следующего уровня.

Чтобы прочитать это содержимое, нужно использовать команду `cat ./-`. Видим, что в файле есть пароль для следующего
уровня.

<!---
найти файл `-` в домашней директории пользователя - внутри файла есть пароль для следующего уровня
-->
2 -> 3: найти файл с паролем

Тут файл называется `spaces in this filename` - нужно использовать кавычки, чтобы указать, что это одно имя файла
<!---
найти файл `spaces in this filename` в домашней директории пользователя - внутри файла есть пароль для следующего уровня
-->

3 -> 4: найти файл с паролем

Тут файл скрыт - нужно использовать флаг `-a` для команды `ls` - он показывает скрытые файлы.
То есть нужно написать `ls -a`

<!---
найти файл `inhere/.hidden` в домашней директории пользователя - внутри файла есть пароль для следующего уровня
-->


4 -> 5: найти файл с паролем

Тут множество файлов и папок, и нужно найти тот, который можно прочитать. Для этого нужно использовать команду `file <имя файла>`.
Она показывает тип файла. Например, введите `file ./*`. 


5 -> 6: найти файл с паролем

Тут тоже нужно использовать команду `file <имя файла>`. Но в этот раз нужно найти файл, который весит 1033 байта.

Для это нужно использовать команду `find ./ -size 1033c`. Она покажет файлы, которые весят 1033 байта.



