from argparse import ArgumentParser
import json

#added a counter for cells to keep columns more linked
def cell_separator(i):
    return "<C"+str(i)+">"

if __name__ == '__main__':

    parser = ArgumentParser()
    parser.add_argument("-f", "--file", help="The SciGen json file to be converted for pretrained models' input format", required=True)
    parser.add_argument("-s", "--split", help="Specify the corresponding split, i.e., train, dev, or test", required=True)


    args = parser.parse_args()
    file = args.file
    out = args.split

    row_seperator = '<R>'
    caption_separator = '<CAP>'

    with open(file, 'r', encoding='utf-8') as f:
        with open('{}.source'.format(out), 'w', encoding='utf-8') as source:
            with open('{}.target'.format(out), 'w', encoding='utf-8') as target:
                data = json.load(f)
                for d in data:
                    cell_counter = 0
                    text = row_seperator + ' ' + cell_separator(cell_counter)
                    cell_counter+=1
                    row_len = len(data[d]['table_column_names'])
                    for i,c in enumerate(data[d]['table_column_names']):
                        text += ' ' + c
                        if i < row_len-1: 
                            text += ' ' + cell_separator(cell_counter)
                            cell_counter+=1

                    for row in data[d]['table_content_values']:
                        cell_counter = 0
                        text += ' ' + row_seperator + ' ' + cell_separator(cell_counter)
                        cell_counter+=1
                        for i, c in enumerate(row):
                            text += ' ' + c
                            if i < row_len -1:
                                text += ' ' + cell_separator(cell_counter)
                                cell_counter+=1

                    text += ' ' + caption_separator + ' ' +data[d]['table_caption'] + '\n'

                    source.write(text)
                    descp = data[d]['text'].replace('[CONTINUE]', '') + '\n'
                    target.write(descp)





