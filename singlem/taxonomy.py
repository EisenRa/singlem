class Taxonomy:
    @staticmethod
    def split_taxonomy(taxonomy_string):
        if taxonomy_string:
            tax = [t.strip() for t in taxonomy_string.split(';')]
            while len(tax) > 0 and tax[-1] == '':
                tax = tax[:-1]
            return tax
        else:
            return None

    @staticmethod
    def lca_taxonomy_of_strings(taxonomy_strings):
        hit_taxonomies = list([list([ta.strip() for ta in t.split(';')]) for t in taxonomy_strings])
        lca = hit_taxonomies[0]
        for taxonomy in hit_taxonomies[1:]:
            if len(taxonomy) < len(lca):
                lca = lca[:len(taxonomy)]
            for i, tax in enumerate(taxonomy):
                if i >= len(lca) or tax != lca[i]:
                    lca = lca[:i]
                    break
        return '; '.join(lca)
