# LLM based Gene expression analysis

This repo contains a project of analyzing transcriptome and proteome data while utilizing LLMs.


## Introduction
Gene expression and proteomics are commonly used to get an understanding of the physiological state of organisms and the impact of various treatments and stresses.
Interpretation of the results of these assays is difficult, and often simplistic.

Our understanding of the functions of genes is limited, there is a large portion of the genomes (~40% in cyanobacteria) whose function has not yet been characterized, and therefore their function is unknown and their impact on physiology not known.

For genes with well identified finction, the gene may be part of multiple pipelines, making difficult to pin point the pathway impacted. 
Gene regulation is complex, some genes may promote or inhibit other genes, rrna transcript may or may not be translated into proteins, and indeed, there is low correlation between the Proteome and transcriptome.
Often the assays report mixed results for a given pathway, with some genes upregulated and others downregulated.

Finally, even when the physiological effect is clear, interpretation may be challenging. For example, if bacteria under nitrogen stress increases expression of urea uptake pathways, does that mean that it is switching to utilizing urea, or does it mean that it is so nitrogen starved that it activates nitrogen uptake mechanisms in a desparate attempt to uptake any possible compound even if it is not there.

Some of the challenges in interpreting gene expression assays include:
1. The wealth of knowledge in the field. Genetic research has been conducted for several decades and numerous studies explored the physiological and genomic aspects of individual genes and pathways. It is imposssible for an academic researcher to keep up with the available research. Especially as there are thoughsends of genes and tens of pathways to keep track of.
   1.a. Given the large quantities of available research, one should also be careful to give priority to high quality research and to disregard research that may be of dubious origins.
2. Similarly, interpretation in light of published research. It would be benefitial to take into account previous studies where proteome/transriptome assays were run and the expression patterns observed there. Some form of meta-analysis may help identify which of the expression patterns are significant and which may be part of background noise or results from other factors.
3. Critical thinking: it is easy to fall back into descriptive interpretation. As in, this pathway is up and this is down. But it is harder to interpret the results in light of physiology and even harder to include multiple hypothesis on the interpretation of the results.


4. <to include???> Often these studies are performed on other organisms (especially when working on non-model organisms), and the results may not be applicable to the bacteria studied. 


## Goal

The goal of this project is to explore different AI based techniques to aid in the analysis of gene expression and protein exptression patterns.

## The use case
As a use case, we will analyze a study of the interaction between the marine cyanobacteria *Prochlorococcus* MED4 and the marine heterotrophic bacteria *Alteromonas*. *Prochlorococcus* grows poorly under nitrogen limited condition but thrives in the presence of the helper bacteria *Alteromonas*. *Alteromonas* also aids in *Prochlorococcus* survival in other stressful conditions, such as survival in the dark, resistance to phages and dealing with phosphorose limitation. It has been shown that *Alteromonas* helps by eliviating stress from buildup of ROS (reactive oxygen species) waste product. Our hypothesis is that some of the interaction is based on nutrient exchange between the strains.

For that purpose a coculture of *Prochlorococcus* and *Alteromonas* was grown in batch triplicates under nitrogen limited condition for 90 days (3 months). RNASEQ and proteome were conducted during exponential growth, decline and long-term survival on days 30, 60 and 90. As controls, both strains were also grown and sampled axenically in monocultures.
Both proteomes and transcriptome were analyzed using best-practices pipelines, yielding a table of expression fold changes vs. the first timepoint (exponential growth) and vs. the controls.
In addition, we are imploying genome scale models (flux based analysis - FBA) to analyze the metabolic mechanisms, potential nutrient exchanges, and to interpret the expression patterns.

## Questions 

The goal of this study is to use AI to answer the following questions:
1. What is known about each gene and pathway with a focus on differentially expressed genes/pathways.
   - Does this gene have a possible role in nutrient exchange?
   - Does this gene have a possible role in microbial interaction?
   - Does this gene have a possible role in stress response?

2. What is the meaning of the observed expression patterns?
   - Can we deduce physiological state?
   - Can we identify putative nutrient exchanges?
   
3. Critical analysis: what are the weak points in the analysis, what needs to be addressed. Are there additional assays/experiments that we can run to address these.


   
   
# Previous text to be changed

This is a project of writing a scientific review paper through LLM.
There are multiple versions, each using a more sophisticated approach.


# increasingly sophisticated methods to generate the review

1. By a prompt 
   a. Simple prompt
   b. Prompt engineering (system prompt), one-shot prompting, chain-of-thought, ...
   
2. by a series of prompts - break down into smaller tasks (outline, research section, write section, verify, integrate, polish)

3. add websearch tool

