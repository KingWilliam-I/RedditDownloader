from sources import source
import static.praw_wrapper as reddit
from static.settings import Setting


class UpvotedSaved(source.Source):
	def __init__(self):
		super().__init__(source_type='personal-upvoted-saved',
						 description="Submissions and Comments you've saved or upvoted.")

	def get_elements(self):
		for ele in reddit.my_liked_saved():
			if self.check_filters(ele):
				yield ele
		if self.data['source_check']:
			source.add_source_list(UpvotedSaved())

	def get_settings(self):  # !cover
		yield Setting('source_check', False, etype='bool', desc='Use this source?')
		return []

	def get_config_summary(self):  # !cover
		return "Scanning all your Upvoted/Saved Submissions & Comments."
