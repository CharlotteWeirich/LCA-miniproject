# Moving Beyond the Bechdel Test
##### Charlotte Weirich, Emma Valisova (note: legal name Alex Valisu)

#### GitHub Project and Process Explanation
1. (Emma) downloading subtitles from the internet: **subtitle-extraction.py script, subtitles folder** (legacy)
3. (mainly Charlotte) uploading subtitles to WebAnno and manually annotating speakers: **available to view on WebAnno** (legacy)
4. (Emma) downloading HTML transcripts from the internet: **html-extraction.py script, html_source folder**
5. (Emma) automatically separating transcripts by scenes and converting the format to fit automatic coreference resolution: **description-extraction-demo.py script, scenes folder**
6. (Charlotte) automatic coreference resolution: **local, scenes/\[show\]/xml folder**
7. (Charlotte) conversion to WebAnno tsv format: **xml-to-webanno-tsv.py script, scenes/\[show\]/tsv folder**
8. (Emma) automatically extracting the number of tokens spoken by each character, manually annotating their gender, and automatically counting the number of tokens spoken by each gender: **description-extraction-demo.py script, scenes/speakers.txt (automatic), scenes/speakers-labelled.txt (manual), gender-distribution.py script, scenes/gender-distribution.txt**
9. (Emma) writing the README file: **README.md**
10. (NA) creating the presentation
