# -*- coding: UTF-8 -*-

import argparse

_parser = argparse.ArgumentParser(description="Run tests for OERPLib.")

_parser.add_argument('--server', default='localhost',
                     help="Host")
_parser.add_argument('--protocol', default='xmlrpc',
                     help="Protocol")
_parser.add_argument('--port', default='8069',
                     help="Port")

_parser.add_argument('--super_admin_passwd', default='admin',
                     help="Super administrator password")

_parser.add_argument('--database', default='oerplib-test',
                     help="Name of the database")

_parser.add_argument('--user', default='admin',
                     help="User login")
_parser.add_argument('--passwd', default='admin',
                     help="User password")

_parser.add_argument('--create_db', action='store_true',
                     help="Create a database for tests")
_parser.add_argument('--drop_db', action='store_true',
                     help="Drop the created database. "
                          "Works only with --create_db")

_parser.add_argument('--verbosity', default=2, type=int,
                     help="Output verbosity of unittest")

ARGS = _parser.parse_args()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
