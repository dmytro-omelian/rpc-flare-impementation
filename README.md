# Paper: Active Retrieval Augmented Generation
_Authors: Zhengbao Jiang, Frank F. Xu, Luyu Gao, Zhiqing Sun, Qian Liu, Jane Dwivedi-Yu, Yiming Yang, Jamie Callan, Graham Neubig_

## Abstract
_Despite the remarkable ability of large language models (LMs) to comprehend and generate language, 
they have a tendency to hallucinate and create factually inaccurate output. Augmenting LMs by retrieving 
information from external knowledge resources is one promising solution. Most existing retrieval-augmented LMs 
employ a retrieve- and-generate setup that only retrieves information once based on the input. 
This is limiting, however, in more general scenarios involving generation of long texts, where continually gathering 
information throughout the generation process is essential. There have been some past efforts to retrieve 
information multiple times while generating outputs, which mostly retrieve documents at fixed intervals 
using the previous context as queries. In this work, we provide a generalized view of active retrieval augmented generation, 
methods that actively decide when and what to retrieve across the course of the generation. 
We propose **Forward-Looking Active REtrieval** augmented generation (FLARE), a generic retrieval-augmented generation method 
which iteratively uses a prediction of the upcoming sentence to anticipate future content, which is then utilized as a query 
to retrieve relevant documents to regenerate the sentence if it contains low-confidence tokens. 
We test FLARE along with baselines comprehensively over 4 longform knowledge-intensive generation tasks/datasets. 
FLARE achieves superior or competitive performance on all tasks, demonstrating the effectiveness of our method._

## Requirements
- ...
