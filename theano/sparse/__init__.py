import sys

try:
    import scipy
    scipy_ver = [int(n) for n in scipy.__version__.split('.')[:2]]
    enable_sparse = bool(scipy_ver >= [0, 7])
    if not enable_sparse:
        sys.stderr.write("WARNING: scipy version = %s."
                " We request version >=0.7.0 for the sparse code as it has"
                " bugs fixed in the sparse matrix code.\n" % scipy.__version__)
except ImportError:
    enable_sparse = False
    sys.stderr.write("WARNING: scipy can't be imported."
            " We disable the sparse matrix code.")

from type import *

if enable_sparse:
    from basic import *
    import opt
    import sharedvar
    from sharedvar import sparse_constructor as shared
