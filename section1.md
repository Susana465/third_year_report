# Ethics and Reproducibility emphasis in this PhD and why it matters

The work I have carried out through this PhD so far, has had a very heavy focus on thinking about Ethics and Reproducibility as an embedded part of my research, not as a last minute add-on. This is because I truly believe it is of utmost importance that there is a shift in how we proceed with science. A science that currently works under a capitalistic mechanism which advocates for mass production of positivist, fast research.

We are currently living in a period where many have started to talk about a "Reproducibility Crisis" [@baker2016500ScientistsLift], [@treves2022Best], where we find more and more, as work is done into reproducing previous published results without success, that there is an increasing awareness of this issue. The reproducibility or replicability crisis (more on these terms below) undermines the credibility of theories scientific knowledge, as an essential part of the scientific part of the scientific method is to be able to repeat and reproduce or falsify empirical results and theories. The issues encountered around reproducibility vary, of course, depending on the field. In this report I focus more, although not solely, on the computational modelling of systems biology aspect of reproducibility.

## Defining reproducibility vs replicability
There is a long history of these terms being used interchangeably, or their meanings being swapped depending on the field of study [@claerbout1992ElectronicDocumentsGive], [@ivie2018ReproducibilityScientificComputing], [@plesser2018ReproducibilityVsReplicability]. For example, a review on the usage of reproducible/replicable meanings [@barba2018TerminologiesReproducibleResearch] showed that most papers and disciplines use the terminology as defined by Claerbout and Karrenbach, whereas microbiology, immunology and computer science tend to follow the Associtation for Computing Machinery use of reproducibility and replication given by Ivie and Thain, 2018. In political science and economics literature, both terms are used interchangeably. So this quickly shows how having a lack of agreement on such definitions can add even more confusion to the mix. 
Here, we use the definition used by [@turingwaycommunity2019TuringWayHandbook], where reproducible research is understood as work that can be independently recreated from the same data and the same code that the original team used. Reproducible is distinct from replicable, robust and generalisable as described in the table below (@fig-rep_table).

![How the Turing Way defines reproducible research.](reproducibility_terms.jpg){#fig-rep_table}

The different dimensions of reproducible research described in the matrix above have the following definitions, taken from the Turing Way booklet:

- **Reproducible**: A result is reproducible when the *same* analysis steps performed on the *same* dataset consistently produces the *same* answer.

- **Replicable**: A result is replicable when the *same* analysis performed on *different* datasets produces qualitatively similar answers.

- **Robust**: A result is robust when the *same* dataset is subjected to *different* analysis workflows to answer the *same* research question (for example one pipeline written in R and another written in Python) and a qualitatively similar or identical answer is produced. Robust results show that the work is not dependent on the specificities of the programming language chosen to perform the analysis.

- **Generalisable**: Combining replicable and robust findings allow us to form generalisable results. Note that running an analysis on a different software implementation and with a different dataset does not provide generalised results. There will be many more steps to know how well the work applies to all the different aspects of the research question. Generalisation is an important step towards understanding that the result is not dependent on a particular dataset nor a particular version of the analysis pipeline.

## Ethics and philosophy of Computational Neuroscience
When reading articles or interacting with academics in science in general, and especially in the field of Computational Modelling of systems biology, Ethics tends to be taken mostly into account if human animal data is directly involved in the research, then mentioned briefly if non-human animals are involved, and it becomes more difficult to find a discussion on ethical matters if none of these are involved at all, for example, if data discussed involves a protein removed from who/where it came from. This scientific reductionism, where complex interactions and sum of their constituent parts are "reduced" to smaller sections in order to potentially make it easier to study, has been discussed to have a variety of problems (and advantages to a degree) [REFERENCE]. One such problem is that we forget to ask where has the data **really** come from. The data we use, for example when creating computer models, has come from animals like mice or rabbits, yet in order to get a successful publication we find ourselves making big statements of how this model could potentially be useful to aid in how Alzheimers works in humans. 

issues with racism

issues with sexism

intersectionality of fields and merging of philosophical discussions may add a bit of time to the research but can very much enrich a fuller and more complex understanding of the shortcomings of our research and how to do better moving forward. 


## Reproducibility issues in the field 
During my PhD work so far, one aspect of the research that has come with quite a lot of struggle is to find accurate parametrization of values for protein dynamics. This is a known issue for most of us who create computational models of biological systems. @wieber2020ModelsParameterizationSoftware call it an “epistemic opacity” when talking about lack of clarity in Computational Chemistry, where this opacity is entangled in methods and software alike. 

This of course leads to reproducibility issues, and as this unfolds, it becomes clear that the “untrustworthiness” of research is also an issue for many other researchers. In fact, a survey of 1576 scientists published in Nature [@baker2016500ScientistsLift] reported that over 70% of the participants failed to reproduce others’ experiments and over 50% failed to reproduce their own results. 

Interestingly, @tiwari2021ReproducibilitySystemsBiology, assessed the reproducibility of 455 mathematical models in systems biology and found that about 50% of published models were not reproducible either due to incorrect or missing information in the manuscript.

Making an effort into creating research that is reproducible can help to avoid wasting resources, including having to repeat the same experiment questions again and again because results from one study could not be reproduced or replicated by other groups. 

A big step into making sure other people can reproduce your work in the field of computer models is to share your code. However, stopping there is almost like doing nothing as the code needs to be well documented and embedded in environments if necessary to run the code with its required dependencies.