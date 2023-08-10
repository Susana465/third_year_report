# Computer models of CaMKII/NMDAR interactions

## Software used: MCell and Bionetgen

Talk about visualization and summarise properties.


## Model description

I have constructed the models at different scales to validate CaMKII interactions with other molecules like calmodulin and NMDARs, at increasing levels of complexity. First I re-created a model of CaMKII as a monomer that was previously completed in 2017. The model created uses cBNGL and represents CaMKII as monomers to serve as a proof of concept as well as a starting validation point, as dynamics of this model were previously shown to be within biologically accurate limits. Secondly, I created a model of CaMKII as a hexamer since modelling this molecule as a dodecamer gave rise to a combinatorial explosion due to the high number of possible states and the network of interactions generated. This is currently in the works of being resolved as I run the model using the network-free simulation using MCell. We will then be able to model CaMKII as a dodecamer. Finally, I aim to validate this work against a model from Ordyan et al., 2020, where they successfully modelled CaMKII as a twelve subunit holoenzyme using BioNetGen simulations. 

2.2.1.	Model of CaMKII monomers
I began the model of CaMKII monomers as described in the 2017 model I created using MCell and CellBlender. At the time, MCell did not allow for molecules to be modelled as multi-complexes. Thus, for example, one phosphorylated CaMKII molecule in the model was just a single subunit phosphorylated –not twelve phosphorylated subunits. This model includes Ca2+ binding rates to CaM, CaM binding rates to monomeric CaMKII, and phosphorylation rates of active CaMKII monomers by one another, all depending on how many Ca2+ ions are bound to the CaM molecules involved. CaMKII dephosphorylation by PP1 is modelled, as well as binding interactions of CaMKII with NMDARs. In order to replicate and validate the results obtained from the CaMKII monomer in 2017, I re-wrote all reactions into a cBNGL model using the same parameters used originally. we define a volume previously modelled of 0.5μm3, which is within ranges of spine volume of 0.004 to 0.6 μm3 in hippocampal CA1 neurons (Harris and Stevens, 1989). Using cBNGL, I can specify the above mentioned 3D volume, with a 2D surface compartment acting as the cell membrane, where NMDARs can diffuse. Inside the cell volume, all of the interacting molecules are released as per table 1.

### Model of CaMKII hexamers
As explained in the introduction of this report, CaMKII is a dodecameric molecule, meaning it’s composed of twelve subunits. Ideally, I would like to model CaMKII as a dodecamer since this would allow us to infer more accurately any emergent behaviour of the protein. However, due to combinatorial explosion, running a CaMKII as a dodecamer takes a really long time: 6+ hours without finalising run time, using a cBNG, SSA simulation. These simulations include only calcium binding to CaM, and CaM binding to CaMKII as a dodecamer, without further reactions added to avoid further complexity. The machine being used for these simulations is a x64-based laptop, with specs: 11th Gen Intel® Core™ i5-1145G7@2.60GHz, 1498Mhz, 4Core(s), 8 Logical Processors. SSA simulations generate a full network of reactions and causes the simulation to slow down considerably. At the moment, compartmental BNGL does not allow for NFsim simulations to be ran. This can be overcome by running the model with MCell as it provides a network free simulation capability. An alternative so far has also been to run the model with CaMKII as a hexamer. However, it still causes combinatorial explosion when generating network reactions. This should be resolved by running the model as a network free simulation in MCell.

### Model of CaMKII as a dodecamer

## Model development and validation
Following from what I did last year, show results, copy what's on github https://github.com/Susana465/CaMKII_hexa_bgnl_to_mcell

Develop the description of how the models work – model description and results. Biologist friendly description of the model. 

talk about roustness, generalisable, environments

Write abstract for each chapter, then merge them altogether.  

### A reproducible model