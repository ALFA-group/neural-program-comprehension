fROI analysis files are named according to the following convention: 

*localizer task "_" task with effects of interest ".csv"*

**Tasks:**
- langlocSN: language localizer task (used to define language system fROIs; S - sentence reading, N - nonword reading)
- MDloc: spatial working memory task (used to define MD fROIs; E - easy, H - hard)
- brainCode: Python program comprehension task (en - code problems, English identifiers, jap - code problems, Japanese identifiers, sent - sentence problems)

**fROI data column names:**
- ROI: region of interest (for number to name conversion, see analysis files)
- Subject: participant ID
- Effect: condition of interest
- LocalizerSize: size of the fROI (top 10% of the voxels most responsive to the localizer contrast within a given parcel)
- EffectSize: strength of response to the effect of interest 

**Behavioral data column names (beh_scores.csv):**
- Subject: participant ID	
- Preassessment: Python proficiency test score	
- Japanese: self-reported knowledge of Japanese (avg of speaking, listening, reading, and writing on a scale from 0 to 5)	
- SelfReport: self-reported knowledge of Python (on a scale from 0 to 5)
