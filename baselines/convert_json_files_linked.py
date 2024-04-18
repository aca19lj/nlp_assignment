from argparse import ArgumentParser
import json


if __name__ == '__main__':

    parser = ArgumentParser()
    parser.add_argument("-f", "--file", help="The SciGen json file to be converted for pretrained models' input format", required=True)
    parser.add_argument("-s", "--split", help="Specify the corresponding split, i.e., train, dev, or test", required=True)


    args = parser.parse_args()
    file = args.file
    out = args.split

    with_seperator = '<WITH>'
    owns_seperator = '<HAS>'
    cell_separator = '<C>'
    row_seperator = '<R>'
    caption_separator = '<CAP>'

    with open(file, 'r', encoding='utf-8') as f:
        with open('{}.source'.format(out), 'w', encoding='utf-8') as source:
            with open('{}.target'.format(out), 'w', encoding='utf-8') as target:
                data = json.load(f)
                for d in data:
                    column_name_list =[]
                    text = ''
                    #set up column name list
                    row_len = len(data[d]['table_column_names'])
                    for i,c in enumerate(data[d]['table_column_names']):
                        column_name_list.append(c)

                    for row in data[d]['table_content_values']:
                        count = 1
                        text += ' ' + row_seperator + ' ' + cell_separator
                        for i, c in enumerate(row[1::]):
                            text += ' ' + column_name_list[count] + ' ' + with_seperator +' ' + row[0]+ ' '+ owns_seperator+ ' '+c
                            count +=1
                            if i < row_len -1:
                                text += ' ' + cell_separator

                    text += ' ' + caption_separator + ' ' +data[d]['table_caption'] + '\n'

                    source.write(text)
                    print(text)
                    descp = data[d]['text'].replace('[CONTINUE]', '') + '\n'
                    target.write(descp)





