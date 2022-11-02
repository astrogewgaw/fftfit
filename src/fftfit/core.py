import numpy as np
import fftfit._kernels as kernels


def fftfit(prof, tmpl, rotate=True):

    """
    Use the FFTFIT algorithm on the profile and template.
    This determines the following parameters, as defined
    in J. H. Taylor's talk at the Royal Society ("Pulsar
    timing and relativistic gravity", Phil. Trans. R. Soc.
    Lond. A (1992), 341, 117-134): tau, tau_err, a, a_err,
    b, b_err, ngood.
    """

    _, amps, phz = kernels.cprof(tmpl)
    ph0 = phz[0]
    if rotate:
        phz = np.fmod(phz - np.arange(1, len(phz) + 1) * ph0, 2 * np.pi)
    return kernels.fftfit(prof, amps, phz)
