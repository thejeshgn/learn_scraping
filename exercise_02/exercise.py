###############################################################################
# Thejesh <i@thejeshgn.com>, GNU/GPL v3
###############################################################################
# Exercise: Given a url and table_id, get the content of table as CSV
#
# Hint: Use python `requests` and `BeautifulSoup` libraries.
# `requests` is a python library used to get html content.
# `BeautifulSoup` is a python library used to parse html content.
#
# Implement get_table_and_save function below.
###############################################################################


# TODO Import requests and BeautifulSoup

# This function should return the title of the url
def get_table_and_save(url, table_id, csv_name):
    # TODO Get the content of the web page using requests

    # TODO Parse the content using BeautifulSoup html parser

    # TODO Extract the table using either using table id 

    # TODO Convert to CSV

    # TODO Save as CSV
    return True


def main():
    """Runs the program. And try it"""
    url = ""
    table_id = ""
    csv_name = ""

    get_table_and_save(url, table_id, csv_name)


if __name__ == "__main__":
    main()
