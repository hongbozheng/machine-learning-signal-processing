#!/usr/bin/env python3

import numpy
import scipy.linalg
import matplotlib.pyplot

DFT_size = 64


def main():
    dft_mat = numpy.fft.fft(numpy.eye(N=DFT_size))
    hann = numpy.diag(scipy.signal.windows.hann(M=64))
    print(scipy.signal.windows.hann(M=64))
    dft_hann_mat = dft_mat@hann

    A = numpy.zeros(shape=(64*5, 64*3))

    for i in range(5):
        A[i*64:(i+1)*64, i*32:i*32+64] = dft_hann_mat

    # matplotlib.pyplot.imshow(X=numpy.real(val=dft_mat))
    # matplotlib.pyplot.imshow(X=numpy.real(val=hann))
    # matplotlib.pyplot.imshow(X=numpy.real(val=dft_hann_mat))
    matplotlib.pyplot.imshow(X=numpy.real(val=A))
    matplotlib.pyplot.show()
    return

if __name__ == "__main__":
    main()