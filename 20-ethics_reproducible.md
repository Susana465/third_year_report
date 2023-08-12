---
title: "Ethics and Reproducibility emphasis in this PhD and why it matters"
---
The work I have carried out through this PhD so far, has had a very heavy focus on thinking about Ethics and Reproducibility as an embedded part of my research, not as a last minute add-on. This is because I truly believe it is of utmost importance that there is a shift in how we proceed with science. A science that currently works under a capitalistic mechanism which advocates for mass production of positivist, fast research that historically mostly only benefits a few (usually cis-male, white, able-bodied individuals [^1]) [@webb2022Addressing], [@diogo2023Not], [@branch2022Discussions]. 

[^1]: This bias towards benefiting cis-male, white, able-bodied people does not mean they do not suffer, and does not negate the existence of the issues they may experience too. For more information on how society is biased in a way that provides privileges in a certain order/hierarchy, and how to handle it, please have a look at [@diangelo2018White],or [@delgado2022Owning].  

## Science for the profit of whom?

There is a historical heritage of monetary incentivization to move towards drug discovery and the profit that comes from this, and how this has played a key role in biasing research towards drug discovery to "fix" individuals, without their wellbeing being necessarily at the forefront. @dosi2023Big provide an  long term review of Big Pharma and monopoly capitalism, but there are many examples of how companies move scientific research in a way that is driven by economic profit; and how there's a constant pull to publish more and publish first. It is not the point of this report to go in depth into how or why this has happened, but I can offer you a few good places to start, if you are interested. 

The book *Warp and Weft* by @fennenWarpWeft, with a focus on psychiatry and neuroscience, looks at some of these sciences' history and examines the ways they have been, and continue to be used as a colonial force. Enforcing a global North science on to the world, as well as describing how many times this enforcement has been led by economic profit for only a few. One good example it cross-references is the "The Mega-Marketing of Depression in Japan" by GlaxoSmithKline, originally spoken about in the book *Crazy Like Us* by @watters2010Crazy, which is another good place to find examples of this kind.

### Historical oppressive biases:
It is because of these histories, that I want to attend to them in the work that I do. If we ignore thinking about the ethics, philosophy and history of the research that we do, we may forget where certain ontologies and basis of knowledge come from. Therefore continuing to pretend that these topics are not necessary to think about, whilst a privileged group continues to perpetuate oppressive biases towards historically marginalized groups. 

In a presentation I gave in 2022, I give a few examples of biases that continue to happen in science, including examples of racism, sexism, ableism and speciesism [@garcia2022Thinking]. A good example of embedded biases in science is given by @branch2022Discussions as they eloquently articulate how a desire to quantify and establish hierarchies among organisms was not purely for scientific interest, but that there is extensive evidence in the fact that the roots of evolutionary biology, which serves as a baseline for many other disciplines like neuroscience, are steeped in histories of white-supremacism, eugenics,and scientific racism. They discuss the definition of the “Not-So-Fit”, and how this limits the diverse thought and investigative potential in biology. This is of importance for my PhD, as I use hierarchies and models of biology that are based on a historical context of how science has reached it's current status of knowledge. 

## Slowing down...
As a response to a fast-paced, profit-driven science, a few Slow Science Manifestos have been published, notably *Another Science is Possible: A Manifesto for Slow Science* by @stengers2018Another maintains that in order to make higher quality education and science, it needs to serve society as a whole, and calls, among other things, for an "accountability in the knowledge society versus profitability in the knowledge economy". 

