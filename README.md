# talkingData
DatasetsPickles.py - создает в папке myPickler файлы
1. channelsDict.train.txt - структуру данных словарь из вхождений и скачиваний для train;
2. channelsNumbers.train.txt - номера каналов в train;
3. channelsDict.train_sample.txt - структуру данных словарь из вхождений и скачиваний для train_sample;
4. channelsNumbers.train_sample.txt - номера каналов в train_sample;

Все файлы сохранены с помощью pickle, так как сохранены в виде структур данных set (для первого и треьего) и dict (для второго и четвертого) 

protocol.txt - вывод в консоль работы DatasetsPickles.py. Содержит информацию о канале, числе сессий и скачиваний для выборок
