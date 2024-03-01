#!/usr/bin/env python3

def parse_periodic_table(file):
    periodic_table = []
    f = open(file, 'r')
    lines = f.readlines()
    f.close()
    for line in lines:
        line = line.strip()
        tmp = line.split('=')
        elements = tmp[1].split(',')
        elementDict = {element.strip().split(':')[0]: element.strip().split(':')[1] for element in elements}
        elementDict['name'] = tmp[0].strip()
        periodic_table.append(elementDict)
    return periodic_table

# present this in file.html
def write_html_table(file, arr):
    f = open(file, 'w')
    html = """<!DOCTYPE html>
        <html lang="en">
        <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>periodic table</title>
        <style>
            table{{
            border-collapse: collapse;
            }}
            h4 {{
            text-align: center;
            }}
            ul {{
            list-style:none;
            padding-left:0px;
            }}
        </style>
        </head>
        <body>
        <table >
            {body}
        </table>
        </body>
        </html>
    """
    container = """
        <td style="border: 1px solid black; padding:10px">
            <h4>{name}</h4>
            <ul>
                <li>{numer}</li>
                <li>{small}</li>
                <li>{molar}</li>
                <li>{electron} electron </li>
            </ul>
        </td>
    """
    pos = 0
    body = '<tr>'
    for element in arr:
        if pos > int(element['position']):
            body += '<tr/> <tr">'
            pos = 0
        for i in range(pos, int(element['position'])):
            body += '<td style="border: none;"></td>'
            pos += 1
        body += container.format(name=element['name'], numer=element['number'], small=element['small'], molar=element['molar'], electron=element['electron'])
        pos += 1
    body += '</tr>'
    f.write(html.format(body=body))
    f.close()

def main():
    file = 'periodic_table.txt'
    arr = parse_periodic_table(file)
    write_html_table('file.html', arr)

if __name__ == '__main__':
    main()