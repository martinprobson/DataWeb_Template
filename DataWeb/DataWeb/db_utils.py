#!/usr/bin/env python
"""
    initdb - Drop and re-create the database.
    Exposed to flask cli via @app.cli.command()
"""
from __future__ import print_function
import os.path
import imp
from config import LOAD_DUMMY_DATA
from datetime import datetime
from DataWeb import db, app, models

def setup_dummy_data():
    """ Add some dummy issues and a test userid for demo/testing """
    issues = [models.Issue(id='Issue 1',description='This is a description of issue 1',status='Active'),
              models.Issue(id='Issue 2',description='This is a description of issue 2',status='Active'),
              models.Issue(id='Issue 3',description='This is a description of issue 3, status is Open',status='Open'),
              models.Issue(id='Issue 10',description='This is a description of issue 10, status is Closed',status='Closed')]
    [db.session.add(i) for i in issues]
    test_user = models.User(id=999,username='test',password='$2b$12$ND0RIu5yKNbY32onSRNMaO.g2YYfWjGlbkRcT.kVA8YDZMJuy4M8a',
                            email='dummy',active=1,confirmed_at=datetime.utcnow())
    db.session.add(test_user)
    db.session.commit()

@app.cli.command('initdb')
def initdb_command():
    """ Initializes the database

    This command creates a new (or refreshes the existing) database
    schema and places it under SqlAlchemy version control.
    """
    db.drop_all()
    db.create_all()
    if LOAD_DUMMY_DATA:
        setup_dummy_data()

    print('Initialized the database.')

