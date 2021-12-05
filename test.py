import argparse
import json

# parse arguments
def add_args(parser):
    parser.add_argument('--ground_truth_path', default='assignment_1_data/output.json', type=str, help='Path to ground truth output file')
    parser.add_argument('--solution_path', default='assignment_1_data/prediction.json', type=str, help='Path to solution file')
    parser.add_argument('--debug', action='store_true', help='print the wrong predictions with input and gold output')
    return parser

# calculated f-measure using prediction and ground truth
def calculateF1(args):
    # read the output and prediction files
    with open(args.solution_path, 'r', encoding="utf-8") as f:
        pred = json.load(f)
        f.close()
    with open(args.ground_truth_path, 'r', encoding="utf-8") as f:
        grnd = json.load(f)
        f.close()
    assert len(pred) == len(grnd)

    # for debugger
    with open('assignment_1_data/input.json', 'r', encoding="utf-8") as f:
        inp = json.load(f)
        f.close()
    assert len(inp) == len(grnd)

    if args.debug:
        wrong_count, total_count = 0, 0

    # calculate the precision, recall, and then f1 score
    prec_num, prec_den, rec_num, rec_den = 0.0, 0.0, 0.0, 0.0
    for idx, (x, y_, y) in enumerate(zip(inp, pred, grnd)):
        assert y_['sid'] == y['sid'] == x['sid']

        debug_flag = False 

        for inp_tok, pred_tok, true_tok in zip(x['input_tokens'], y_['output_tokens'], y['output_tokens']):
            # case 1, 3, 5
            if true_tok != "sil" and true_tok != "<self>":
                if pred_tok == true_tok:
                    prec_num += 1.0
                    prec_den += 1.0
                    rec_num += 1.0
                    rec_den += 1.0
                elif pred_tok == "sil" or pred_tok == "<self>":
                    rec_den += 1.0
                    if args.debug:
                        wrong_count += 1
                        print("INPUT: %s\nOutput: %s\nPredicted: %s\nSID: %u\n"%(inp_tok, true_tok, pred_tok, x['sid']))
                else:
                    prec_den += 1.0
                    rec_den += 1.0
                    if args.debug:
                        wrong_count += 1
                        print("INPUT: %s\nOutput: %s\nPredicted: %s\nSID: %u\n"%(inp_tok, true_tok, pred_tok, x['sid']))

            # case 4
            elif true_tok=="sil" or true_tok=="<self>":
                if pred_tok != true_tok:
                    prec_den += 1.0
                    if args.debug:
                        wrong_count += 1
                        print("INPUT: %s\nOutput: %s\nPredicted: %s\nSID: %u\n"%(inp_tok, true_tok, pred_tok, x['sid']))
            
            # case 2 doesn't affect
            if args.debug:
                total_count += 1
        
    precision = prec_num / prec_den if prec_den != 0.0 else 0.0
    recall = rec_num / rec_den if rec_den != 0.0 else 0.0

    f1 = (2 * precision * recall) / (precision + recall) if (precision + recall != 0.0) else 0.0
    
    print("number of sentences:", len(pred))
    print("precision:", round(100*precision,1), " recall:", round(100*recall,1), "f1:", round(100*f1,1))
    if args.debug:
        print("%u wrong tokens out of total %u tokens"%(wrong_count, total_count))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='COL 772 Assignment 1 | 2018EE10957')
    parser = add_args(parser)
    args = parser.parse_args()

    calculateF1(args)
