# Data Structures and Algorithms Suite

Practice implementing common data structures and algorithms and use the test suite to check if your solution is correct.

This is based on the [*kata-machine*](https://github.com/ThePrimeagen/kata-machine) by [*The Primeagen*](https://www.twitch.tv/theprimeagen) which was a typescript suite for his course [*The Last Algorithms Course You'll Need*](https://frontendmasters.com/courses/algorithms/) on Frontend Masters.

**Note: At this time, not all the algorithms have been implemented. I'm still working on it.**

## How to Use the Suite
The suite consists of a ```src``` folder and a ```tests``` folder. The ```src``` folder contains all the files for each data structure and algorithm you can practice implementing. This is where you'll be working. Type annotations are provided to help you recognize how the function should behave i.e. what the arguments are and what the function should return.

To test your implementation, open a terminal window, cd into the root ```dsa-suite``` directory and run the following command:

```commandline
python test.py <function_name>
```

where the ```<function_name>``` is the name of the function you want to test.

#### *Example*
If I want to try implementing linear search, I'd open the ```LinearSearchList.py``` file in the ```src``` folder and write my implementation:

```python
def linear_search(haystack: List[int], needle: int) -> bool:
    for item in haystack:
        if item == needle:
            return True
    return False
```

Then, I'd run this command from a terminal window ensuring I am in the root folder where the ```test.py``` file is located:

```commandline
python test.py linear_search
```

If your implementation is correct, you should see an ```OK``` at the bottom of the output. Otherwise, you'll see a message similar to ```FAILED (failures=1)```
