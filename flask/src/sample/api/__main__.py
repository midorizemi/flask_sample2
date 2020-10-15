#!/usr/bin/env python3

# import connexion


def run():
    from api.application import app
    app.run()


if __name__ == '__main__':
    run()
