from src import create_app

app = create_app()

if __name__ == '__main__':
    # Run the Flask app on localhost, port 5000 with debug enabled
    app.run(debug=True, host='127.0.0.1', port=5000)
