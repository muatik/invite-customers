
def file_line_stream(file_path):
    """
    reads the given file line by line and returns each line immediately.
    :param file_path:
    :return: generator of lines
    """
    with open(file_path, "r") as f:
        for i in f:
            yield i


