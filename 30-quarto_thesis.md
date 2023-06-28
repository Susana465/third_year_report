# Why the emphasis on reproducibility?

The term "reproducible" here uses the Turing Way definition of reproducibility: *"A result is reproducible when the **same** analysis steps performed on the **same** dataset consistently produces the **same** answer."*

During my PhD work so far, one aspect of the research that has come with quite a lot of struggle is to find accurate parametrization of values for protein dynamics. This is a known issue for most of us who create computational models of biological systems. @wieber2020ModelsParameterizationSoftware call it an “epistemic opacity” when talking about lack of clarity in Computational Chemistry, where this opacity is entangled in methods and software alike. 

This of course leads to reproducibility issues, and as this unfolds, it becomes clear that the “untrustworthiness” of research is also an issue for many other researchers. In fact, a survey of 1576 scientists published in Nature [@baker2016500ScientistsLift] reported that over 70% of the participants failed to reproduce others’ experiments and over 50% failed to reproduce their own results. 

Interestingly, @tiwari2021ReproducibilitySystemsBiology, assessed the reproducibility of 455 mathematical models in systems biology and found that about 50% of published models were not reproducible either due to incorrect or missing information in the manuscript.

Making an effort into creating research that is reproducible can help to avoid wasting resources, including having to repeat the same experiment questions again and again because results from one study could not be reproduced or replicated by other groups. 

A big step into making sure other people can reproduce your work in the field of computer models is to share your code. However, stopping there is almost like doing nothing as the code needs to be well documented and embedded in environments if necessary to run the code with its required dependencies.

(talk about [environments](https://nsls-ii.github.io/scientific-python-cookiecutter/environments.html) too?)

## Reproducible model:

So, in order to make my work reproducible, I started by creating some documentation and code which can be run in someone else's machine and if they can get the same output, we have succeeded!

The good news is that we did succeed in this mission, both Nico Romano and David Sterratt were able to run the code in their own machines and make it work using different operating systems.

The model they ran was a hexamer version of the CaMKII model I am working on, and can be found here:

[CaMKII_hexa_bgnl_to_mcell](https://github.com/Susana465/CaMKII_hexa_bgnl_to_mcell)

(currently private, is it ok to make public?) (not sure what else to add here? should I add images of the models run? but its the same as last year...)

## Quarto:

Quarto® is an open-source scientific and technical publishing system built on [Pandoc](https://pandoc.org/). It allows you to weave together narrative text and code to produce elegantly formatted output as documents, web pages, blog posts, books and more. 

Quarto is at its core multi-language and multi-engine (supporting Knitr, Jupyter, and Observable today and potentially other engines in the future); where you can have all your code and narrative text in one. For a full breakdown and FAQs of how Quarto works, you can have a look [here](https://quarto.org/docs/faq/rmarkdown.html).

The good thing for me personally, is that, thanks to Quarto, I can write my thesis chapters using [markdown](https://www.markdownguide.org/getting-started/) (which is a lot more intuitive than LaTeX, in my opinion). Moreover, I can keep track of version control of each file and allows for helpful traceability of materials included in the document I am writing; which in itself has many benefits as it immensely helps to be able to go back to a previous version where everything was working before I broke the code (yet again).

Part of my work includes work which runs with different python scripts, and using Quarto means that I can embed python code if needed to explain how certain functionalities of the models work. It also allows for code using R to run within a Quarto document, as well as jupyter notebooks too!