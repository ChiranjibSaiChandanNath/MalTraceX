from backend.app import create_app

app = create_app()

if __name__ == '__main__':
    print("Starting Malware Analysis Sandbox...")
    print("Frontend and Backend are running together.")
    print("Access the application at: http://127.0.0.1:5000")


    app.run(host='127.0.0.1', debug=True, port=5000)

