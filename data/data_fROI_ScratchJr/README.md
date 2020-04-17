fROI analysis files are named according to the following convention: 

*localizer task "_" task with effects of interest ".csv"*

**Tasks:**
- langlocSN: language localizer task (used to define language system fROIs)
- MDloc: spatial working memory task (used to define MD fROIs)
- ScratchJr: ScratchJr program comprehension task

**fROI data column names:**
- ROI: region of interest (for number to name conversion, see analysis files)
- Subject: participant ID
- Effect: condition of interest
- LocalizerSize: size of the fROI (top 10% of the voxels most responsive to the localizer contrast within a given parcel)
- EffectSize: strength of response to the effect of interest 
