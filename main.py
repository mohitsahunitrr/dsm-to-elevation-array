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
    extract_elevations(argv[1], int(argv[3]))

def validate_argv(argv):
    if len(argv) != 3:
        print("You should pass two arguments to this script. Abort.")
        sys.exit(1)

    if not os.path.isfile(argv[1]):
        print("First argument for this script should be a input file")
        sys.exit(1)

    if not argv[2].isdigit():
        print("Second argument for this script should be a positive integer")
        sys.exit(1)

def extract_elevations(input_path, number_of_bar):
    """
    Convert DSM file in input_path to histogram file of result_path
    """
    def extract_elevations_of_block(block_2d):
        block_1d = block_2d.flatten()
        block_1d_without_no_data = gn.extract(block_1d != no_data_value, block_1d)
        return gn.histogram(block_1d_without_no_data, bins=gn.linspace(input_minimum, input_maximum, number_of_bar))

    def summarize_block(previous_result, result):
        if previous_result is None:
            return result
        else:
            return (previous_result[0] + result[0], previous_result[1])

    input_tiff = gdal.Open(input_path)

    if input_tiff.RasterCount != 1:
        raise ValueError("DSM should have only one band data")

    input_band = input_tiff.GetRasterBand(1)
    (input_minimum, input_maximum, _, _) = input_band.GetStatistics(True, True)
    no_data_value = input_band.GetNoDataValue()

    (output_counts, output_bins) = loop_through_blocks(input_band, 500, extract_elevations_of_block, summarize_block)
    result = json.dump({ "counts": output_counts.tolist(), "bins": output_bins.tolist() }, separators=(",", ":"))
    print(result)

def loop_through_blocks(input_band, block_size, calc, summarize):
    x_size = input_band.XSize
    y_size = input_band.YSize
    result = None

    for x_offset in range(0, x_size, block_size):
        x_width = min(block_size, x_size - x_offset)

        for y_offset in range(0, y_size, block_size):
            y_width = min(block_size, y_size - y_offset)
            block = input_band.ReadAsArray(x_offset, y_offset, x_width, y_width)

            result = summarize(result, calc(block))

    return result

if __name__ == "__main__":
    main()
