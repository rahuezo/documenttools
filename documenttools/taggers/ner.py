import sys 

try: 
    from networktools.events.entities import stanford_ner_to_tree, Tree
except ImportError: 
    print 'You need to install networktools first.'
    sys.exit()

from documenttools.files.readers import FileReader

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

    def __init__(self, input_file): 
        self.file = input_file

    def tag(self): 
        reader = FileReader(self.file)
        extension = reader.get_extension()
        content = reader.read()
        
        output_filename = self.file.replace('.{}'.format(extension), '_ner_tagged.{}'.format(extension))

        return output_filename, NerTagger.create_tagged_content(content)
