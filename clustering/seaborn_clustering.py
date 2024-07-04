import numpy as np
import seaborn as sns
import streamlit as st
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

def create_dict():
    file = open("prots.fasta")

    dict_lengths = dict()

    for line in file:
        line = line.strip()
        if line[0] == ">":
            id = line[1:]
            dict_lengths[id] = 0
        else:
            dict_lengths[id] = len(line)

    return dict_lengths


def create_dict_seq():
    file = open("prots.fasta")
    dict_lengths = dict()
    for line in file:
        line = line.strip()
        if line[0] == ">":
            id = line[1:]
            dict_lengths[id] = ""
        else:
            dict_lengths[id] = line

    return dict_lengths

def create_heatmap_seaborn(file_path, dict_lengths):
    ava = open(file_path)

    pattern_identities = "Identities"
    dict_heatmap = dict()

    for line in ava:
        line = line.strip().split("\t")
        print(line)
        query = line[0]
        target = line[1]
        percent = int(float(line[2])*100)
        if query not in dict_heatmap and query != target:
            dict_heatmap[query] = [(target, int(percent))]
        if query != target:
            dict_heatmap[query].append((target, int(percent)))
        if int(percent) < 40:
            dict_heatmap[query].append((target, 0))

    dict_heatmap_with_lengths = {}
    for query_id, targets in dict_heatmap.items():
        updated_query_id = f"{dict_lengths[query_id]}_{query_id}"
        updated_targets = [(f"{dict_lengths[target]}_{target}", percent) for target, percent in targets]
        dict_heatmap_with_lengths[updated_query_id] = updated_targets

    for query_id in dict_heatmap_with_lengths:
        dict_heatmap_with_lengths[query_id] = sorted(dict_heatmap_with_lengths[query_id], key=lambda x: x[1], reverse=True)


    targets = sorted(set(target for sublist in dict_heatmap_with_lengths.values() for target, _ in sublist))
    query_ids = sorted(dict_heatmap_with_lengths.keys())
    heatmap_data = np.zeros((len(query_ids), len(targets)))

    print(targets, query_ids)


    print(dict_heatmap)

    for i, query_id in enumerate(query_ids):
        for target, percent in dict_heatmap_with_lengths[query_id]:
            j = targets.index(target)
            heatmap_data[i, j] = float(percent)

    # np.savetxt('heatmap_data_cell.tsv', heatmap_data, delimiter='\t', fmt='%.2f')
    
    # for i in range(len(targets)):
    #     targets[i] = targets[i][4:]
    
    # for i in range(len(query_ids)):
    #     query_ids[i] = query_ids[i][4:]
    

    # all_prots = targets+query_ids 
    # dict_seqs = create_dict_seq()

    # heatmap_prots = open("heatmap_prots.fasta", "w")    

    # for id in all_prots:
    #     heatmap_prots.write(f">{id}\n{dict_seqs[id]}\n")

    sns.set(font_scale=0.9)  
    plt.figure(figsize=(10, 10))


    colors = [(1.0, 1.0, 1.0), (0.85, 0.9, 1.0), (0.7, 0.8, 1.0), (0.55, 0.7, 1.0), (0.4, 0.6, 1.0), (0.3, 0.5, 1.0)]

    cluster = sns.clustermap(heatmap_data, method='average', cmap = LinearSegmentedColormap.from_list('LightBlues', colors), xticklabels=targets, yticklabels=query_ids)

    data_matrix = cluster.data2d
    row_labels = cluster.dendrogram_row.reordered_ind
    col_labels = cluster.dendrogram_col.reordered_ind
    ax_heatmap = cluster.ax_heatmap

    for i, row_label in enumerate(row_labels):
        for j, col_label in enumerate(col_labels):
            query_id = query_ids[row_label]
            target = targets[col_label]
            percent = heatmap_data[row_label, col_label]
            query_env = query_id[5]
            target_env = target[5]
            label = f"{query_env+target_env}" 
            ax_heatmap.text(j+0.5, i+0.5, label, fontdict={"ha": "center", "va": "center", "fontsize": 10})

    plt.xlabel("Target Sequences")
    plt.ylabel("Query Sequences")
    plt.title("Heatmap")
    plt.xticks(rotation=45, ha='right')
    plt.yticks(rotation=0)
    plt.tight_layout()

    return plt

def main():
    st.title("Clustermap Heatmap Visualization")

    file_path = st.file_uploader("Upload your All vs All Blast file (.txt)")
    if file_path is not None:
        st.write("### Heatmap (Seaborn)")
        dict_lengths = create_dict()
        clustermap = create_heatmap_seaborn(file_path.name, dict_lengths)
        st.pyplot(clustermap)

if __name__ == "__main__":
    main()
