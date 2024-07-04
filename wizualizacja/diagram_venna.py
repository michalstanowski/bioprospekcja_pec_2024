blast = {'s1_k127_2782919_1'}
mmseqs = {'s2_k127_904253_1'}
domains = {'s5_k127_5664362_1'}

sets = (blast, mmseqs, domains)

venn = venn3_unweighted([blast, mmseqs, domains], ('BLASTP', 'MMseqs2', 'domeny'))


colors = {
    '100': 'red',         
    '010': 'lime',        
    '001': 'blue',        
    '110': 'yellow',      
    '101': 'magenta',     
    '011': 'cyan',        
    '111': 'white'        
}


for subset in colors:
    if venn.get_label_by_id(subset):  
        venn.get_label_by_id(subset).set_color('black')
        venn.get_label_by_id(subset).set_fontsize(10)
        venn.get_label_by_id(subset).set_fontweight('bold') 

    if venn.get_patch_by_id(subset):  
        venn.get_patch_by_id(subset).set_color(colors[subset])
        venn.get_patch_by_id(subset).set_alpha(0.35)
        venn.get_patch_by_id(subset).set_edgecolor('black')  
      

for label in venn.set_labels:
    if label:  
        label.set_fontsize(12)
        label.set_fontweight('bold')
        
plt.show()
