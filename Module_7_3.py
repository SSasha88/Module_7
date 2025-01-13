print('Задача "Найдёт везде"')
print()
class WordsFinder:
    def __init__(self, *filenames):
        self.file_names = filenames
    def get_all_words(self):
        all_words = {}
        punctuation = [',', '.', '=', '!', '?', ';', ':', ' - ', ]
        for filename in self.file_names:
            with open(filename, encoding='utf-8') as f:
                content = f.read()
            for punc in punctuation:
                content = content.replace(punc, '')
            words = content.lower().split()
            all_words[filename] = words
        return all_words
    def find(self, word):
        results = {}
        word = word.lower()
        for filename, words in self.get_all_words().items():
            if word in words:
                index = words.index(word)
                results[filename] = index + 1
        return results
    def count(self, word):
        results = {}
        word = word.lower()
        for filename, words in self.get_all_words().items():
            count = words.count(word)
            if count > 0:
                results[filename] = count
        return results


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())
print(finder2.find('TEXT'))
print(finder2.count('teXT'))
