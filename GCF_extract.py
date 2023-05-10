def extract(file_paths, output_path):
    with open(output_path, 'w') as output_file:
        for file_path in file_paths:
            with open(file_path, 'r') as file:
                data = file.readlines()

            header = ""
            sequence = ""
            for line in data:
                if line[0] == '>':
                    if header:
                        output_file.write(header + '\n' + sequence + '\n')
                    header = line.rstrip()
                    sequence = ""
                else:
                    sequence += line.rstrip()
            output_file.write(header + '\n' + sequence + '\n\n')

extract([
"GCF_000007045.1_ASM704v1_genomic.fna", "GCF_000018985.1_ASM1898v1_genomic.fna", "GCF_000019005.1_ASM1900v1_genomic.fna", "GCF_000019265.1_ASM1926v1_genomic.fna", "GCF_000019825.1_ASM1982v1_genomic.fna", "GCF_000026665.1_ASM2666v1_genomic.fna", "GCF_000146975.1_ASM14697v1_genomic.fna", "GCF_000147095.1_ASM14709v1_genomic.fna", "GCF_000180515.1_ASM18051v2_genomic.fna", "GCF_000196595.1_ASM19659v1_genomic.fna", "GCF_000210935.1_ASM21093v1_genomic.fna", "GCF_000210955.1_ASM21095v1_genomic.fna", "GCF_000210975.1_ASM21097v1_genomic.fna", "GCF_000210995.1_ASM21099v1_genomic.fna", "GCF_000211015.1_ASM21101v1_genomic.fna", "GCF_000211035.1_ASM21103v2_genomic.fna", "GCF_000211055.1_ASM21105v2_genomic.fna", "GCF_000211075.1_ASM21107v1_genomic.fna", "GCF_000251085.2_ASM25108v2_genomic.fna", "GCF_000299015.1_ASM29901v1_genomic.fna", "GCF_000817005.1_ASM81700v1_genomic.fna", "GCF_001255215.1_S_pneumo_A66_v1_genomic.fna", "GCF_001457635.1_NCTC7465_genomic.fna", "GCF_001896045.1_ASM189604v1_genomic.fna", "GCF_001896065.1_ASM189606v1_genomic.fna", "GCF_001896085.1_ASM189608v1_genomic.fna", "GCF_002357995.1_ASM235799v1_genomic.fna", "GCF_002813535.1_ASM281353v1_genomic.fna", "GCF_002813955.1_ASM281395v1_genomic.fna", "GCF_002843545.1_ASM284354v1_genomic.fna", "GCF_002947575.1_ASM294757v1_genomic.fna", "GCF_003003495.1_ASM300349v1_genomic.fna", "GCF_003354825.1_ASM335482v1_genomic.fna", "GCF_003609935.1_ASM360993v1_genomic.fna", "GCF_003966485.1_ASM396648v1_genomic.fna", "GCF_003966505.1_ASM396650v1_genomic.fna", "GCF_003966525.1_ASM396652v1_genomic.fna", "GCF_003967155.2_ASM396715v2_genomic.fna", "GCF_003994915.1_ASM399491v1_genomic.fna", "GCF_004291255.1_ASM429125v1_genomic.fna", "GCF_004331935.1_ASM433193v1_genomic.fna", "GCF_008253725.1_ASM825372v1_genomic.fna", "GCF_009664475.1_ASM966447v1_genomic.fna", "GCF_011694695.1_ASM1169469v1_genomic.fna", "GCF_013047165.1_ASM1304716v1_genomic.fna", "GCF_015838875.1_ASM1583887v1_genomic.fna", "GCF_015839035.1_ASM1583903v1_genomic.fna", "GCF_015839415.1_ASM1583941v1_genomic.fna", "GCF_015839575.1_ASM1583957v1_genomic.fna", "GCF_015839775.1_ASM1583977v1_genomic.fna", "GCF_015839915.1_ASM1583991v1_genomic.fna", "GCF_015840115.1_ASM1584011v1_genomic.fna", "GCF_017569245.1_ASM1756924v1_genomic.fna", "GCF_019454385.1_ASM1945438v1_genomic.fna", "GCF_019456615.1_ASM1945661v1_genomic.fna", "GCF_019915285.1_ASM1991528v1_genomic.fna", "GCF_020008085.1_ASM2000808v1_genomic.fna", "GCF_020097335.1_ASM2009733v1_genomic.fna", "GCF_021398235.1_ASM2139823v1_genomic.fna", "GCF_021398265.1_ASM2139826v1_genomic.fna", "GCF_021398285.1_ASM2139828v1_genomic.fna", "GCF_022068225.1_ASM2206822v1_genomic.fna", "GCF_022068245.1_ASM2206824v1_genomic.fna", "GCF_022068265.1_ASM2206826v1_genomic.fna", "GCF_022068285.1_ASM2206828v1_genomic.fna", "GCF_022068525.1_ASM2206852v1_genomic.fna", "GCF_022068645.1_ASM2206864v1_genomic.fna", "GCF_022068765.1_ASM2206876v1_genomic.fna", "GCF_022068885.1_ASM2206888v1_genomic.fna", "GCF_022069005.1_ASM2206900v1_genomic.fna", "GCF_022069085.1_ASM2206908v1_genomic.fna", "GCF_022069205.1_ASM2206920v1_genomic.fna", "GCF_022069325.1_ASM2206932v1_genomic.fna", "GCF_022069445.1_ASM2206944v1_genomic.fna", "GCF_022069505.1_ASM2206950v1_genomic.fna", "GCF_022069545.1_ASM2206954v1_genomic.fna", "GCF_022069645.1_ASM2206964v1_genomic.fna", "GCF_022069785.1_ASM2206978v1_genomic.fna", "GCF_022070005.1_ASM2207000v1_genomic.fna", "GCF_022070225.1_ASM2207022v1_genomic.fna", "GCF_022070425.1_ASM2207042v1_genomic.fna", "GCF_022070465.1_ASM2207046v1_genomic.fna", "GCF_022070485.1_ASM2207048v1_genomic.fna", "GCF_022070545.1_ASM2207054v1_genomic.fna", "GCF_022070565.1_ASM2207056v1_genomic.fna", "GCF_022075645.1_ASM2207564v1_genomic.fna", "GCF_022075745.1_ASM2207574v1_genomic.fna", "GCF_022318385.1_ASM2231838v1_genomic.fna", "GCF_022318405.1_ASM2231840v1_genomic.fna", "GCF_022318425.1_ASM2231842v1_genomic.fna", "GCF_022318445.1_ASM2231844v1_genomic.fna", "GCF_022318465.1_ASM2231846v1_genomic.fna", "GCF_022318485.1_ASM2231848v1_genomic.fna", "GCF_022318505.1_ASM2231850v1_genomic.fna", "GCF_022318525.1_ASM2231852v1_genomic.fna", "GCF_022318545.1_ASM2231854v1_genomic.fna", "GCF_022558605.1_ASM2255860v1_genomic.fna", "GCF_900475305.1_43721_E02_genomic.fna", "GCF_900475515.1_42731_F01_genomic.fna", "GCF_900636585.1_43058_B01_genomic.fna", "GCF_900692935.1_18090_1_84-2_genomic.fna", "GCF_900693025.1_19341_2_86-2_genomic.fna", "GCF_900693055.1_19084_8_150-2_genomic.fna", "GCF_900795205.1_22841_2_22-5_genomic.fna", "GCF_930986525.1_RMV7_genomic.fna"
], "output.fasta")
