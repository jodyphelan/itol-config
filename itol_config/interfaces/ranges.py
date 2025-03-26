from .base_interface import ConfigWriter

template = """DATASET_RANGE
SEPARATOR COMMA
DATASET_LABEL,%(dataset_label)s
COLOR,#ff0000

RANGE_TYPE,bracket
RANGE_COVER,clade


LEGEND_TITLE,%(legend_title)s
LEGEND_SHAPES,%(legend_shapes)s
LEGEND_LABELS,%(legend_labels)s
LEGEND_COLORS,%(legend_colours)s

DATA
"""

class RangeConfigWriter(ConfigWriter):
    # init super
    def __init__(self, tree: str, data: dict, label:str, colour_lookup: dict):
        
        super().__init__(data, label, colour_lookup)
        import ete3
        tree = ete3.Tree(tree,format=1)
        unique_values = set(data.values())

        self.clades = []
        for val in unique_values:
            taxa_with_val = [t for t in data if data[t] == val]
            ancestral_node = tree.get_common_ancestor(taxa_with_val)
            leaves = [leaf.name for leaf in ancestral_node.get_leaves()]
            node1 = leaves[0]
            node2 = leaves[-1]
            self.clades.append(
                {
                    'node1':node1,
                    'node2':node2,
                    'label':val
                }
            )
        

        

    def write(self, outfile: str) -> None:
        """
        Parse the data to be coloured.
        
        Parameters
        ----------
        outfile : str
            Output file name.
        
        Returns
        -------
        None
        """
        with open(outfile,"w") as O:
            O.write(template % self.config)
            for label in self.clades:
                O.write("%(node1)s,%(node2)s,#ffffff,,#000000,solid,2,%(label)s,#000000,4,normal" % (label))
