import unittest
import numpy as npy
import os, sys
from util import insert_local_path, setup_data2
insert_local_path()
sys.path.insert(0, '../lib')
from spanlib_python import Filler
#from spanlib import Filler

#sys.path.insert(0, '../libok/spanlib')
#from spanlib_python import Filler

import pylab as P

class TestSequenceFunctions(unittest.TestCase):

    def test_fill_simple(self):
        """Test hole filling and forecast estimation with a single variable"""
        # Init
        nt = 500
        tmax = 80.
        ref = npy.ma.sin(npy.linspace(0., tmax, nt))+10. # period = 2pi
        ref = npy.ma.resize(ref, (3, nt)).T
        ref[:, 1] = npy.ma.masked
        withholes = ref.copy()
#        withholes[200:215] = npy.ma.masked
#        withholes[200:415] = npy.ma.masked
#        withholes[480:] = npy.ma.masked
        withholes[380:] = npy.ma.masked
        # Fill
        filled = Filler(withholes, loglevel='debug')
        print 'plot'
        P.plot(filled.filtered[:, 0], 'r')
#        P.plot(withholes[:, 0], 'b')
        P.show()
        self.assertTrue(npy.allclose(filled.filtered.filled()[200:202,0], 
            npy.array([10.61948956,  10.74003157])))
        
#    def test_fill_double(self):
#        """Test hole filling and forecast estimation with a pair of variables"""
#        # Init
#        nt = 500
#        tmax = 80.
#        ref = npy.ma.sin(npy.linspace(0., tmax, nt))+10. # period = 2pi
#        ref = npy.ma.resize(ref, (3, nt)).T
#        ref[:, 1] = npy.ma.masked
#        withholes = ref.copy()
#        withholes[200:215] = npy.ma.masked
#        withholes[480:] = npy.ma.masked
#        # Fill
#        filled = Filler([withholes, withholes*100])
##        P.plot(filled.filtered[0][:, 0], 'r')
##        P.plot(withholes[:, 0], 'b')
##        P.show()
#        self.assertTrue(npy.allclose(filled.filtered[0].filled()[200:202,0], 
#            npy.array([10.61834159,  10.73914392])))
        
if __name__ == '__main__':
    unittest.main()
