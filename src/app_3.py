"""
    Demonstrating extracting tables from pdf files
    and converting them into pandas dataframes so they can be used in data science processes
    Uses `tabula-py`

    However, issues with jpype were encountered --- requiring a JAVA_HOME environment variable, the process
    for some path, the process for which the tutorial didn't talk about, it doesnm't work, giving a certain kind of error.
"""

import tabula


#   pages argument can be 1 (default) or "all"
tables = tabula.read_pdf("./res/test.pdf", pages=1)
#   this prints a list of pandas dataframes; each dataframe represents a table
# print(tables)

#   assigns the first table dataframe to a variable
df = tables[0]
print(df)

#   an operation that can be performed depending on the data in the pdf
# print(df[df.Age > 30])