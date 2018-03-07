from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/fibonacci')
def fibonacci():
    json_input = int(request.args.get('element'))

    if (json_input == 1):
        fibonaccilist = [0]
        sortedlist = [0]

    elif (json_input == 2):
        fibonaccilist = [0, 1]
        sortedlist = [0, 1]

    else:
        fibonaccilist = [0, 1]
        while (len(fibonaccilist) < json_input):
            last_element = fibonaccilist[-1] + fibonaccilist[-2]
            fibonaccilist.append(last_element)
            if (len(fibonaccilist) == json_input):
                continue

    if json_input % 2 == 0:
        even_list = [i for i in fibonaccilist if i % 2 == 0]
        odd_list = [i for i in fibonaccilist if i % 2 == 1]
        sortedlist = list(reversed(odd_list + even_list))
    else:
        sortedlist = list(reversed(fibonaccilist))

    dict_result = {
            "fibonacci": fibonaccilist,
            "sorted": sortedlist,
            }
    return jsonify(dict_result)

if __name__ == '__main__' :
    app.run(debug=True, port=8000)
