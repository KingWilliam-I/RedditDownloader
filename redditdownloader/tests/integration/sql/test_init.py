from os.path import isfile, join
import static.settings as settings
import sql
from tests.mock import EnvironmentTest


class SqliteInitTest(EnvironmentTest):
	env = 'rmd_version_4'

	def setUp(self):
		settings.load(self.settings_file)

	def tearDown(self):
		sql.close()

	def test_init_db(self):
		""" The database should build """
		sql.init_from_settings()
		# self.assertTrue(isfile(join(settings.get("output.base_dir"), "manifest.sqlite")), "Failed to create sqlite file.")
		self.assertTrue(isfile(join(settings.get("output.manifest_for_sqlite_dir"), "manifest.sqlite")), "Failed to create sqlite file.")		# This is part of the change to save manifest.sqlite to a different directory than the downloads
