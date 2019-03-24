import codecs
import os
import re

from .utils import queue_file_write
from .utils import write_files

def split_combined_document(manifest_path, combined_document_path):
	print("august: reading combined document from '%s'." % combined_document_path)

	with codecs.open(combined_document_path, "r", "utf-8") as f:
		combined_document = f.read()

	base_path = os.path.dirname(manifest_path)

	references = re.findall(
		"\[\[reference:\s+(\S.*?)\]\](.*?)\[\[/reference\]\]",
		combined_document,
		re.DOTALL)

	manifest = combined_document

	write_queue = list()

	for file_name, file_contents in references:
		file_name = file_name.strip()
		file_path = os.path.join(base_path, file_name)
		file_contents = file_contents.strip()

		# Add the trailing newline that was just stripped away.
		file_contents = file_contents + "\n"

		queue_file_write(write_queue, file_path, file_contents)

		manifest = re.sub(
			"\[\[reference:\s+%s\]\].*?\[\[/reference\]\]" % re.escape(file_name),
			"[[include: %s]]" % file_name,
			manifest,
			0,
			re.DOTALL
		)

	return queue_file_write(write_queue, manifest_path, manifest)

def split_wrapper(manifest_path, combined_document_path):
	write_files(split_combined_document(manifest_path, combined_document_path))