# The neuroscience of program comprehension

## Folder structure

### Stimuli
All stimuli related content is available in `stimuli/`.

We have three versions of the stimuli -
- `EN`: Codes with variable names in English.
- `JAP`: Codes with obfuscated variable names.
- `SENT`: English descriptions of these codes.


The raw stimuli are available in python and text files. `stimuli/stimuli_all_***.py` (`.txt` for `sent` stimuli). The items are separated by a line starting with `#`.

Scripts availble in `scripts/` help convert these stimuli into their corresponding excels and CSVs. These formats are then used by the MATLAB code in `psychtoolbox`, which is seen by the participants.

Due to bugs arising due to different MATLAB versions, we are currently using the CSVs as inputs to the MATLAB code.

English to obfuscated names mapping is available in `stimuli/eng_to_jap.xlsx

### Analaysis and Data
Contains analysis from the behavorial pilots conducted. Corresponding participant responses are in `data/`.

#### Encoding
The following are the encodings used in the analyses
##### ItemType
```
{
 1: 'math_seq',
 2: 'math_for',
 3: 'math_if',
 4: 'str_seq',
 5: 'str_for',
 6: 'str_if'
}
```

##### LangType
```
{
 'en':1,
 'jap':2, 
 'sent':3
}
```
