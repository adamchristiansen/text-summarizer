# An extractive text summarizer

This is a project for the University of Lethbridge graduate level CPSC 5310
course, Studies in Computation Intelligence: Advanced Data Processing. The
strategies implemented are based on the work of Gong and Liu.

> Yihong Gong and Xin Liu. Generic text summarization using relevance measure
> and latent semantic analysis.
> In _Proceedings of the 24th annual international ACM SIGIR conference on
> Research and development in information retrieval_, pages 19–25. ACM, 2001.

## Running

The simple way to run the program is to open a shell and run:

```sh
$ python3 run.py
```

To run everything in the execution matrix, run:

```sh
$ python3 run.py --all
```

All of the generated data can be removed with:

```sh
$ python3 run.py --clean
```

## Programs

The following programs are included in the root directory:

* `lsm.py`: perform a summarization using latent semantic analysis.
* `prep.py`: preprocess the corpus into usable data.
* `rel.py`: perform a summarization using the relevance measure.
* `run.py`: run all of the other scripts in the correct order.
