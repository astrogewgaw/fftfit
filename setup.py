from numpy.distutils.core import setup
from numpy.distutils.extension import Extension

if __name__ == "__main__":
    setup(
        ext_modules=[
            Extension(
                name="fftfit._kernels",
                sources=[
                    "src/fftfit/brent.f",
                    "src/fftfit/cprof.f",
                    "src/fftfit/fccf.f",
                    "src/fftfit/ffft.f",
                    "src/fftfit/fftfit.f",
                    "src/fftfit/_kernels.pyf",
                ],
            )
        ]
    )
