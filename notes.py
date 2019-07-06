import sublime
import sublime_plugin
import os
import re
import codecs
from . import scope

def create_note_buffer(context, edit):
	panel = context.view.window().new_file()
	panel.set_scratch(True)
	panel.set_name('Notes')
	panel.set_syntax_file('Packages/August/August.sublime-syntax')

	# panel.erase(edit, sublime.Region(0, panel.size()))

	return panel

def extract_info_from_files():
	referenced_file_names = (re.compile("\\[\\[\\s*include:\\s+(\\S.*?)\\s*\\]\\]").findall(manifest))

def write_to_buffer(file, edit, text):
	file.insert(edit, file.size(), text + '\n')

class AugustListNotesCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		# get origin buffer
		source_file      = self.view.window().active_view()

		# extract name information
		source_file_name = source_file.file_name()
		source_file_path = os.path.dirname (source_file_name)
		source_file_name = os.path.basename(source_file_name)

		# create destination buffer
		output_file = create_note_buffer(self, edit)
		output_file.set_syntax_file('Packages/August/August Note.sublime-syntax')

		first_note = True

		# handle the source file with scope selectors because we're lazy
		for region in source_file.find_by_selector(scope.note):
			region_text = source_file.substr(region).rstrip().replace('[[','').replace(']]','')

			if "include:" in region_text:
				first_note = False
				relative_path = region_text.replace('include:','').strip()
				absolute_path = os.path.join(source_file_path, relative_path)

				if os.path.exists(absolute_path):
					write_to_buffer(output_file, edit, '\n' + relative_path)

					with codecs.open(absolute_path, "r", "utf-8") as f:
						file_content = f.read()

					notes_list = (re.compile("\\[\\[(.+)\\]\\]").findall(file_content))

					for note in notes_list:
						write_to_buffer(output_file, edit, note)

					write_to_buffer(output_file, edit, '\n' + source_file_name)

			elif "reference:" in region_text:
				first_note = False
				header = '{} (inside {})'.format(region_text.replace('reference:','').strip(), source_file_name)

				write_to_buffer(output_file, edit, '\n' + header)

			elif "/reference" in region_text:
				first_note = False
				write_to_buffer(output_file, edit, '\n' + source_file_name)

			else:
				if first_note:
					write_to_buffer(output_file, edit, '\n' + source_file_name)
					first_note = False

				line_number = str(source_file.rowcol(region.end())[0] + 1).ljust(8,' ')

				write_to_buffer(output_file, edit, "L{} {}".format(line_number, region_text))