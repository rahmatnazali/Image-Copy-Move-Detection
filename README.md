This is a python package for detecting copy-move attack on a digital image.

This project is part of our paper that [has been published at Springer](https://link.springer.com/chapter/10.1007%2F978-3-030-73689-7_39). More detailed theories and steps are explained there.

The project is formerly written with Python 2 for our Undergraduate Thesis, which is now left unmaintained [here](https://github.com/rahmatnazali/image-copy-move-detection-python2). The original thesis is written in Indonesian that in any case can also be downloaded from [here](http://repository.its.ac.id/1801/).

## Description
The implementation generally manipulates overlapping blocks, and are constructed based on two algorithms:
1. Duplication detection algorithm, taken from [Exposing Digital Forgeries by Detecting Duplicated Image Region](http://www.ists.dartmouth.edu/library/102.pdf) ([alternative link](https://www.semanticscholar.org/paper/Exposing-Digital-Forgeries-by-Detecting-Duplicated-Popescu-Farid/b888c1b19014fe5663fd47703edbcb1d6e4124ab)); Fast and smooth attack detection algorithm on digital image using [principal component analysis](https://en.wikipedia.org/wiki/Principal_component_analysis), but sensitive to noise and any following manipulations that are being applied after the attack phase (in which they call it _post region duplication process_)
2. Robust detection algorithm, taken from [Robust Detection of Region-Duplication Forgery in Digital Image](https://ieeexplore.ieee.org/document/1699948); Relatively slower process with rough result on the detection edge but are considered robust towards noise and _post region duplication process_

### How do we modify them?

We know that the first algorithm use `coordinate` and `principal_component` features, while the second algorithm use `coordinate` and `seven_features`.

Knowing that, we then attempt to give a tolerance by merging all the features like so:

![Modification diagram](assets/modification_diagram.PNG?raw=true) 

The attributes are saved as one object. Then a lexicographical sorting is applied to the principal component and the seven features.

The principal component will bring similar block closer, while the seven features will back up the detection for a block that can't be detected by principal component due to being applied with post region duplication process (for example being blurred).

By doing so, the new algorithm will have a tolerance regarding variety of the input image. The detection result will be relatively smooth and accurate for any type of image, with a trade-off in run time as we basically run two algorithm.

## Example image
### Original image
![Original image](assets/dataset_example.png?raw=true) 
### Forgered image
![Forgered image](assets/dataset_example_blur.png?raw=true)
### Example result after detection
![Result image](output/20191125_094809_lined_dataset_example_blur.png)

Another example of the result can be seen in the `output` directory.

## Getting Started

Assuming you already have Python 3.x on your machine:
- clone this repo
- create a [virtual environment](https://docs.python.org/3/library/venv.html) and enter into it
- run `pip3 install -r requirements.txt`

## Example

```python3
from pimage import copy_move

copy_move.detect('assets/', 'dataset_example_blur.png', 'output/', block_size=32)
```

You can also see directly at the [example code](example/example.py).

## Verbose mode

When running `copy_move.detect()` or `copy_move.detect_and_export()`, you can pass `verbose=True` to output 
the status of each step. The default value will be `False` and nothing will be printed.

Example of the verbose output:

```
Processing: dataset/multi_paste/cattle_gcs500_copy_rb5.png
Step 1 of 4: Object and variable initialization
Step 2 of 4: Computing characteristic features
100%|██████████| 609/609 [04:14<00:00,  2.39it/s]
Step 3 of 4:Pairing image blocks
100%|██████████| 241163/241163 [00:00<00:00, 816659.95it/s]
Step 4 of 4: Image reconstruction
Found pair(s) of possible fraud attack:
((-57, -123), 2178)
((-11, 140), 2178)
((-280, 114), 2178)
((-34, -305), 2178)
((-37, 148), 2178)
Computing time : 254.81 second
Sorting time   : 0.89 second
Analyzing time : 0.3 second
Image creation : 1.4 second
Total time    : 0:04:17 second 
```
