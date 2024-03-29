"""
This script performs summarization by latent semantic analysis.
"""

import argparse
import os

import numpy as np

from utils import doc
from utils import fs
from utils import misc
from utils import weight

#------------------------------------------------------------------------------
# Parse command line arguments
#------------------------------------------------------------------------------

parser = argparse.ArgumentParser(
        description='Summarize articles using the latent semantic analysis.')
parser.add_argument('output_dir', type=str,
        help='The directory which to write the output data')
parser.add_argument('input_dir', type=str,
        help='The directory which contains the input data')
parser.add_argument('local_weight', type=str,
        help='The local weighting strategy to use')
parser.add_argument('normalize', type=misc.str_to_bool,
        help='Indicates the local weights should be normalized')
args = parser.parse_args()

# Get the command line arguments in a usable form
OUTPUT_DIR   = os.path.abspath(args.output_dir)
INPUT_DIR    = os.path.abspath(args.input_dir)
LOCAL_WEIGHT = weight.local_builder(args.local_weight, args.normalize)

# A description of the summarization strategy
STRATEGY = "LSA_{{{}{}}}".format(args.local_weight[0].upper(), int(args.normalize))

# Create the ouput directory
fs.make_dir(OUTPUT_DIR)

#------------------------------------------------------------------------------
# Process the data
#------------------------------------------------------------------------------

INPUT_FILENAMES = sorted(fs.list_dir(INPUT_DIR, files=True))

def summarize(document):
    """
    Generate a summary for a document and set it in place.

    # Arguments

    * `document (Document): The document to summarize.
    """
    matrix = document.word_matrix(LOCAL_WEIGHT)
    # Note that `vh` is returned as the transpose
    _, _, vh = np.linalg.svd(matrix, full_matrices=True)

    summary_indices = []
    for i in range(document.summary_size()):
        # Make sure that no duplicate sentences are included sorted the
        # candidate sentences and picking the highest ranked one that is not
        # yet chosen
        points = sorted(enumerate(vh[:,i]), key=lambda x: x[1], reverse=True)
        for j, _ in points:
            if j not in summary_indices:
                summary_indices.append(j)
                break
    # Set the summary in the document
    document.set_summary(summary_indices)

for fname in INPUT_FILENAMES:
    input_file = os.path.join(INPUT_DIR, fname)
    output_file = os.path.join(OUTPUT_DIR, fname)
    # Prepare the file
    document = doc.Document.load_file(input_file)
    # Summarize the document in place
    summarize(document)
    document.summary_strategy = STRATEGY
    # Write the generated document to the output location
    document.dump_file(output_file)
