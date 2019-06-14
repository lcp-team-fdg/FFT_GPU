#ifndef __FDG_GPU_FFT__
#define __FDG_GPU_FFT__

int prepare(int size, int bands_count); // 10 -> 2^10 fft samples

float* compute(float* data, int** bands_indexes);

int release(void);

#endif //  __FDG_GPU_FFT__