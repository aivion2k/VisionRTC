# VisionRTC - All-in-One Tool for Computer Vision

VisionRTC is an advanced server-side inference tool designed for testing and implementing computer vision solutions effortlessly. This platform allows you to implement and test computer vision methods and models on the server side, eliminating the need for any client-side implementation.

## Features

### Easy Implementation
VisionRTC simplifies the process of implementing and testing computer vision methods and models. With minimal setup, you can quickly get your solutions up and running.

### Simple Configuration
Configure VisionRTC easily through a user-friendly web interface. Full configuration via JSON is supported, offering flexibility and control over your setup.

### Dataset Management
Save datasets with or without labels returned by various methods. This feature helps streamline your data processing workflow and ensures efficient management of your datasets.

### Versatile Camera Source Integration
Use any device connected to the same network as a camera source. Whether it's a phone, PC, or any other device with a browser, VisionRTC supports seamless integration. GStreamer support will be added soon for enhanced functionality.

### Asynchronous Processing
VisionRTC supports multiple connections and methods simultaneously, providing asynchronous processing capabilities. This ensures efficient handling of multiple tasks without compromising performance.

## Getting Started

### Prerequisites

To use VisionRTC, you need to generate OpenSSL keys and paste them into certs folder. Follow the command below to generate the required keys:

```sh
openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365 -nodes
```

### Running VisionRTC

After generating the keys, you can start VisionRTC by accessing the following link on your loopback client:

```
https://127.0.0.1:8080/
```

or you can use different device and connect to:
```
https://your_server_ip_address:8080/
```

## Installation

1. Clone the repository:
```
git clone https://github.com/yourusername/VisionRTC.git
```
2. Navigate to the project directory:
```
cd VisionRTC
```
3. Install the necessary dependencies:
```
pip install -r requirements.txt
```
4. Run the application:
```
python main.py
```


## Configuration
Access the web interface via your browser to configure VisionRTC. Navigate to **https://127.0.0.1:8080/** and use the UI to choose the camera source, resolution and desired method.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.

## Contact
For any inquiries or support, please contact me via Linkedin
