# -*- coding: utf-8 -*-

from mrjob.job import MRJob
import unicodedata
import re

class MRWordFrequencyCount(MRJob):

    def mapper(self, _, line):
      data = u = unicode(line, "utf-8")
      normal = unicodedata.normalize('NFKD', data).encode('ASCII', 'ignore')
      new_line = re.sub('\W+',' ', normal.lower())

      for w in new_line.decode('utf-8','ignore').split():
        yield w,1

    def reducer(self, w, values):
      yield w, sum(values)

if __name__ == '__main__':
    MRWordFrequencyCount.run()