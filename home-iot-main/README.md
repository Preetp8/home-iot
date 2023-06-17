# Home IoT
This is a simple IoT project that enables you to monitor and control various smart home devices using a web interface. This project consists of a Node.js server that handles device communication and a Flask-based web interface that lets you interact with the devices.



## Installation

To install and run this project, follow these steps:

1. Clone the repository from GitHub:
```
git clone https://github.com/your-username/home-iot.git
```

2. Navigate into the home-iot directory:
```
cd home-iot
```
3. Install the dependencies for the Node.js server:
```
cd home-iot-node-server
npm install
cd ..
```
4. Ensure that Python and pip are installed on your system. If they are not installed, you can download and install Python from the official website (https://www.python.org/downloads/). Once Python is installed, you can install pip by following the instructions at (https://pip.pypa.io/en/stable/installation/).

5. Install Flask by running the following command:
```
pip install flask
```
6. Run the Node.js server in one terminal window:
```
node home-iot-node-server/app.js
```
7. Run the Flask-based web interface in another terminal window:
```
python main.py
```

## Usage
Once the server and web interface are running, you can access the interface by opening a web browser and navigating to http://localhost:5000. From there, you can view the status of your smart home devices and control them as needed.


