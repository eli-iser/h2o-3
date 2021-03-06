import sys
sys.path.insert(1,"../../")
import h2o
from tests import pyunit_utils
import numpy as np

def test_negate():

  a = np.random.randn(100,1).tolist()
  d = h2o.H2OFrame(a)

  assert d[~(d['C1']>0),'C1'] == d[(d['C1']<=0), 'C1']
  assert d[~(d['C1']<=0),'C1'] == d[(d['C1']>0),'C1']


if __name__ == "__main__":
   pyunit_utils.standalone_test(test_negate)
else:
   test_negate()
