###############################################################################
# Thejesh <i@thejeshgn.com>, GNU/GPL v3
###############################################################################
# Exercise: Given a url and table_id, save the content of table as CSV
#   Example 1:
#    URL = https://thejeshgn.github.io/learn_scraping/table1.html
#    Table = Example Table 
#   Example 2:
#    URL = https://thejeshgn.github.io/learn_scraping/table1.html
#    Table = Districts of India 
#
# Hint: Use python `requests` and `BeautifulSoup` libraries.
#  `requests` is a python library used to get html content.
#  `BeautifulSoup` is a python library used to parse html content.
#  Try https://docs.python.org/3/library/csv.html#csv.writer for CSV writing
#
# Implement get_table_and_save function below.
###############################################################################
# TODO Import requests and BeautifulSoup

# This function should True if everything is okay
def get_table_and_save(url, table_id, csv_file_path):
    # TODO Get the content of the web page using requests

    # TODO Parse the content using BeautifulSoup html parser

    # TODO Extract the table using table_id 

    # TODO Convert to CSV

    # TODO Save CSV as .csv file at given csv_file_path

    return True


def main():
    """Runs the program. And try it"""
    url = ""
    table_id = ""
    csv_name = ""

    get_table_and_save(url, table_id, csv_name)


if __name__ == "__main__":
    main()
