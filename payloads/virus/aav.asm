; payload
;  exec: ssDNA
;  type: virus
;  desc:
;   Adeno-associated virus, infects humans but doesn't cause any disease.
;   Is a perfect for carrying payloads (e.g. vector vaccine)
;  related:

; this is the Adeno-associated virus
; taken from https://www.ncbi.nlm.nih.gov/nuccore/KX583629.1

; the first thing we have is a repeating region
bases gtcatactttctcacaataagcttgtcctcctccccccaataacacgctcgctcgctcgctcgggacaaccgggcgaagcccggttgcaagcgcccttcgggcgcttgtcccgagcgagcgagcgagcgtgttattggggggaggaggacaagcttattgtgagaaagtatga

; padding
bases ccaaagtacgtaggccagataccgtaggggttacacaaccaggttgtaacacttgggtgtctgggttcgatttccagtctggccgtgtagggagggcgtgattcttcatcaaagtggtgggtggagaatctgacccttcttttttctcgcgagactttgcgagatttccaaatatcgcgagaccttaacagtataaagtgagcgcgagcgagcgaccgcgccagacgccatcacgccgttgatccctacacaccaag

; this is the reproduction protein
bases atgacgacacctacgtactacgagctgattgtggagctgccgagcgacattgacactcaactccccctggtcagcgacagctttgtgcgatgggtgacgagcaagacgtgggaaccccccctggacagcaaatgggacatggaccaagtggaccaagtccagctgactctcggagacaagattcaacgggaaattttaaaacagtggaggaccattaccggagaccctgatccgaaatattacgtccagctggagcaaggagagacgtactttcacctgcacacgttgctgcagtgctgcaacattaagccgttggtcctcggaagatatgtcaaacagattgagaaaaagctggtgagtaccgtctacggggggcacaatcctctgatcgacaattggctccgaattaccaagacaaaatcgatcgggggctccaataaaattcgcgcgcaaagctacattcccgcctatctcattcccaaaaaacaaccggaagttcagtgggcgtggacaaatatcgaggagtatataaaggccgttttaaactctgaattgcgtcatcaaattggagaagcgcatttccaggagcaaggcctcgctctgcgcgacagcaccaacctatcgagaaactctgagggggctcccatcatcgtcagcaagtgcaccaagaaatacatggagctcgtcgagtggctggtcgagaagggcatcacgaccgagaagcaatggctcttggaaaacaaggagagctttcgctccttccaggcctcgagcaactcggctcgccaaatcaaggcggcccttcagggcgccactcaggaaatgctcctcaccaagacggcgtcagactacctgattggcaaagaccccatcggagacatgaccgacaaccgaatctacaaaattttggaaatgaacggctacgaccctctctacgtggccaacctgtttgtaggttggtgtcagatgaagtttggaaaacgaaacacaatctggctgtttggacctgcgaccacgggcaagaccaacattgcggaggctattgcccatgctgtgcccttttatggatgcgtcaactggaccaacgaaaactttcccttcaacgactgcctggaaaagatgatcatttggtgggaagaggggaaaatgacggccaagattgtagagacggctaaagccatcctcgggggatccaaggttcgcgtcgaccaaaagtgcaagtcttcgatgcagctggaacctacgccggtcatcattaccagcaacaccaacatgtgttatgtcgtggatggaaacacgaccacctttgagcacgctcaacccctacaggaccgaatgtttaagctggaactcttgaagcgacttcccgacgactttggaaaagtgaccaaaaaggaagtcagagactttttcgcgtggggggctaaacataccgtagaggtcgattcttgctttttagtaagaaaggcggagtctcgtaaaagacacgccccggaagtggcatcagaggataaaagccctcccgctaaggcggctcgcacagacgagcttcagcatttgagcggcgaggagggaacctctgtctctgccaggtatgttttgaaatgcgctaaacatttggggatggtaaccatgatgtggccatgtagagattgtgaaaaggccaattgtaatataaatcagtgcattttgcataaaagtttgtcttgtaaagagtgttttccagattatgattccgatgtatctgttcaggaaggcgagccttccggcaacccccccttgtcgagctccgacgaggacattccctctcaccaacccccccttgtcaaagattgtaaaccctggactccgtgttcctatcaccacctgaccggggtagccaatagaaattgtagcatgtgcaaattgagaaatgtggatttggatgattgtgacagtgagcaataa

