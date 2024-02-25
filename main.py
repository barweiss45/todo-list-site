#! /usr/bin/env python3

"""Entrypoint for application"""

from app import create_app

app = create_app()  # Calls Factory Function

if __name__ == "__main__":
    app.run(debug=True)
