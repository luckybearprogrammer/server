from flask import Flask, request, jsonify
import os

app = Flask(__name__)


# Функция для записи числа в файл
def write_to_file(number, idUser):
    with open('numbers.txt', 'a+', encoding="utf-8") as file:
        file.write(str(number) + " " + str(idUser) + '\n')


# API endpoint для записи числа в файл

@app.route('/write_number', methods=['POST'])
def write_number():
    content = request.json
    number = content['number']
    idUser = content['iduser']
    with open('numbers.txt', 'r', encoding="utf-8") as file:
        base = {int(line.strip().split()[0]): line.strip().split()[1] for line in file}
    key = next(key for key, value in base.items() if value == idUser)
    base[number] = base.pop(key)
    base = dict(sorted(base.items()))
    with open("numbers.txt", 'w', encoding="utf-8") as file:
        for key, item in base.items():
            file.write(f"{key} {item}\n")

    return jsonify({'message': 'Number has been written to the file'})


@app.route('/mesto', methods=['POST'])
def mesto():
    content = request.json
    idUser = content['iduser']
    with open('numbers.txt', 'r', encoding="utf-8") as file:
        base = {int(line.strip().split()[0]): line.strip().split()[1] for line in file}
    for index, (key, value) in enumerate(base.items()):
        if value == idUser:
            return jsonify({"message": "ок", "index": index+1})


@app.route('/top', methods=['POST'])
def top():
    # with open('numbers.txt', 'r') as file:
    #     base = {int(line.strip().split()[0]): line.strip().split()[1] for line in file}
    base = ""
    with open('numbers.txt', 'r', encoding="utf-8") as file:
        for line in file:
            base += line.strip() + "lol"
    return jsonify({'message': 'you are in base', 'top': base})


@app.route('/can', methods=['POST'])
def can():
    content = request.json
    nick = content['nick']
    with open('users.txt', 'r') as file:
        base = [line.strip() for line in file]
    if nick not in base:
        with open("users.txt", "a+", encoding="utf-8") as file:
            file.write(f"{nick}\n")
        with open("numbers.txt", "a+", encoding="utf-8") as file:
            file.write(f"999 {nick}\n")
        return jsonify({'message': 'nice', 'can': True})
    else:
        return jsonify({'message': 'you are in base', 'can': False})


@app.route('/myresult', methods=['POST'])
def my_result():
    content = request.json
    nick = content['nick']
    with open('numbers.txt', 'r', encoding="utf-8") as file:
        base = {int(line.strip().split()[0]): line.strip().split()[1] for line in file}
    print(base)
    keys = list(base.keys())
    index = list(base.values()).index(nick)
    key = keys[index]
    return jsonify({'message': 'good', 'result': key})


# Функция для сортировки чисел в файле
def sort_numbers_in_file():
    with open('numbers.txt', 'r', encoding="utf-8") as file:
        base = {int(line.strip().split()[0]): line.strip().split()[1] for line in file}
    base = dict(sorted(base.items(), reverse=True))
    with open('numbers.txt', 'w', encoding="utf-8") as file:  # Открываем файл на перезапись
        for key, item in base.items():
            file.write(f"{key} {item}\n")


if __name__ == '__main__':
    if not os.path.exists('numbers.txt'):
        open('numbers.txt', 'w').close()
    if not os.path.exists('sorted_numbers.txt'):
        open('sorted_numbers.txt', 'w').close()
    app.run(port=2461, debug=True)
