#------------------------------------------------------------------------------
# PyMTL components
#------------------------------------------------------------------------------

from Model          import Model
from Model          import capture_args  # TEMPORARY
from signals        import Wire, InPort, OutPort
from Bits           import Bits
from SimulationTool import SimulationTool
from PortBundle     import PortBundle, create_PortBundles
from BitStruct      import BitStruct, BitStructDefinition, BitField
from helpers        import get_nbits, get_sel_nbits, zext, sext, concat
from SignalValue    import CreateWrappedClass

#------------------------------------------------------------------------------
# py.test decorators
#------------------------------------------------------------------------------

from pytest          import mark
from distutils.spawn import find_executable
from os.path         import exists

has = lambda x: find_executable( x ) != None

requires_xcc = mark.skipif( not( has('maven-gcc') and has('maven-objdump') ),
                            reason='requires cross-compiler toolchain' )

requires_vmh = mark.skipif( not exists('../tests/build/vmh'),
                            reason='requires vmh files' )

#------------------------------------------------------------------------------
# new_pymtl namespace
#------------------------------------------------------------------------------

__all__ = [ # Model Construction
            'Model',
            # Signals
            'InPort',
            'OutPort',
            'Wire',
            'PortBundle',
            'create_PortBundles',
            # Message Types
            'Bits',
            'BitStruct',
            # Message Constructors
            'BitStructDefinition',
            'BitField',
            # Tools
            'SimulationTool',
            # TEMPORARY
            'capture_args',
            'CreateWrappedClass',
            # Helper Functions
            'get_nbits',
            'get_sel_nbits',
            'sext',
            'zext',
            'concat',
            # py.test decorators
            'requires_xcc',
            'requires_vmh',
          ]