; padding
bases aatgacttaaactagac

; this is the capsid protein
bases atgtctgctgctgattctgttccagattggttggagaattttgtgcgcaagcacattgtcaatccggttgccgaatttgctcatttggaggctggagccccacaaccaaagcctaaccagcagcatcaagatcgaggcggaaccaaggacgatagccgaggtcttgttttacctggctacaagtatcttggtccttttaacggtcttgacaagggtgaacccgtcaacgctgctgacgctgctgcgctcgagcacgacaaggcgtacgaccagcagctgcaagcgggagacaacccctatctgaaatataaccacgcagacgccgaatttcaagaggccctaaaggacgacacatcctttgggggaaatctcggtaaagcggtattccaggccaaaaagagggttctcgaaccctttggcttggctgaagacggaaagacggctcctaccaacgaacgtcgaaaggagaatatagacgactactatcccaagaggaaaaaagccaaggcgggagaagaaaagcccccttctaccgacgcagtagaaggagctggagacggagaaccaagcacatctaccggaggggaaacccccagcggtactcaatctaatacaatgtctgcagggggcggcgcaccaatgggcgatgaccaacagggtgccgatggagtgggtaattcctcgggaaattggcattgcgattccacatggctggacaatcttgtcatcaccaagtccacccgaacctgggtcctgcccagctacaacaaccacatctacaagcgagtctccaacacgggaggagacaactcgtactttggattcagcaccccgtggggatactttgactttaaccgattccactgccacttttcaccgcgagactggcaacggctcatcaacaacaactggggaatccgacccaaggccctcaagtttaagctcttcaacatccaagtcaaagaggtcacgactcaagactcgaccaagaccgtcgccaataacctcaccagcactattcaagtctttgcggactcggaatatcagctaccgtatgtagtgggcaacgcgtccgagggatgcctgcctccctttcccgcggacgtctttgtgctgccgcagtacggatacctgactttggacaataacggaaactctgtcgacagaagcgccttttactgtctcgagtactttccgagtcagatgctgagaacgggcaacaattttgaatttacctacgaatttgaaaaggtgccgttccacagcatgtttgctcacaaccagtcgctgagtcggctaatgaatccgttggtggaccagtacttgtactactttagcaacgtctcggggcctaacaacgctgcccagattcgttacgacaagggtcgtaaggaagacattgccggccaatgcagaaattggctccccggaccattttggcaaaatcagagcgtgcgtctggacaatgccaacaacaatcccaagtgggattactgggcaaactcgaatcgagtaaggctggacggcaaattgtactccgtcaaccctggaattcctcaagccacagaagctacgcagaatccctacaaccagtatccgacgcagtcgactctggtgtttgaaaagaagcccggaggaaaccccaccggagtagatccaaacaatctcaaccttaccaaggatgaagaaattagaaccaccaatcccgtggcctatgccgtgtcaggaacagtcaccggaacgtcggccatcaatcaaaacaatggagccagtcagactcctacggcttccgacgtggacattttgggagccatgcccggaatggtgtggcaaaatagagacatttatctgcaagggcccatttgggccaagattccctccacagacaatcattttcatccttgtcctctcatgggaggattcggattcaagcatccgcctccgcagattctcatcaaaaacacaccggtgccgtcagaccctgcgggattttcagcgaccaagttcaactcgttcatcactcagtattccaccggacaagtcaccgtggaaatcatgtgggaactacaaaaggaaacgtccaagaggtggaatccagaaattcagtttacgtccaatttcaacgccacccaagaactgcagtttgcacccaacgtgtctggagactacgaagaacccagagccatcggctcgagatatctcaccaaacctctgtaa

; padding
bases cttgtatttattcattgtttgtatcatttattcaataaaccgtttattcgtttcagtttcaattcgactcgcgtcatactttctcacaataagcttgtcctcctccccccaataacacgctcgctcgctcgctcgggacaagcgcccgaagggcgcttgcaaccgggcttcgcccggttgtcccgagcgagcgagcgagcgtgttattggggggaggaggacaagcttattgtgagaaagtatgac
