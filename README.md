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


## Methods
### Prior knowledge on Genes/Pathways
Published research will be summarized via a combination of LLMs and literature search.

We will build a series of solutions, increasingly sophisticated, to perform this task.

The output will be a database containing all genes and pathways in the Prochlorococcus MED4 and Alteromonas HOT1A3, including:
- a summary of published research
- sections on possible roles related to the research questions (nutrient exchange, microbial interaction, stress response)

### Building the Gene database
Methods we may use: 
1. Select LLM models to use (frontier, open source)
2. Prompt engineering (simple prompt, structured prompt, chain-of-thought, one-shot, multi-shot, series of prompts)
3. Inject published papers ("manually" add to prompt, tools (web search, crossref verification of references, load paper text), RAG
4. Agents

### Assessing quality of the gene database
Quality of the results will be validated by a mixture of automated and manual techniques. 
1. The resulting database needs to be based on published research, avoiding hallucinations. That is, references should correctly cite relevant published papers (papers should be real and relevant papers should be referenced), the content needs to reflect the actual content of the referenced research.
2. Results should be in the correct level of details. Highlight known research on Prochlorococcus, cyanobacteria, and alteromonas and so forth. Specifying the specific strains where applicable. Details should be sufficient for analyzing omics data but not overly detailed (for example, no need to specify Km). 
3. Results should be structured in a way that is amenable for automated processing. For example, broken into sections, labeled, etc. Distinguish results from speculative discussion.

Here is a list of instructions created by Claude. The generated DB should follow them:
- Follow academic writing conventions and maintain formal scientific tone
- Cite relevant literature (using [Author, Year] format)
- Structure content logically with clear section organization
- Balance technical detail with accessibility for a scientific audience
- Focus on empirical evidence and current understanding
- Acknowledge knowledge gaps and areas of uncertainty
- Use precise scientific terminology while defining specialized terms
- Avoid speculation beyond what is supported by published research

#### Quality checks:
1. All references are valid and in the correct format. Check using CROSSREF API.
2. The content reflects actual findings from the research. (a) Ask the LLM to provide supporting quotes and check that these appear in the cited paper. (b) create a verification prompt that takes the generated database entry and the publication full text and verifies that claims are substantiated.
3. All relevant references are cited - manually review valid references from all entries and from web search to create a list of references that should be cited - compare LLM references to this target list.
4. Create a reviewer LLM to verify correct format, tone, and level of details.
5. manually review entries for select genes. Recruit experts to review a few genes each.
6. Develop a simple test to check for correct structure. Use sentiment analysis to check the sections are labelled correctly.
7. Use LLM reviewer to rank the results. either as is or by comparing to different database entries for the same gene.

This quality assessment will be used to assess the progress as more and more advanced techniques are used and will be used to select the gene database to be used for the omics research.



### Analyze Observed Expression patterns


The second phase of the research includes analysis of omics results.
We have sequenced transcriptome and proteome of *Prochlorococcus* in coculture with *Alteromonas* while in long-term nitrogen starvation. The goal of this phase it to study the condition of the strains under these stresses. Including: physiological state, stress responses, coculture impacts and possible nutrient exchanges and shifts to alternate N and C sources.


Questions and analysis methods:

1. which of the changes in expression pattern is related to the experiment, and what is their physiological interpretation. To answer this question we will create a table of expression patterns in published RNASEQ and proteome studies of *Prochlorococcus* and *Alteromonas* as well as related strains.
   a. Open: how to build this table? Option 1: based on NCBI bioprojects repository (probably out of scope). Option 2: Download supp info from papers. Requires extraction, processing, mapping to genes of the strains used in the experiment.
   b. Open: How to compare current experimental results. Option 1: statistical check? Option 2: Network approach. Option 3: Build AI model (probably will not have sufficient data).
   
2. What is the conditions of the strains in the experiment? This question will be checked by identifying  upregulated/downregulated genes/proteins and querying the gene DB to assess their potential impact on the research question. 
   a. Note that we also have additional info such as: GO terms, KOs. And additional analysis methods like FBA and pathway enrichment.
   b. this stage could be performed by LLM prompt with validation performed manually and by LLM.
   
   


   
# Previous text to be changed


increasingly sophisticated methods to generate the review

1. By a prompt 
   a. Simple prompt
   b. Prompt engineering (system prompt), one-shot prompting, chain-of-thought, ...
   
2. by a series of prompts - break down into smaller tasks (outline, research section, write section, verify, integrate, polish)

3. add websearch tool

