import codecs
import os

def queue_file_write(queue, file_path, file_contents):
	queue.append({"path": file_path, "contents": file_contents})
	return queue

def write_files(file_queue):
	for file_details in file_queue:
		full_file_path = file_details["path"]
		file_contents = file_details["contents"]

		# construct folder structure
		dir_path = os.path.dirname(full_file_path)
		if not os.path.exists(dir_path):
			os.makedirs(dir_path)

		# write files
		with codecs.open(full_file_path, "w", "utf-8") as f:
			f.write(file_contents)
			print("august: wrote '%s'" % full_file_path)