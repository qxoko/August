import codecs
import os
import re

from .utils import queue_file_write
from .utils import write_files

def expand_manifest(manifest_path, combined_document_path):
	print("august: combining manifest in '%s'" % manifest_path)

	with codecs.open(manifest_path, "r", "utf-8") as f:
		manifest = f.read()

	# All referenced files in the manifest are relative to this base path.
	base_path = os.path.dirname(manifest_path)

	referenced_file_names = (re.compile("\[\[\s*include:\s+(\S.*?)\s*\]\]").findall(manifest))

	for file_name in referenced_file_names:

		file_name = file_name.strip()
		file_path = os.path.join(base_path, file_name)

		if os.path.exists(file_path):

			with codecs.open(file_path, "r", "utf-8") as f:
				referenced_file = f.read()

			manifest = re.sub(
				"\[\[\s*include:\s*?%s\s*\]\]" % re.escape(file_name),
				"".join([
					"[[reference: %s]]" % file_name,
					"\n" if referenced_file.startswith("\n") else "\n\n",
					referenced_file,
					"\n" if referenced_file.endswith("\n") else "\n\n",
					"[[/reference]]"
				]),
				manifest)

	return queue_file_write(list(), combined_document_path, manifest)

def join_wrapper(manifest_path, combined_document_path):
	write_files(expand_manifest(manifest_path, combined_document_path))