#!/bin/bash

info=$1
logs=access.log
result=requests_info.txt

count_str() {
    echo "Общее количество запросов" >> $result
    wc -l $logs | awk '{print $1}' >> $result
    echo >> $result
}

count_type_requests() {
    echo "Общее количество запросов по типу (тип, количество)" >> $result
    cat $logs | awk '{print $6}' | awk -F"\"" '{print$2}' | sort | uniq -c | awk '{print $2" "$1}' >> $result
    echo >> $result
}

top_popular_requests() {
    echo "Топ 10 самых частых запросов (url, количество)" >> $result
    cat $logs | awk '{print $7}' | sort | uniq -c | sort -n -r | head | awk '{print $2" "$1}' >> $result
    echo >> $result
}

top_5_requests_with_client_error() {
    echo "Топ 5 самых больших по размеру запросов, которые завершились клиентской (4ХХ) ошибкой (url, статус, размер, ip)" >> $result
    cat $logs | awk '{print $1" "$7" "$9" "$10}' | sort -n -r -k4 | grep -w -e 4[0-9][0-9] | head -n 5 | awk '{print $2" "$3" "$4" "$1}' >> $result
    echo >> $result
}

top_5_clients_with_server_error_requests() {
    echo "Топ 5 пользователей по количеству запросов, которые завершились серверной (5ХХ) ошибкой (ip, количество)" >> $result
    cat $logs | awk '{print $1" "$9" "}' | grep -w -e 5[0-9][0-9] | sort | uniq -c | sort -n -r -k1 |head -n 5 | awk '{print $2" "$1}' >> $result
    echo >> $result
}

if [ $info == 1 ]
then
    cp /dev/null $result
    count_str
elif [ $info == 2 ]
then
    cp /dev/null $result
    count_type_requests
elif [ $info == 3 ]
then
    cp /dev/null $result
    top_popular_requests
elif [ $info == 4 ]
then
    cp /dev/null $result
    top_5_requests_with_client_error
elif [ $info == 5 ]
then
    cp /dev/null $result
    top_5_clients_with_server_error_requests
elif [ $info == '-all' ]
then
    cp /dev/null $result
    count_str
    count_type_requests
    top_popular_requests
    top_5_requests_with_client_error
    top_5_clients_with_server_error_requests
elif [ $info == '-h' ]
then
    echo "1 - Общее количество запросов"
    echo "2 - Общее количество запросов по типу"
    echo "3 - Топ 10 самых частых запросов"
    echo "4 - Топ 5 самых больших по размеру запросов, которые завершились клиентской (4ХХ) ошибкой"
    echo "5 - Топ 5 пользователей по количеству запросов, которые завершились серверной (5ХХ) ошибкой"
    echo "-h - Это сообщение"
    echo "-all - Вся информация из 1-5"
else
    echo "Неверный аргумент. Воспользуйтесь командой requests_info.sh -h, чтобы узнать, какие аргументы поддерживаются"

fi
