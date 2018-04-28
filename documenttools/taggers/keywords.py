from documenttools.files.readers import FileReader

import re, os


class KeywordTagger: 
    @staticmethod
    def create_tagged_content(header, content): 
        return 'Found Keywords: {hd}\n\n{ct}'.format(hd=header, ct=content)

    @staticmethod
    def create_txt_name(f): 
        rf = f[::-1]
        rf_no_ext = rf.replace(rf[0:rf.index('.') + 1], '')
        return rf_no_ext[::-1] + '.txt'

    def __init__(self, input_file, keywords): 
        self.file = input_file
        self.keywords = keywords

    def get_keyword_occurrences(self, content): 
        return filter(lambda keyword: re.search(r'\b{kw}\b'.format(kw=keyword), content, flags=re.IGNORECASE), self.keywords)

    def emphasize_keyword_occurrences(self, content, keyword_occurrences): 
        for keyword in keyword_occurrences:
            ocurrences = re.findall(r'\b{kw}\b'.format(kw=keyword), content, flags=re.IGNORECASE) 

            for ocurrence in ocurrences: 
                content = content.replace(' {} '.format(ocurrence), ocurrence.upper())
        return content

    def tag(self): 
        # reader = FileReader(self.file)
        content = self.file[1] #reader.read()
        
        keyword_occurrences = self.get_keyword_occurrences(FileReader.normalize(content))

        if keyword_occurrences: 
            header = ', '.join(keyword_occurrences).upper()
            return KeywordTagger.create_txt_name(self.file[0]), KeywordTagger.create_tagged_content(header, content)
        return None
    