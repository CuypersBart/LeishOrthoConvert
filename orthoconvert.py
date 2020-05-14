import argparse
import os

parser = argparse.ArgumentParser(description="This tools converts Leishmania donovani LdBPKv2 gene IDs to\
    Leishmania major IDs using an orthology mapped database",
    epilog="For all questions, problems and suggestions please contact the author Bart Cuypers at\
    bart.cuypers@uantwerpen.be")
parser.add_argument('LdBPK_IDs', metavar = 'LdBPK_IDs', type = str,
                    help = 'input gene list')
parser.add_argument('-excludeNA', dest='NA', action='store_false', help = 'exclude genes in output without any ortholog')
parser.add_argument('-O', dest='O', action='store_true', help = 'only output result gene (not input gene)')
parser.set_defaults(NA=True, O=False)

args = parser.parse_args()
orthologs = {}
print(args)

SCRIPTPATH = os.path.dirname(os.path.realpath(__file__))

with open(SCRIPTPATH + '/Orthogroups.tsv') as myfile:
    myfile.readline()
    for i in myfile:
        i = i.strip('\n').split('\t')
        Ldo = i[1].replace('.1', '').split(', ')
        Lmaj = i[4].split(', ')
        if '' not in [Lmaj[0], Ldo[0]]:
            for ortho in Ldo:
                orthologs[ortho] = Lmaj[0].replace('.1_mRNA-p1', '').replace('_mRNA-p1', '').replace('_mRNA_1-p1', '').replace(
                    '_pseudogenic_transcript-p1', '')

with open(args.LdBPK_IDs) as myfile:
    for i in myfile:
        i = i.strip('\r\n')
        if args.O == False:
            if i in orthologs:
                print("\t".join([i, orthologs[i]]))
            elif args.NA == True:
                print("\t".join([i, "NA"]))
        else:
            if i in orthologs:
                print("\t".join([orthologs[i]]))
            elif args.NA == True:
                print("\t".join(["NA"]))