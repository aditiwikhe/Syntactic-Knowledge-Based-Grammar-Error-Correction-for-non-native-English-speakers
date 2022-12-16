import errant
import json
import numpy as np
import argparse

# Create the parser and add arguments
parser = argparse.ArgumentParser()
parser.add_argument(dest='argument1', help="This is the first argument")
parser.add_argument(dest='argument2', help="A string argument")
parser.add_argument(dest='argument3', help="A string argument")
# Parse and print the results
args = parser.parse_args()

src_dict = {}
annotator = errant.load('en')

lang = args.argument2

f = open('lang_tags_prob.json')
data = json.load(f)
distribution = data[lang]
#print(distribution.keys())

f1 = open('lang_tags_mera_1_probs.json')
data1 = json.load(f1)
distribution1 = data1[lang]
#print(distribution1.keys())

dest_file = args.argument3
src_file = args.argument1
with open(dest_file, 'w') as the_file:
    with open(src_file) as file:
        for line in file:
            if line.startswith('S'):
                src_dict[int(float((line.split('\t')[0].split('-')[1])))] = {}
                src_dict[int(float((line.split('\t')[0].split('-')[1])))]['S'] = line.split('\t')[1][:-1]
                src_dict[int(float((line.split('\t')[0].split('-')[1])))]['H'] = []

            elif line.startswith('H'):
                src_dict[int(float((line.split('\t')[0].split('-')[1])))]['H'].append(line.split('\t')[2][:-1])

    for x in src_dict.keys():
        edits_tags = []
        orig = annotator.parse(src_dict[x]['S'])
        src_dict[x]['scores'] = []
        for z in src_dict[x]['H']:
            cor = annotator.parse(z)
            edits = annotator.annotate(orig, cor)
            score_indi = 0
            score_comb = 0
            if edits:
                list_edits_type = []
                for e in edits:
                    list_edits_type.append(e.type)
                    if e.type in distribution.keys():
                        score_indi = score_indi + distribution[e.type]

                score_indi = score_indi/len(edits)

                list_edits_type_set = set(list_edits_type)
                list_edits_type_set_sorted = sorted(list_edits_type_set)
                list_edits_type_set_sorted_str = '_'.join(list_edits_type_set_sorted)
                if list_edits_type_set_sorted_str in distribution1.keys():
                    score_comb = distribution1[list_edits_type_set_sorted_str]
            src_dict[x]['scores'].append(score_comb + score_indi)
        arr_scores = np.array(src_dict[x]['scores'])
        arg_idx = np.argmax(arr_scores)
        src_dict[x]['idx'] = arg_idx
        the_file.write(src_dict[x]['H'][arg_idx] + '\n')
        #print(np.argmax(arr_scores))

