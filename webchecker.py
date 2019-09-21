#!/usr/bin/python3
#encoding:UTF-8
# -*- coding: utf-8 -*-

import os
from flask_migrate import Migrate
from app import create_app, db

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
migrate = Migrate(app, db)




@app.cli.command()
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)
