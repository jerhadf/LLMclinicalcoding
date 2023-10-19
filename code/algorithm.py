# Algorithm 1 Assign a set of ICD codes for a case note using LLM-guided tree search.

# from https://arxiv.org/pdf/2310.06552v1.pdf

# Requisites:
# • tree: An ICD ontology, with methods for accessing the natural language code descriptions,
# selecting the children of a code and checking if a given code is assignable (i.e a leaf code).
# • prompt_template: An LLM prompt which embeds the string variables ‘case_note’ and
# ‘code_descriptions’.
# • llm_api_request: a function accepting a case note and a set of code descriptions to be
# inserted into the prompt. Returns a text completion from the LLM.
# • match_code_descriptions: a function which takes an LLM text completion and the set
# of candidate code descriptions and returns the codes which the model predicted as being
# relevant.
# 1: function SEARCH_TREE(case_note)
# 2: assigned_codes ← () ▷ Predicted leaf codes
# 3: candidate_codes ← tree.root.children ▷ The set of ICD-10 chapters
# 4:
# 5: while true do
# 6: code_descriptions ← tree.get_descriptions(candidate_codes)
# 7: llm_response ← llm_api_request(case_note, code_descriptions)
# 8: predicted_codes ← match_code_descriptions(llm_response, code_descriptions)
# 9:
# 10: for code in predicted_codes do
# 11: if code in tree.assignable_codes then
# 12: assigned_codes.append(code)
# 13: else
# 14: parent_codes.append(code)
# 15: end if
# 16: end for
# 17:
# 18: if parent_codes.length > 0 then
# 19: parent_code ← parent_codes.pop(0)
# 20: candidate_codes ← tree.get_child_codes(parentCode)
# 21: else
# 22: break ▷ There are no further codes to explore.
# 23: end if
# 24: end while
# 25: return assigned_codes
# 26: end function
# Under the simplifying assumption that generating a response to each prompt takes constant time,
# the time complexity for the LLM-guided tree search algorithm is the same as that of a multi-label
# decision tree query: O(k · log(d)), where k refers to the number of predicted labels and and d refers
# to the depth of the tree at which each of these labels is found.
# Whilst any single path from the root of the tree to a leaf is on average ≈ 4 steps, if many paths are
# explored, the number of prompts can be large (> 100). We therefore enforce a simple prompt limit
# (not described in Algorithm A.4) in place of the while true loop to avoid excessive steps. We set
# this hyper-parameter to a value of 50, as early experiments suggested that additional steps beyond
# this yield little benefit.