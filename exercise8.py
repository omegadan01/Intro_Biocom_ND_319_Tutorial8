#########exercise 8#############################


#####Question 1

import re
vcf = open("Cflorida.vcf","r")
outfile = open("CfloridaCounts.txt","w")
search_tex =r'(CF.A.|CF.A2.|CF07.A.|cf.a.)([0-9]{3})'
replace_tex =r'Cf.Sfa.\2'

for line in vcf:
    line = line.strip()
    if "##" in line:
		outfile.write(line + "\n")	
	elif "#" in line:
        texas = re.sub(search_tex, replace_tex, line)
        outfile.append(line + "\n")
        print texas
	else:
        #select lines with "Contig", find 0/0:, keep 1 digit after that, get rid of everything else
        outfile.append(line + "\n")
vcf.close()











#####Question 2
