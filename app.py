finalLen = []

pair1 = input('What is the genotype of the first parent?: ')

pair2 = input('What is the genotype of the second parent?: ')
print('\n')

pheno1D = str.casefold(input('What is the dominant trait of the first parent?: '))
pheno1R = str.casefold(input('What is the reccesive trait of the first parent?: '))
print('\n')

geneP = (pair1 + pair2)

finalGene = list((geneP[0] + geneP[2], geneP[0] + geneP[1], geneP[1] + geneP[3], geneP[1] + geneP[3]))

phenoGene = list((geneP[0], geneP[2], geneP[0], geneP[1], geneP[1], geneP[3], geneP[1], geneP[3]))

if str(phenoGene[0]).isupper() == True:
  finalLen.append('a')

if str(phenoGene[2]).isupper() == True:
  finalLen.append('a')

if str(phenoGene[4]).isupper() == True:
  finalLen.append('a')

if str(phenoGene[6]).isupper() == True:
  finalLen.append('a')

len1 = len(finalLen)
precentD = (len1/4)*100
precentR = 100-precentD

print('The possible genotypes for the trait are: \n') 
print(*finalGene, sep = ' ')
print('\n')

print('The offspring is', precentD, '% to have', pheno1D)
print('The offspring is', precentR, '% to have', pheno1R)
