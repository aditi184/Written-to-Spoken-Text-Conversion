# Written To Spoken Text Conversion

A rule-based NLP engine is designed for converting written text to spoken text. This is part of [Natural Language Processing](https://www.cse.iitd.ac.in/~mausam/courses/col772/autumn2021/) course taken by [Prof Mausam](https://www.cse.iitd.ac.in/~mausam/). Some examples of the text conversion:

1. All abbreviations are separated as they are spoken. Example, “U.S.” or “US” is converted
   to “u s”.
2. All dates are converted into words. Example, “29 March 2012” will be converted to “the
   twenty ninth of march twenty twelve”. “2011-01-25” will be converted to “the twenty fifth of
   january twenty eleven”.
3. All times are converted into words. Example, “04:40 PM” is converted to “four forty p m”.
   “21:30:12” is converted to “twenty one hours thirty minutes and twelve seconds”
4. Currency is also spelled out. “$15.24” is converted to “fifteen dollars and twenty four cents”.
   “£11” is converted to “eleven pounds”.

## Running Mode

Predictions

```bash
python run.py --input_path <path_to_input> --solution_path <path_to_solution>
```

Testing

```bash
python test.py --ground_truth_path <path_to_ground_truth> --solution_path <path_to_solution>
```
