# talkingData
DatasetsPickles.py - создает в папке myPickler файлы
1. channelsDict.train.txt - структуру данных словарь, где ключом выступает номер канала, а значением - list из числа сессий и скачиваний; сформирован по train;
2. channelsNumbers.train.txt - номера каналов в train;
3. channelsDict.train_sample.txt - структуру данных словарь, где ключом выступает номер канала, а значением - list из числа сессий и скачиваний; сформирован по train_sample;
4. channelsNumbers.train_sample.txt - номера каналов в train_sample;

Все файлы сохранены с помощью pickle, так как сохранены в виде структур данных dict (для первого и треьего) и set (для второго и четвертого) 

Также в папке myPickler сохранен protocol.txt - текстовый файл вывода в консоль работы DatasetsPickles.py. Представляет собой список типа ключ-значение из channelsDict.train.txt


train.txt содержит 184903891 строк
train_sample.txt содержит 100001 строк
merged содержит 185003891 строк
