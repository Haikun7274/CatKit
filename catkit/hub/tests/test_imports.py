
import os
import sys
import unittest
import tempfile
import pprint
import sqlite3
import json
import click
from click.testing import CliRunner

import cathub


class CommandLineTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def test_imports(self):
        import catkit.hub
        import catkit.hub.cathubsqlite
        import catkit.hub.postgresql
        import catkit.hub.folderreader
        import catkit.hub.tools
        import catkit.hub.ase_tools
        import catkit.hub.folder2db
        import catkit.hub.db2server
        import catkit.hub.make_folders_template
        import catkit.hub.psql_server_connect
        import catkit.hub.organize

    def test_cli(self):
        runner = CliRunner()
        
        from catkit.hub import reactions, publications        
        runner.invoke(reactions)
        runner.invoke(publications)

        from cathub import make_folders
        runner.invoke(make_folders, ['--create-template', 'template'])
        runner.invoke(make_folders, ['template'])

                      
if __name__ == '__main__':
    unittest.main()
        