Moreover, as long as we continue to create fast research without regard for reproducibility, we will continue to experience what some now call a "Reproducibility Crisis" [@baker2016500ScientistsLift], [@treves2022Best], where we find that, as work is done into trying to reproduce previous published results, this is not possible. The reproducibility or replicability crisis (more on these terms [below](#defining-reproducibility-vs-replicability)) undermines the credibility of theories scientific knowledge; as an essential part of the scientific part of the scientific method is to be able to repeat and reproduce or falsify empirical results and theories. 

There is an argument to be made that making research more reproducible and ethical takes more time. And it does. This is precisely why slowing down can help in creating higher quality research that serves all in society.


## Importance of reproducibility
During my PhD work so far, one aspect of the research that has come with quite a lot of struggle is to find accurate parametrization of values for protein dynamics. This is a known issue for most of us who create computational models of biological systems. @wieber2020ModelsParameterizationSoftware call it an “epistemic opacity” when talking about lack of clarity in Computational Chemistry, where this opacity is entangled in methods and software alike. 

This of course leads to reproducibility issues, and as this unfolds, it becomes clear that the “untrustworthiness” of research is also an issue for many other researchers. In fact, a survey of 1576 scientists published in Nature [@baker2016500ScientistsLift] reported that over 70% of the participants failed to reproduce others’ experiments and over 50% failed to reproduce their own results. 

Interestingly, @tiwari2021ReproducibilitySystemsBiology, assessed the reproducibility of 455 mathematical models in systems biology and found that about 50% of published models were not reproducible either due to incorrect or missing information in the manuscript.

Making an effort into creating research that is reproducible can help to avoid wasting resources, including having to repeat the same experiment questions again and again because results from one study could not be reproduced or replicated by other groups. 

### Defining reproducibility vs replicability
These terms have been used interchangeably for a while, or their meanings being swapped depending on the field of study @claerbout1992ElectronicDocumentsGive], [@ivie2018ReproducibilityScientificComputing], [@plesser2018ReproducibilityVsReplicability].

Here, we use the definition used by [@turingwaycommunity2019TuringWayHandbook], where reproducible research is understood as work that can be independently recreated from the same data and the same code that the original team used. Reproducible is distinct from replicable, robust and generalisable as described in the table below (@fig-rep_table).

![How the Turing Way defines reproducible research.](reproducibility_terms.jpg){#fig-rep_table}

The different dimensions of reproducible research described in the matrix above have the following definitions, taken from the Turing Way booklet:

- **Reproducible**: A result is reproducible when the *same* analysis steps performed on the *same* dataset consistently produces the *same* answer.

- **Replicable**: A result is replicable when the *same* analysis performed on *different* datasets produces qualitatively similar answers.

- **Robust**: A result is robust when the *same* dataset is subjected to *different* analysis workflows to answer the *same* research question (for example one pipeline written in R and another written in Python) and a qualitatively similar or identical answer is produced. Robust results show that the work is not dependent on the specificities of the programming language chosen to perform the analysis.

- **Generalisable**: Combining replicable and robust findings allow us to form generalisable results. Note that running an analysis on a different software implementation and with a different dataset does not provide generalised results. There will be many more steps to know how well the work applies to all the different aspects of the research question. Generalisation is an important step towards understanding that the result is not dependent on a particular dataset nor a particular version of the analysis pipeline.

## Ethics and Reproducibility go together

Entangled with reproducibility, is thinking about ethics. Because no matter how efficient and reproducible an outcome may be, if it's harming a group of individuals, how good really is this research? Likewise, if a project has taken into account and described potential bias and harms of their data, but then does not share enough material for their research to be reproduced by others, are we really advancing?

Thinking about reproducibility can in turn help to think how you will share your data, as well as where your own data has come from. Hence, reaching an increased awareness of how your data was sourced and its ethics and potential biases. In order to showcase how I see these topics as being interwoven, I presented a poster titled "Bias and reproducibility in a computational neurobiology PhD's journey" (@fig-posterPhDjourney) at the International Conference on Systems Biology (ICSB) in October 2022. On the left side of the poster, I share how to think about the ethics and bias of your research, and on the right side I provide tools for reproducibility. I also wrote about this more in depth in this GitHub repository [here](https://github.com/Susana465/Bias-and-Reproducibility-Poster).

I created this poster because I wanted to showcase, at a conference full of scientists at different stages of their research, how I take into account bias an reproducibility in my research, and how they could too.

[![Poster about bias and reproducibility, showing research cycle as a journey which starts with design, then data collection, data analysis and final reporting, and compares this through images to growing an apple tree, collecting the apples and then selling them.](20221006_poster_phd_journey.jpg){#fig-posterPhDjourney fig-pos="h"}](https://github.com/Susana465/Bias-and-Reproducibility-Poster/blob/main/20221006_poster_phd_journey.jpg)


Working with ethics, philosophy, reproducibility and an openness to discuss the wider context of where our research rests, may add a bit of time to the research timeline, but can very much enrich a fuller and more complex understanding of the shortcomings of our research and how to do better moving forward. 

Following on the idea that scientists are great at selling the gains in efficiency and accuracy of their work, but less well-practiced in thinking about the ethical implications of our work, I present a framework developed to think about dangers or risks involved with your data and research: Data Hazard Labels, see following @sec-data-hazards.
