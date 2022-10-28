import os
import re

from Utils.StringBuilder import StringBuilder


def generate_file(path, datasource_filename, filename_export, database_use_name, row_list, template, separator,
                  script_title="",
                  initial_script=""):
    builder = StringBuilder()
    builder.append_line('--' + script_title)
    builder.append_line(database_use_name)
    builder.append_line(initial_script)

    if not os.path.exists(path):
        os.mkdir(path)

    rows = get_data_from_file(os.path.join(path, datasource_filename))

    for i, row in enumerate(rows):
        if not row or re.search("^\s*$", row):
            continue

        data = row.split(separator)
        temp_string = template
        sb = StringBuilder(temp_string)

        for j, item in enumerate(row_list):
            sb.replace(item, data[j]
                       .strip().replace('\r\n', '').replace('\n', '')
                       .replace('\r', '').replace("\'", "\'\'"))

        sb.replace("#number#", str(i + 1))
        builder.append(sb.to_string())

    write_to_file(os.path.join(path, filename_export), builder.to_string())


def get_data_from_file(filepath):
    with open(filepath, encoding="utf-8") as f:
        return f.readlines()


def write_to_file(pathname, text):
    with open(pathname + '.txt', 'w', encoding='utf-8') as f:
        f.write(text)
