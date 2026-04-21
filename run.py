from backend.app import create_app

app = create_app()

if __name__ == '__main__':
    print("Starting Malware Analysis Sandbox...")
    print("Frontend and Backend are running together.")
    print("Access the application at: http://192.168.171.128:5000")

    # host='0.0.0.0' allows Windows browser to connect to Kali
    app.run(host='0.0.0.0', debug=True, port=5000)
