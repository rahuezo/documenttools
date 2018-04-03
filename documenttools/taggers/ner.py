from networktools.events.entities import stanford_ner_to_tree, Tree
from documenttools.files.readers import FileReader

import tkFileDialog as fd
import re


class NerTagger: 
    @staticmethod
    def create_tagged_content(text): 
        tree = stanford_ner_to_tree(text)
        tagged_content = []

        for subtree in tree: 
            if type(subtree) == Tree: 
                tagged_content.append('<{label}>{ent}</{label}>'.format(label=subtree.label(), ent=' '.join([e[0] for e in subtree])))
            else: 
                tagged_content.append(subtree[0])

        return ' '.join(tagged_content)

    def __init__(self, files): 
        self.files = files

    def tag(self): 
        for f in self.files: 
            reader = FileReader(f)
            content = reader.read()

            if not content: 
                continue
            yield NerTagger.create_tagged_content(content)
