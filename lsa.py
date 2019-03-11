"""
This script performs summarization by latent semantic analysis.
"""

import argparse
import os

from utils import doc
from utils import fs

#------------------------------------------------------------------------------
# Parse command line arguments
#------------------------------------------------------------------------------

parser = argparse.ArgumentParser(
        description='Summarize articles using the latent semantic analysis.')
parser.add_argument('output_dir', type=str,
        help='The directory which to write the output data')
parser.add_argument('input_dir', type=str,
        help='The directory which contains the input data')
args = parser.parse_args()

# Get the command line arguments in a usable form
OUTPUT_DIR = os.path.abspath(args.output_dir)
INPUT_DIR  = os.path.abspath(args.input_dir)

# Create the ouput directory
fs.make_dir(OUTPUT_DIR)

#------------------------------------------------------------------------------
# Process the data
#------------------------------------------------------------------------------

INPUT_FILENAMES = sorted(fs.list_dir(INPUT_DIR, files=True))

for fname in INPUT_FILENAMES:
    input_file = os.path.join(INPUT_DIR, fname)
    output_file = os.path.join(OUTPUT_DIR, fname)
    document = doc.Document.load_file(input_file)
    # TODO Do the processing
    document.dump_file(output_file)