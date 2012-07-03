#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""dbConverter

convert sqlite to wav """

import sqlite3

class Config:
    DB_PATH = "pressure"

def main():
    print 'test'
    conn = sqlite3.connect(Config.DB_PATH)
    result = conn.execute("SELECT * FROM user")
    print 'all user:'
    print result.fetchall()

    result = conn.execute("SELECT * FROM record")
    print 'all record:'
    print result.fetchall()

    result = conn.execute("SELECT * FROM data")
    print 'one row of data:'
    print result.fetchone()

if __name__ == '__main__':
    main()

