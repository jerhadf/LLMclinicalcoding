# System prompt

## Iteration A - basic
ROLE: You are a clinical coder.

TASK: Consider the case note below and assign the appropriate ICD code.

{Case note}

ICD code:

## GPT prompt
GPT-3.5/4 Prompt

[ Case note]:

{note}
11 11 11

[Example]:
<example prompt>
Gastro-esophageal reflux disease
Enteroptosis

<response>
Gastro-esophageal reflux diease: Yes, Patient was prescribed omeprazole.
Enteroptosis: No.

[ Task]:
Consider each of the following ICD-10 code descriptions and evaluate if there are
any related mentions in the case note.
Follow the format in the example precisely.

{code descriptions}

## GPT-4 refinement prompt
GPT-4 Meta-refinement prompt
[Discharge Note]: 11 11 1T
{note}
11 11 1T

[Assigned ICD-10 code descriptions]:
{code descriptions}

[Instructions]:
Responding only with ICD-10 code descriptions, give a list of any seemingly
incorrect ICD-10 codes that have been assigned for this discharge note.

Figure 4: Meta-refinement prompt template for GPT-4. The response is parsed to extract the listed
codes which are then removed from the set of predictions.

## LLAMA prompt
Llama-2 Prompt

[ Case note]:
{note}

[Example]:
<code descriptions>
* Gastro-esophageal reflux disease
* Enteroptosis
* Acute Nasopharyngitis [Common Cold]
</code descriptions>

<response>
* Gastro-esophageal reflux diease: Yes, Patient was prescribed omeprazole.
* Enteroptosis: No.
* Acute Nasopharyngitis [Common Cold]: No.
</response>

[Task]:
Follow the format in the example response exactly, including the entire
description before your (Yes|No) judgement, followed by a newline.
Consider each of the following ICD-10 code descriptions and evlaluate if there
are any related mentions in the Case note.

{code descriptions}