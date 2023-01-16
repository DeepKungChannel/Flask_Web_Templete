import website


if __name__ == '__main__':
    app = website.create_app()
    app.run("localhost", port="8080", debug=True)