__author__ = 'Stevevn LI'

import nose
from auto_checklog import AutoCheckLog

if __name__ == '__main__':
    nose.main(addplugins=[AutoCheckLog()])

