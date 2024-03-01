#!/bin/python
import sys, argparse, csv
from scipy import stats

def printit(res, problim, bit, pval):
    '''
    print a pass/fail result line as a CSV
    '''
    print(res, problim, bit, pval.k, pval.n, pval.statistic, pval.pvalue, sep=",")

def runtests(csvfile, problim):
    '''
    CSV format: bit, percent-zero, percent-one, count
    represents the numbers of zeroes and ones in each
    bit position for a TEK.
    We'll test for binomial test pass/fail for each 
    at a given probability, defaulting to 0.05.
    '''
    fails=[]
    print("pass/fail, problim, bit, zeros, total, percent, pvalue")
    with open(csvfile) as file:
        readCSV = csv.reader(file, delimiter=',')
        for row in readCSV:
            try:
                if row[0]=="Bit" or row[0]=="": # skip header or non-int
                    continue
                # print(row)
                bit=int(row[0])
                p_0=float(row[1])/100
                p_1=float(row[2])/100
                tot=int(row[3])
                if (not isinstance(bit, int) or bit < 0 or bit > 127):
                    print("Skipping row", row)
                    continue
                # process line
                pval=stats.binomtest(int(p_0*tot),tot)
                if (pval.pvalue < problim):
                    printit("fail", problim, bit, pval)
                    fails.append({bit, pval})
                else:
                    printit("pass", problim, bit, pval)

            except Exception as e:
                print(str(e),row)

    return len(fails)==0

if __name__ == "__main__":
    # command line arg handling 
    csvfile="bitcounts.csv"
    problim=0.05
    argparser=argparse.ArgumentParser(description='Do binomial tests on countbits.py output')
    argparser.add_argument('-i','--input',     
                        dest='csvfile',
                        help='file containing CSV output from countbits.py')
    argparser.add_argument('-p','--probability',     
                        dest='problim',
                        help='probability for pass/fail')
    args=argparser.parse_args()
    if args.csvfile is not None:
        csvfile=args.csvfile
    if args.problim is not None:
        problim=float(args.problim)

    res=runtests(csvfile, problim)
    if (res==True):
        print("pass")
    else:
        print("fail")
