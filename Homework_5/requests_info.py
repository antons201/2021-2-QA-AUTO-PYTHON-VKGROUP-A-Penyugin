import collections
import re
import json
import sys


out = open('requests_info.txt', 'w')
json_data = {}
json_file = False


def count_str():
    f = open('access.log', 'r')
    if not json_file:
        out.write("Общее количество запросов\n")
        out.write(str(sum(1 for line in f)) + "\n")
        out.write("\n")
    else:
        json_data["total number of requests"] = str(sum(1 for line in f))
    f.close()


def count_type_requests():
    f = open('access.log', 'r')
    request_types = collections.Counter()
    for line in f:
        request_types[line.split(" ")[5].split("\"")[1]] += 1

    if not json_file:
        out.write("Общее количество запросов по типу (тип, количество)\n")
        for request_type in request_types:
            out.write(request_type + " " + str(request_types[request_type]) + "\n")
        out.write("\n")
    else:
        json_types = []
        for request_type in request_types:
            json_types.append({'type': request_type, 'count': request_types[request_type]})
        json_data["total number of requests by type"] = json_types
    f.close()


def top_popular_requests():
    f = open('access.log', 'r')
    request_urls = collections.Counter()
    for line in f:
        request_urls[line.split(" ")[6]] += 1

    if not json_file:
        out.write("Топ 10 самых частых запросов (url, количество)\n")
        for request_url in request_urls.most_common(10):
            out.write(str(request_url[0] + "%6d" % request_url[1]) + "\n")
        out.write("\n")
    else:
        json_requests = []
        for request_url in request_urls.most_common(10):
            json_requests.append({'url': request_url[0], 'count': request_url[1]})
        json_data["top 10 most frequent requests"] = json_requests
    f.close()


def top_5_requests_with_client_error():
    f = open('access.log', 'r')
    requests_info = []
    for line in f:
        if line.split(" ")[9] != "-" and re.match('4[0-9][0-9]', line.split(" ")[8]) is not None:
            requests_info.append(
                [line.split(" ")[0], line.split(" ")[6], line.split(" ")[8], int(line.split(" ")[9])])
    requests_info.sort(key=lambda x: x[3], reverse=True)

    if not json_file:
        out.write("Топ 5 самых больших по размеру запросов, которые завершились клиентской (4ХХ) ошибкой (url, статус, "
                  "размер, ip)\n")
        for i in range(5):
            out.write(requests_info[i][1] + " " + requests_info[i][2] + " " + str(requests_info[i][3]) + " " +
                      requests_info[i][0] + "\n")
        out.write("\n")
    else:
        json_requests = []
        for i in range(5):
            json_requests.append(
                {'url': requests_info[i][1], 'status': requests_info[i][2], 'size': requests_info[i][3],
                 'ip': requests_info[i][0]})
        json_data["top 5 largest requests in size that ended with a client (4XX) error"] = json_requests
    f.close()


def top_5_clients_with_server_error_requests():
    f = open('access.log', 'r')
    requests_info = []
    requests_users_count = collections.Counter()
    for line in f:
        if re.match('5[0-9][0-9]', line.split(" ")[8]) is not None:
            requests_info.append([line.split(" ")[0], int(line.split(" ")[8])])

    for request in requests_info:
        requests_users_count[request[0]] += 1

    if not json_file:
        out.write("Топ 5 пользователей по количеству запросов, которые завершились серверной (5ХХ) ошибкой (ip, "
                  "count)\n")
        for requests_user_count in requests_users_count.most_common(5):
            out.write(requests_user_count[0] + " " + str(requests_user_count[1]) + "\n")
        out.write("\n")
    else:
        json_users = []
        for requests_user_count in requests_users_count.most_common(5):
            json_users.append({'ip': requests_user_count[0], 'count': requests_user_count[1]})
        json_data["top 5 users by the number of requests that ended with a server (5XX) error"] = json_users
    f.close()

if len(sys.argv) < 2 or len(sys.argv) > 3:
    print("Неверный аргумент. Воспользуйтесь командой requests_info.sh -h, чтобы узнать, какие аргументы поддерживаются")
    exit(1)

if len(sys.argv) == 3:
    if sys.argv[2] == "--json":
        json_file = True

if sys.argv[1] == '1':
    count_str()
    if json_file:
        json.dump(json_data, out, indent=4)
elif sys.argv[1] == '2':
    count_type_requests()
    if json_file:
        json.dump(json_data, out, indent=4)
elif sys.argv[1] == '3':
    top_popular_requests()
    if json_file:
        json.dump(json_data, out, indent=4)
elif sys.argv[1] == '4':
    top_5_requests_with_client_error()
    if json_file:
        json.dump(json_data, out, indent=4)
elif sys.argv[1] == '5':
    top_5_clients_with_server_error_requests()
    if json_file:
        json.dump(json_data, out, indent=4)
elif sys.argv[1] == '-all':
    count_str()
    count_type_requests()
    top_popular_requests()
    top_5_requests_with_client_error()
    top_5_clients_with_server_error_requests()
    if json_file:
        json.dump(json_data, out, indent=4)
elif sys.argv[1] == '-h':
    print("Первый аргумент (обязательный):\n"
          "1 - Общее количество запросов\n"
          "2 - Общее количество запросов по типу\n"
          "3 - Топ 10 самых частых запросов\n"
          "4 - Топ 5 самых больших по размеру запросов, которые завершились клиентской (4ХХ) ошибкой\n"
          "5 - Топ 5 пользователей по количеству запросов, которые завершились серверной (5ХХ) ошибкой\n"
          "-h - Это сообщение\n"
          "-all - Вся информация из 1-5\n"
          "Второй аргумент (опциональный):\n"
          "--json - Вывести информацию в формате json")
else:
    print("Неверный аргумент. Воспользуйтесь командой requests_info.py -h, чтобы узнать, какие аргументы поддерживаются")

out.close()