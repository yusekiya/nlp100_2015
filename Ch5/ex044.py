# 与えられた文の係り受け木を有向グラフとして可視化せよ．
# 可視化には，係り受け木をDOT言語に変換し，Graphvizを用いるとよい．
# また，Pythonから有向グラフを直接的に可視化するには，pydotを使うとよい．
import ex041
import networkx as nx
import matplotlib.pyplot as plt

def main():
    chunks = ex041.generate_chunks_whole_sentence()
    res = []
    for sentence in chunks:
        surface_dst = [(chunk.get_phrase(), chunk.dst) for chunk in sentence]
        dependency = [('{}'.format(surface), '{}'.format(surface_dst[dst][0]))\
                      for surface, dst in surface_dst if surface and dst!=-1]
        if dependency:
            res.append(dependency)
    # output dot lang for n-th sentence
    output_dot(res[9])
    return 0


def plot_network(DiGraph):
    pos = nx.spring_layout(DiGraph)
    nx.draw_networkx_nodes(DiGraph, pos, node_size=5000, node_color='white')
    nx.draw_networkx_edges(DiGraph, pos)
    nx.draw_networkx_labels(DiGraph, pos, font_family='Osaka', font_size=20)
    plt.show()


def output_dot(dependency, fname='./output.dot'):
    DG = nx.DiGraph()
    DG.add_edges_from(dependency)
    nx.set_node_attributes(DG, 'fontname', 'Osaka')
    nx.nx_agraph.write_dot(DG, fname)


if __name__ == '__main__':
    main()
    print('finished')
