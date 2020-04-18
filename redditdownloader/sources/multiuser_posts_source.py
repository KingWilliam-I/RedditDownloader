from sources import source
import static.praw_wrapper as reddit
from static.settings import Setting

# copied and altered from user_posts_source.py
# TODO: change from getting posts from one user to the intended multiuser

# Is there another file that deals with the types entered into the sourde fields?
class MultiuserPostsSource(source.Source):
	def __init__(self):
		super().__init__(source_type='multiuser-posts-source', description="Multiple Users' Submission and/or Comment histories.")

	def get_elements(self):
            for user in self.data['users'].split(','):
                for re in reddit.user_posts(
                        username=self.data['users'],
                        find_submissions=self.data['scan_submissions'],
                        find_comments=self.data['scan_comments']):
                    if self.check_filters(re):
                        yield re






	def get_settings(self):
		yield Setting('users', '', etype='str', desc='Target usernames:')
		yield Setting('scan_comments', False, etype='bool', desc='Scan their comments?')
		yield Setting('scan_submissions', False, etype='bool', desc='Scan their submissions?')

	def get_config_summary(self):
		feeds = ""
		if self.data['scan_comments']:
			feeds += "Comments"
		if self.data['scan_submissions']:
			if len(feeds) > 0:
				feeds += " & "
			feeds += "Submissions"
		return "Scanning User (%s)'s %s." % (self.data['user'], feeds)
