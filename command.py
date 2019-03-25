import sublime_plugin
import os
from . import scope

# @incomplete
def create_buffer(context):
	panel = context.view.window().new_file()
	panel.set_scratch(True)
	return panel

class AugustPrintCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		source_file = self.view.window().active_view()

		output_file = create_buffer(self)
		output_file.set_name('Scene List')

		# output_file.set_syntax_file('Packages/August/August.sublime-syntax')
		# output_file.set_read_only(True)

		title = 'SCENE LIST: '

		try:
			title += os.path.basename(source_file.file_name()).upper() + '\n'
		except AttributeError:
			title += 'UNSAVED FILE\n'

		output_file.insert(edit, output_file.size(), title)

		index = 1

		for region in source_file.find_by_selector(scope.scene):
			output_file.insert(edit, output_file.size(), "\n{}.\t{}".format(index, source_file.substr(region)).rstrip())
			index += 1


def get_reverse_scope_list(file, scope):
	region_list = file.find_by_selector(scope)
	region_list.reverse()
	return region_list, len(region_list)

def clear_scene_numbers(self, edit):
	import re
	source_file = self.view.window().active_view()
	region_list, count = get_reverse_scope_list(source_file, scope.scene_numbers)
	for region in region_list:
		new_text = re.sub(r' ?#.+#', '', source_file.substr(region))
		source_file.replace(edit, region, new_text)

class AugustRemoveSceneNumberCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		clear_scene_numbers(self, edit)

class AugustSceneNumberCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		clear_scene_numbers(self, edit)

		source_file = self.view.window().active_view()

		region_list, count = get_reverse_scope_list(source_file, scope.scene)

		for region in region_list:
			source_file.replace(edit, region, source_file.substr(region).rstrip() + " #{}#".format(str(count)))
			count -= 1


class AugustHideBoneyardCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		if self.view.fold(self.view.find_by_selector(scope.boneyard)):
			self.view.fold(self.view.find_by_selector(scope.boneyard))
		else:
			for region in self.view.find_by_selector(scope.boneyard):
				self.view.unfold(region)

class AugustMergeCommand(sublime_plugin.TextCommand):
	def null(self, name):
		pass

	def join(self, user_request):
		if user_request == '':
			self.view.set_status('August','[August] No filename provided for merge')
			return

		from .mountain.join import join_wrapper

		manifest_path = self.view.file_name()
		user_request  = os.path.expanduser(user_request)
		output_path	  = os.path.dirname(user_request)

		output = ''

		if output_path == '':
			output = os.path.dirname(manifest_path) + '/' + user_request
		else:
			output = user_request

		join_wrapper(manifest_path, output)

		self.view.window().open_file(output)

	def run(self, edit):
		if any(n in self.view.file_name() for n in ['fountain','ftn']):
			self.view.window().show_input_panel(' filename to write: ', '', self.join, self.null, self.null)

class AugustSplitCommand(sublime_plugin.TextCommand):
	def null(self, name):
		pass

	def split(self, user_request):
		if user_request == '':
			self.view.set_status('August','[August] No manifest provided for split')
			return

		from .mountain.split import split_wrapper

		screenplay_path = self.view.file_name()
		user_request    = os.path.expanduser(user_request)
		manifest_path   = os.path.dirname(user_request)

		output = ''

		if manifest_path == '':
			output = os.path.dirname(screenplay_path) + '/' + user_request
		else:
			output = user_request

		split_wrapper(output, screenplay_path)

	def run(self, edit):
		if any(n in self.view.file_name() for n in ['fountain','ftn']):
			self.view.window().show_input_panel(' manifest filename: ', '', self.split, self.null, self.null)