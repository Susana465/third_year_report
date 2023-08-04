# What is my PhD research question?
The biological question that started this PhD was how do Calcium/calmodulin-dependent protein kinase II (CaMKII) and N-methyl-D-aspartate receptor (NMDARs) in the postsynaptic neuron interact and enable the processes of learning and memory?

When studying learning and memory at the molecular level, in health and disease, it has been shown that NMDAR and CaMKII together with their interactions with other proteins within neuronal spines, can influence their shape and size [@fink2002MolecularMechanismsCaMKII]. Long-term modifications of synaptic strength, such as LTD (Long Term Depression) and LTP (Long Term Potentiation) involve diverse chemical pathways and have been the primary mechanisms used to study the molecular basis of learning and memory [@blundon2008DissectingComponentsLongTerm]. So what exactly is happening at the cellular and molecular level during memory formation? 

These are the biological prompts that I look at when creating 3D models of the molecules in question. I use mainly [mcell](https://mcell.org/) and python to do so.

**TLDR: I create 3D models which simulate interactions between CaMKII and NMDAR in the postsynaptic neuron, to understand how memory works in animal brains.**

![Alt text](image.png)

|Overview of this PhD| 
|:---------|
|**Aims of this PhD:**| 
| - Explain how specific molecules work together during memory.<br> - Develop new ways of 3D modelling to look at time and space dynamics of molecular interactions.|
|**Type of data used:**| 
| - Kinetic rates of molecule interactions, molecular concentrations collected frm literature and databases. <br> - Numbers obtained from either wet-pab experiments or mathematically calculated.|
|**Methods:**| 
| - Models written with standardised open source languages: python, bionetgen Language. <br> - Numbers obtained from either wet-pab experiments or mathematically calculated. <br> - Run locally or in cluster if simulations are more computationally expensive. |
|**Applications and significance:**| 
| - Other researchers can build from these models to create further predictions for potential pharmacological applications. <br> - The molecules I look at have been shown to be dysfunctional in Alzheimer's and Huntington's disease. |

## Why use Computational Modelling to study biological systems?

As an overview, some of the main reasons for using modelling are:

1.	Biological systems are complex and multiscale, models can help us to integrate experimental data, facilitating theoretical hypotheses, and addressing what if questions.

2.	Models aim to make clear the current state of knowledge regarding a particular system, by attempting to be precise about the elements involved and the interactions between them. Doing this can be an effective way to highlight gaps in understanding.

3.	Related to point one, models then serve to combine knowledge from different published research, and make biological predictions which can then serve as hypothesis to be tested empirically by experimentalists.

4.	Computer-simulated experiments can help guide the wet-lab process by narrowing the experimental search space, enabling more cost, time-effective and waste-free research, as well as more ethical research too as we reduce animal suffering through reduction of animal research.

But as time went by, I realised more and more how important looking at the ethics of the research that we do is. How biased science actually is, and how we continue to carry these if we don't look at them in the face. Additionally, how much research time and money is wasted by doing experiments which cannot be reproduced or replicated later on. Hence my emphasis on these topics. 

I have made it a purpose of this PhD project to highlight and talk about some of the things I care most in research: making it transparent, inclusive, and accessible.