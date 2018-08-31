# dsm-to-elevation-array

This is a python script to convert DSM (single band) file to text file of list of density of elevation.
Other `.sh` files are just a helper script to use docker conveniently, and important thing is `main.py`.

You can run this script with three command line arguments.

1. First one is a path of input tif, i.e., DSM file
2. Second one is a path of output txt.
3. Third one is number of bins. For example, when your DSM has minimum of `-10` and maximum of `10`, and your bin value is `10`, result 10 bins collect values between `[-10, -8)`, `[-8, -6)`, `[-6, -4)`, `[-4, -2)`, `[-2, 0)`, `[0, 2)`, `[2, 4)`, `[4, 6)`, `[6, 8)`, `[8, 10]`. In other words, first bin collects values between `[-10, -8)`, so you can refer this bin to check how many points have values between `[-10, 8)`.
