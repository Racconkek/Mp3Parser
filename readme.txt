Запуск: Parser.py
usage: MP3 Parser [-h] [-p] [-v1] [-v2] [-f FILE]
Gives you information about mp3 file
arguments:
  -h, --help            show this help message and exit
  -p, --parse           Parse all mp3 file
  -v1, --ID3v1          Parse ID3v1 tag in mp3 file
  -v2, --ID3v2          Parse ID3v2 tag in mp3 file
  -f FILE, --file FILE  Write here absolute path to your mp3 file

Когда программа уже запущена, доступны следующие команды:
1) parse - распарсить всю информацию
2) parse tag1 - распарсить ID3v1 тэг
3) parse tag2 - распарсить ID3v2 тэг
4) set file *.mp3 - запомнить новый файл для парсинга в формате .mp3
5) play - воспроизвести текущий файл
6) end - завершить работу