from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def landing_page():
    return '''
    Hello! This is the landing page.
    '''

@app.route('/fibonacci', methods=['GET', 'POST'])
def fibonacci():
    # Get number of elements
    json_input = int(request.args.get('element'))

    # Corner case for 0 elements
    if (json_input == 0):
        fibonaccilist = []
        sortedlist = []

    # Corner case for 1 elements
    elif (json_input == 1):
        fibonaccilist = [0]
        sortedlist = [0]

    # Corner case for 2 elements
    elif (json_input == 2):
        fibonaccilist = [0, 1]
        sortedlist = [0, 1]

    else:
        fibonaccilist = [0, 1]
        # While the length of list has still not reach the required length,
        # Keep adding a new fibonacci element by summing the previous 2 elements
        while (len(fibonaccilist) < json_input):
            last_element = fibonaccilist[-1] + fibonaccilist[-2]
            fibonaccilist.append(last_element)
            # If fibonacci list has the required no. elements, break out of loop
            if (len(fibonaccilist) == json_input):
                continue

    # Since fibonacci is already sorted in ascending order,
    # Reverse the list to get the descending sorted list
    if json_input % 2 == 1:
        sortedlist = list(reversed(fibonaccilist))
    # If number of elements is even, all even numbers come first (sorted in descending order)
    # Split the list into 2 lists of even and odd each, reverse and typecast back to list
    # Then concatenate the odd list to the even list
    else:
        even_list = list(reversed([i for i in fibonaccilist if i % 2 == 0]))
        odd_list = list(reversed([i for i in fibonaccilist if i % 2 == 1]))
        sortedlist = even_list + odd_list

    # Create a dict to store the results
    dict_result = {
            "fibonacci": fibonaccilist,
            "sorted": sortedlist,
            }

    # Convert the dict into a json object and return
    return jsonify(dict_result)

if __name__ == '__main__' :
    app.run(host='0.0.0.0', port=80)
