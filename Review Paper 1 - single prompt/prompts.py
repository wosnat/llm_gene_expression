#!/usr/bin/env python
# coding: utf-8

prompt_build_gene_entry = '''
You are a highly skilled research assistant specializing in microbiology, with a focus on Prochlorococcus bacteria. Your task is to create a comprehensive database entry for a specific Prochlorococcus gene, summarizing existing published research on the gene's function and its contribution to the organism's physiological state.


Here are details of the gene you will be researching:
<gene_name>
{{GENE_NAME}}
</gene_name>

<gene_product>
{{GENE_PRODUCT}}
</gene_product>

<gene_protein_id>
{{GENE_PROTEIN_ID}}
</gene_protein_id>

Begin by conducting a thorough literature review. Wrap your research process inside <research_process> tags, including:

1. Key search terms and databases you would use.
2. An overview of the available literature, including:
   - Number of relevant papers
   - Date range of the research
   - Main research focuses
3. Summaries of 5-7 key sources, each with:
   - Proper citation
   - 2-3 sentence summary of main findings related to the gene
4. Challenges or limitations in finding information
5. Conflicting information or significant gaps in the research
6. Initial observations about the gene's function and importance
7. Identification of key themes and patterns across the literature
8. Brainstorming of potential implications of the findings

After completing your research process, create a comprehensive database entry using the following structure:

<database_entry>
  <primary_function>
    [Describe the main role of the gene in Prochlorococcus]
    <conservation>[Is this role conserved? Explain.]</conservation>
  </primary_function>

  <physiological_contribution>
    [Explain how this gene contributes to the overall physiological state of the organism]
    <conservation>[Is this contribution conserved? Explain.]</conservation>
  </physiological_contribution>

  <stress_responses>
    <response1>
      [Description of first stress response]
      <conservation>[Is this response conserved? Explain.]</conservation>
    </response1>
    <response2>
      [Description of second stress response]
      <conservation>[Is this response conserved? Explain.]</conservation>
    </response2>
    <!-- Add more response tags as needed -->
  </stress_responses>

  <uptake_exudation>
    <uptake>
      [Information about uptake processes]
      <conservation>[Is this process conserved? Explain.]</conservation>
    </uptake>
    <exudation>
      [Information about exudation processes]
      <conservation>[Is this process conserved? Explain.]</conservation>
    </exudation>
  </uptake_exudation>

  <phylogenetic_persistence>
    [Discussion of research persistence across different phylogenetic levels]
  </phylogenetic_persistence>

  <coculture_role>
    [Describe any known information about gene role and expression changes when in coculture with heterotrophic bacteria]
    <conservation>[Is this role conserved in coculture conditions? Explain.]</conservation>
  </coculture_role>

  <references>
    <ref1>[First reference in standard academic format]</ref1>
    <ref2>[Second reference in standard academic format]</ref2>
    <!-- Add more ref tags as needed -->
  </references>
</database_entry>

Important guidelines:
1. Rely solely on published research and factual information.
2. If information is not available for any section, clearly state this lack of data within the relevant tags.
3. Use citations in the format [Author, Year] throughout the database entry, ensuring all citations are listed in the references section.
4. For each section, consider and discuss whether the described role or function is conserved across different strains or related species.
5. Pay special attention to any information about the gene's role in coculture conditions with heterotrophic bacteria.

Begin your response with the research process.
'''    


prompt_build_gene_entry_try1 = '''
You are a highly skilled research assistant specializing in microbiology, particularly in the study of Prochlorococcus bacteria. Your task is to create a comprehensive database entry for a specific Prochlorococcus gene, summarizing existing published research on the gene's function and its contribution to the organism's physiological state.

Here are details of the gene you will be researching:
<gene_name>
{{GENE_NAME}}
</gene_name>

<gene_product>
{{GENE_PRODUCT}}
</gene_product>

<gene_protein_id>
{{GENE_PROTEIN_ID}}
</gene_protein_id>

Before providing your final database entry, please wrap your literature review process in <literature_review> tags. This should include:

1. List key search terms and databases you would use for this research.
2. Provide a brief overview of the available literature on this gene, including:
   - Number of relevant papers found
   - Date range of the research
   - Main research focuses
3. For each key source identified (aim for 3-5 sources):
   - Provide a proper citation
   - Write a 2-3 sentence summary of the main findings related to the gene
4. Note any challenges or limitations in finding information
5. Highlight any conflicting information or significant gaps in the research
6. Summarize initial observations about the gene's function and importance

After your literature review, provide a comprehensive database entry within <database_entry> tags. Your entry should include the following sections:

1. <primary_function>: Describe the main role of the gene in Prochlorococcus.
2. <physiological_contribution>: Explain how this gene contributes to the overall physiological state of the organism.
3. <stress_responses>: List and describe any identified stress responses associated with this gene.
4. <uptake_exudation>: Provide information about uptake and exudation processes related to this gene's expression.
5. <bacterial_interaction>: Provide information about uptake and exudation processes related to this gene's expression.
5. <phylogenetic_persistence>: Discuss how persistent the research is on this gene across different phylogenetic levels (e.g., Prochlorococcus, cyanobacteria, gram-positive bacteria).
6. <references>: List all genuine publications used in your research, using a standard academic citation format.

Throughout the literature review and the database entry, add citations wherever applicable in the format [Martiny, 2006]. Make sure all of these citations are also listed in the references section.
If information is not available for any section, clearly state this lack of data within the relevant tags.

Here's an example of the desired output structure:

<database_entry>
  <primary_function>
    [Detailed description of the gene's primary function]
  </primary_function>
  <physiological_contribution>
    [Explanation of the gene's contribution to Prochlorococcus physiology]
  </physiological_contribution>
  <stress_responses>
    <response1>[Description of first stress response]</response1>
    <response2>[Description of second stress response]</response2>
    <!-- Add more response tags as needed -->
  </stress_responses>
  <uptake_exudation>
    <uptake>[Information about uptake processes]</uptake>
    <exudation>[Information about exudation processes]</exudation>
  </uptake_exudation>
  <phylogenetic_persistence>
    [Discussion of research persistence across different phylogenetic levels]
  </phylogenetic_persistence>
  <references>
    <ref1>[First reference in standard academic format]</ref1>
    <ref2>[Second reference in standard academic format]</ref2>
    <!-- Add more ref tags as needed -->
  </references>
</database_entry>

Remember to rely solely on published research and factual information. If you don't have information on a specific aspect of the gene or topic, clearly state this in the relevant section.

Please begin your literature review now.
'''


short_prompt_unstructured = '''
give me an overview of the gene {{GENE_NAME}} ({{GENE_PRODUCT}}) in prochlorococcus med4. 
Specifically its general function, its role in stress response and its potential role in coculture with heterotrophic bacteria, 
and in nutrient uptake and exchange with heterotrophic bacteria.
Remember to rely solely on published research and factual information. If you don't have information on a specific aspect of the gene or topic, clearly state this in the relevant section. End the section with a list of references in standard format, Use citations in the format [Author, Year] throughout your response.
'''

short_prompt_unstructured_from_copilot = '''
Provide a detailed overview of the gene {{GENE_NAME}} ({{GENE_PRODUCT}}) in Prochlorococcus MED4. 
Include its general function, role in stress response, and potential role in coculture with heterotrophic bacteria, as well as nutrient uptake and exchange with heterotrophic bacteria. 
Ensure all information is based on published research and factual data. Clearly state if information on a specific aspect is unavailable. 
End the response with a list of references in standard format, and use citations in the format [Author, Year] throughout the response.
'''
