# Oracle Internship Technical Challenge

## How to build the Docker image from the Dockerfile

* Clone this repository a folder, e.g.

    `git clone ~/Desktop/https://github.com/bokwoon95/oraclechallenge`

* Navigate into the cloned repository

    `cd ~/Desktop/oraclechallenge/`

* Build the Docker image

    `docker build -t oraclechallenge .`

* Run the Docker image (labeled 'oraclechallenge'). This command also maps the docker port 80 to your computer port 8000

    `docker run -p 8000:80 oraclechallenge`

You should see the below output:

    `* Running on http://0.0.0.0:80/ (Press CTRL+C to quit)`

Although it says `http://0.0.0.0:80/`, the actual address is `http://0.0.0.0:8000`. Port `80` is the docker container's published port, but the actual port on your computer that it is mapped to is `8000`.

* Open a web browser and goto this address

    `http://0.0.0.0:8000/fibonacci?element=10`

You should see an output like this:

![Alt Text](element10.png?raw=true "picture")

To change the number of elements, change the number `10` after `element=` into whatever number you want.
