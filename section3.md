# Data Hazards

Following on the idea that scientists are great at selling the gains in efficiency and accuracy of their work, but less well-practiced in thinking about the ethical implications of our work, I present a framework developed to think about "Data Hazards". The ethical implications that ought to be considered go beyond most ethics Institutional Review Boards, to questions about the wider societal impact of data science and algorithms work. This is where a project like the [Data Hazards Project](https://datahazards.com/) comes in handy. Data Hazards is a project made to help us in thinking about worst-case scenarios and ways to mitigate these. 

The Data Hazards Project has created a community-developed shared vocabulary of data science risks. The vocabulary presents data ethics concepts in the form of [Data Hazard Labels](https://datahazards.com/contents/data-hazards.html), similarly to chemical hazard labels. This project exists to facilitate material for interdisciplinary discussions and self-reflection about all kinds of data ethics risks.

## Example label: high environmental cost

<center><img src="https://datahazards.com/_images/environment.png"  width="200" height=""></center>

### Description

This hazard is appropriate where methodologies are energy-hungry, data-hungry (requiring more and more computation), or require special hardware that require rare materials.

### Examples

 - Example 1: Running computer models in super computers requires vast energy usage.

### Safety Precautions
 - Consider in what circumstances it is worthwhile to use this type of methodology.
   - To communicate the scale of the issue to other stakeholders, you may want to [convert units of energy into more relatable units]().
   - Find out [if your cloud provider uses renewable energy]().
   - Consider profiling your code, and rewriting it to use less energy.
   
- Consider future work that would reduce the need to use increasingly more resources.

## Application example into Research life-cycle
To help visualize where and when Data Hazards can be used in your workflow, below is an example assuming four main stages of workflow: design, data collection, data analysis and reporting. This is a generalised example, but something like this is what it looks like for me when I work on my PhD. 


### Design:
 - Are you using data? Then doing some reflection on [identity and positionality](https://the-turing-way.netlify.app/ethical-research/self-reflection/sr-positionality.html?highlight=bias) could help you think of what Data Hazards labels you might encounter as you design your project, for example ["ranks of classifies people hazard"](https://datahazards.com/contents/hazards/ranks-classifies.html) or ["risk to privacy"](https://datahazards.com/contents/hazards/risk-to-privacy.html) could apply at this stage.
 - In this part of the workflow, you might want to prepare to avoid certain Data Hazards if you can, and if you can't avoid them because of where your data has come from, you may want to acknowledge this. For example, if you a [sensitive data project](https://the-turing-way.netlify.app/project-design/sdp.html), what Data Hazard labels will apply, and/or what can you do to design your project in a way that avoids certain harms?
 
### Data Collection and Analysis:
 - As you are collecting and analyzing your data, you might want to iteratively think of the potential Data Hazards that exist in the information you are collecting. To then apply the labels as you perform the next step of the process: reporting.

### Reporting:
 - When reporting your results, you can think of applying and reporting the Data Hazard labels that are relevant for your project; examples of how others have done this can be found here [link to self reflection and case studie(s)]. Labeling your project with Data Hazards should also include considerations of mitigations to these risks. This would then be helpful for people who see your outputs in the future. They can be aware of potential risks as they proceed with the project, and continue to think of solutions to any issues related to the research topic.

## Application of Data Hazards into my PhD project:
In order to showcase how Data Hazards can be reflected upon during a PhD, I have been implementing thinking about the vocabulary they provide into my own work.

### Poster Visual: Bias and reproducibility in a computational neurobiology PhD's journey
In relation to this workflow, back in October 2022 I presented a poster at ICSB - International Conference on Systems Biology and was selected for a flash talk to showcase my work. I created this poster because I wanted to showcase, at a conference full of scientists at different stages of their research, how I take into account bias an reproducibility in my research.

As a preview, you can see it below, please click on it if you'd like to view a bigger version of this image. 

Find GitHub repository [here](https://github.com/Susana465/Bias-and-Reproducibility-Poster).

[![Poster about bias and reproducibility, showing research cycle as a journey which starts with design, then data collection, data analysis and final reporting, and compares this through images to growing an apple tree, collecting the apples and then selling them.][1]][2]

[1]: ./20221006_poster_phd_journey.jpg

[2]: https://github.com/Susana465/Bias-and-Reproducibility-Poster/blob/main/20221006_poster_phd_journey.jpg

{{< pagebreak >}}