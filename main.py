#!/usr/bin/env python
import json, os, sys

from osgeo import gdal, gdalnumeric as gn

gdal.UseExceptions()

def main():
    """
    Entry function
    """
    argv = sys.argv

    validate_argv(argv)
    extract_elevations(argv[1], argv[2], int(argv[3]))

def validate_argv(argv):
    if len(argv) != 4:
        print("You should pass two arguments to this script. Abort.")
        sys.exit(1)

    if not os.path.isfile(argv[1]):
        print("First argument for this script should be a input file")
        sys.exit(1)

    if not argv[3].isdigit():
        print("Third argument for this script should be a positive integer")
        sys.exit(1)

def extract_elevations(input_path, result_path, number_of_bar):
    """
    Convert DSM file in input_path to histogram file of result_path
    """
    input_array = gdal.Open(input_path).ReadAsArray()

    if len(input_array.shape) != 2:
        raise ValueError("DSM should have only one band data")

    (output_counts, output_bins) = gn.histogram(input_array.flatten(), bins=number_of_bar)
    output_file = open(result_path, 'w')
    json.dump({ "counts": output_counts.tolist(), "bins": output_bins.tolist() }, output_file, separators=(",", ":"))
    output_file.write('\n')
    output_file.close()
    
if __name__ == "__main__":
    main()
