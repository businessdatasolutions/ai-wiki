# An Analysis of Fusion Functions for Hybrid Retrieval

**Authors:** Sebastian Bruch, Siyu Gai, Amir Ingber
**Venue:** ACM Transactions on Information Systems (TOIS), 2023
**DOI:** https://doi.org/10.1145/3596512
**arXiv:** 2210.11934 (v1 21 Oct 2022; **v2 4 May 2023 — the version held here**)
**URL:** https://arxiv.org/abs/2210.11934
**OpenAlex:** W4377138005
**Captured:** 2026-09-16 (curl of the arXiv PDF)
**fulltext_source:** pdf-converted
**converter:** pdftotext -layout
**pages:** 36

---

## Scope and conversion note

Full paper, all 36 pages. `pdftotext -layout` flattens the results tables and mangles inline
math — verify any number against the co-located PDF before quoting it on a wiki page.

**Why acquired.** Directly bears on `CLAUDE.md` §Search and on the hardcoded `K_RRF = 60` /
`GRAPH_W = 0.5` constants in `scripts/wiki-retrieve.mjs`. The paper's headline claim runs
*against* the assumption baked into the v0.10 plan: RRF is parameter-sensitive, and a convex
combination of lexical and semantic scores outperforms it in-domain and out-of-domain while
needing only a small tuning set.

---

                                        An Analysis of Fusion Functions for Hybrid Retrieval
                                        SEBASTIAN BRUCH, Pinecone, USA
                                        SIYU GAI∗ , University of California, Berkeley, USA
                                        AMIR INGBER, Pinecone, Israel




arXiv:2210.11934v2 [cs.IR] 4 May 2023
                                        We study hybrid search in text retrieval where lexical and semantic search are fused together with the intuition
                                        that the two are complementary in how they model relevance. In particular, we examine fusion by a convex
                                        combination (CC) of lexical and semantic scores, as well as the Reciprocal Rank Fusion (RRF) method, and
                                        identify their advantages and potential pitfalls. Contrary to existing studies, we find RRF to be sensitive to
                                        its parameters; that the learning of a CC fusion is generally agnostic to the choice of score normalization;
                                        that CC outperforms RRF in in-domain and out-of-domain settings; and finally, that CC is sample efficient,
                                        requiring only a small set of training examples to tune its only parameter to a target domain.
                                        CCS Concepts: • Information systems → Retrieval models and ranking; Combination, fusion and
                                        federated search.
                                        Additional Key Words and Phrases: Hybrid Retrieval, Lexical and Semantic Search, Fusion Functions

                                        1   INTRODUCTION
                                        Retrieval is the first stage in a multi-stage ranking system [1, 2, 45], where the objective is to find
                                        the top-𝑘 set of documents, that are the most relevant to a given query 𝑞, from a large collection of
                                        documents D. Implicit in this task are two major research questions: a) how do we measure the
                                        relevance between a query 𝑞 and a document 𝑑 ∈ D?; and, b) how do we find the top-𝑘 documents
                                        according to a given similarity metric efficiently? In this work, we are primarily concerned with
                                        the former question in the context of text retrieval.
                                           As a fundamental problem in Information Retrieval (IR), the question of the similarity between
                                        queries and documents has been explored extensively. Early methods model text as a Bag of
                                        Words (BoW) and compute the similarity of two pieces of text using a statistical measure such as
                                        the term frequency-inverse document frequency (TF-IDF) family, with BM25 [33, 34] being its most
                                        prominent member. We refer to retrieval with a BoW model as lexical search and the similarity
                                        scores computed by such a system as lexical scores.
                                           Lexical search is simple, efficient, (naturally) “zero-shot,” and generally effective, but has important
                                        limitations: it is susceptible to the vocabulary mismatch problem and, moreover, does not take
                                        into account the semantic similarity of queries and documents [5]. That, it turns out, is what deep
                                        learning models are excellent at. With the rise of pre-trained language models such as BERT [8],
                                        it is now standard practice to learn a vector representation of queries and documents that does
                                        capture their semantics, and thereby, reduce top-𝑘 retrieval to the problem of finding 𝑘 nearest
                                        neighbors in the resulting vector space [9, 13, 16, 32, 40, 44]—where closeness is measured using
                                        vector similarity or distance. We refer to this method as semantic search and the similarity scores
                                        computed by such a system as semantic scores.
                                           Hypothesizing that lexical and semantic search are complementary in how they model relevance,
                                        recent works [5, 13, 14, 19, 20, 42] began exploring methods to fuse together lexical and semantic
                                        retrieval: for a query 𝑞 and ranked lists of documents 𝑅Lex and 𝑅Sem retrieved separately by lexical
                                        and semantic search systems respectively, the task is to construct a final ranked list 𝑅Fusion so as to
                                        improve retrieval quality. This is often referred to as hybrid search.
                                        ∗ Contributed to this work during a research internship at Pinecone.


                                        Authors’ addresses: Sebastian Bruch, sbruch@acm.org, Pinecone, New York, NY, USA; Siyu Gai, catherine_gai@berkeley.edu,
                                        University of California, Berkeley, Berkeley, CA, USA; Amir Ingber, Pinecone, Tel Aviv, Israel, ingber@pinecone.io.
2                                                                               Sebastian Bruch, Siyu Gai, and Amir Ingber


   It is becoming increasingly clear that hybrid search does indeed lead to meaningful gains in
retrieval quality, especially when applied to out-of-domain datasets [5, 40]—settings in which the
semantic retrieval component uses a model that was not trained or fine-tuned on the target dataset.
What is less clear and is worthy of further investigation, however, is how this fusion is done.
   One intuitive and common approach is to linearly combine lexical and semantic scores [13, 20, 40].
If 𝑓Lex (𝑞, 𝑑) and 𝑓Sem (𝑞, 𝑑) represent the lexical and semantic scores of document 𝑑 with respect
to query 𝑞, then a linear (or more accurately, convex) combination is expressed as 𝑓Convex =
𝛼 𝑓Sem + (1 − 𝛼) 𝑓Lex where 0 ≤ 𝛼 ≤ 1. Because lexical scores (such as BM25) and semantic scores
(such as dot product) may be unbounded, often they are normalized with min-max scaling [16, 40]
prior to fusion.
   A recent study [5] argues that convex combination is sensitive to its parameter 𝛼 and the
choice of score normalization.1 They claim and show empirically, instead, that Reciprocal Rank
Fusion (RRF) [6] may be a more suitable fusion as it is non-parametric and may be utilized in a
zero-shot manner. They demonstrate its impressive performance even in zero-shot settings on a
number of benchmark datasets.
   This work was inspired by the claims made in [5]; whereas [5] addresses how various hybrid
methods perform relative to one another in an empirical study, we re-examine their findings
and analyze why these methods work and what contributes to their relative performance. Our
contributions thus can best be summarized as an in-depth examination of fusion functions and
their behavior.
   As our first research question (RQ1), we investigate whether the convex combination fusion is
a reasonable choice and study its sensitivity to the normalization protocol. We show that, while
normalization is essential to create a bounded function and thereby bestow consistency to the
fusion across domains, the specific choice of normalization is a rather small detail: there always
exist convex combinations of scores normalized by min-max, standard score, or any other linear
transformation that are rank-equivalent. In fact, when formulated as a per-query learning problem,
the solution found for a dataset that is normalized with one scheme can be transformed to a solution
for a different choice.
   We next investigate the properties of RRF. We first unpack RRF and examine its sensitivity to its
parameters as our second research question (RQ2)—contrary to [5], we adopt a parametric view
of RRF where we have as many parameters as there are retrieval functions to fuse, a quantity
that is always one more than that in a convex combination. We find that, in contrast to a convex
combination, a tuned RRF generalizes poorly to out-of-domain datasets. We then intuit that, because
RRF is a function of ranks, it disregards the distribution of scores and, as such, discards useful
information. Observe that the distance between raw scores plays no role in determining their
hybrid score—a behavior we find counter-intuitive in a metric space where distance does matter.
Examining this property constitutes our third and final research question (RQ3).
   Finally, we empirically demonstrate an unsurprising yet important fact: tuning 𝛼 in a convex
combination fusion function is extremely sample-efficient, requiring just a handful of labeled
queries to arrive at a value suitable for a target domain, regardless of the magnitude of shift in
the data distribution. RRF, on the other hand, is relatively less sample-efficient and converges to a
relatively less effective retrieval system.
   We believe our findings, both theoretical and empirical, are important and pertinent to the
research in this field. Our analysis leads us to believe that the convex combination formulation is
theoretically sound, empirically effective, sample-efficient, and robust to domain shift. Moreover,

1 c.f. Section 3.1 in [5]: “This fusion method is sensitive to the score scales . . . which needs careful score normalization”

(emphasis ours).
An Analysis of Fusion Functions for Hybrid Retrieval                                               3


unlike the parameters in RRF, the parameter(s) of a convex function are highly interpretable and, if
no training samples are available, can be adjusted to incorporate domain knowledge.
   We organized the remainder of this article as follows. In Section 2, we review the relevant
literature on hybrid search. Section 3 then introduces our adopted notation and provides details of
our empirical setup, thereby providing context for the theoretical and empirical analysis of fusion
functions. In Section 4, we begin our analysis by a detailed look at the convex combination of
retrieval scores. We then examine RRF in Section 5. In Section 6, we summarize our observations
and identify the properties a fusion function should have to behave well in hybrid retrieval. We
then conclude this work and state future research directions in Section 7.

2   RELATED WORK
A multi-stage ranking system is typically comprised of a retrieval stage and several subsequent re-
ranking stages, where the retrieved candidates are ordered using more complex ranking functions [2,
39]. Conventional wisdom has that retrieval must be recall-oriented while improving ranking quality
may be left to the re-ranking stages, which are typically Learning to Rank (LtR) models [17, 24,
29, 39, 41]. There is indeed much research on the trade-offs between recall and precision in such
multi-stage cascades [7, 21], but a recent study [46] challenges that established convention and
presents theoretical analysis that suggests retrieval must instead optimize precision. We therefore
report both recall and NDCG [11], but focus on NDCG where space constraints prevent us from
presenting both or when similar conclusions can be reached regardless of the metric used.
   One choice for retrieval that remains popular to date is BM25 [33, 34]. This additive statistic
computes a weighted lexical match between query and document terms: it computes, for each
query term, the product of its “importance” (i.e., frequency of a term in a document, normalized
by document and global statistics such as average length) and its propensity—a quantity that is
inversely proportionate to the fraction of documents that contain the term—and adds the scores of
query terms to arrive at the final similarity or relevance score. Because BM25, like other lexical
scoring functions, insists on an exact match of terms, even a slight typo can throw the function off.
This vocabulary mismatch problem has been subject to much research in the past, with remedies
ranging from pseudo-relevance feedback to document and query expansion techniques [15, 30, 36].
   Trying to address the limitations of lexical search can only go so far, however. After all, they
additionally do not capture the semantic similarity between queries and documents, which may
be an important signal indicative of relevance. It has been shown that both of these issues can
be remedied by Transformer-based [38] pre-trained language models such as BERT [8]. Applied
to the ranking task, such models [25, 27–29] have advanced the state-of-the-art dramatically on
benchmark datasets [26].
   The computationally intensive inference of these deep models often renders them too ineffi-
cient for first-stage retrieval, however, making them more suitable for re-ranking stages. But by
cleverly disentangling the query and document transformations into the so-called dual-encoder
architecture, where, in the resulting design, the “embedding” of a document can be computed
independently of queries, we can pre-compute document vectors and store them offline. In this
way, we substantially reduce the computational cost during inference as it is only necessary to
obtain the vector representation of the query during inference. At a high level, these models project
queries and documents onto a low-dimensional vector space where semantically-similar points
stay closer to each other. By doing so we transform the retrieval problem to one of similarity search
or Approximate Nearest Neighbor (ANN) search—the 𝑘 nearest neighbors to a query vector are the
desired top-𝑘 documents. This ANN problem can be solved efficiently using a number of algorithms
such as FAISS [12] or Hierarchical Navigable Small World Graphs [22] available as open source
4                                                                                 Sebastian Bruch, Siyu Gai, and Amir Ingber


packages or through a managed service such as Pinecone2 , creating an opportunity to use deep
models and vector representations for first-stage retrieval [13, 44]—a setup that we refer to as
semantic search.
   Semantic search, however, has its own limitations. Previous studies [5, 37] have shown, for
example, that when applied to out-of-domain datasets, their performance is often worse than
BM25. Observing that lexical and semantic retrievers can be complementary in the way they
model relevance [5], it is only natural to consider a hybrid approach where lexical and semantic
similarities both contribute to the makeup of final retrieved list. To date there have been many
studies [13, 14, 18–20, 40, 42, 47] that do just that, where most focus on in-domain tasks with one
exception [5] that considers a zero-shot application too. Most of these works only use one of the
many existing fusion functions in experiments, but none compares the main ideas comprehensively.
We review the popular fusion functions from these works in the subsequent sections and, through
a comparative study, elaborate what about their behavior may or may not be problematic.


3     SETUP
In the sections that follow, we study fusion functions with a mix of theoretical and empirical analysis.
For that reason, we present our notation as well as empirical setup and evaluation measures here
to provide sufficient context for our arguments.


3.1    Notation
We adopt the following notation in this work. We use 𝑓o (𝑞, 𝑑) : Q × D → R to denote the score of
document 𝑑 ∈ D to query 𝑞 ∈ Q according to the retrieval system o ∈ O. If o is a semantic retriever,
Sem, then Q and D are the space of (dense) vectors in R𝑑 and 𝑓Sem is typically cosine similarity or
inner product. Similarly, when o is a lexical retriever, Lex, Q and D are high-dimensional sparse
vectors in R |𝑉 | , with |𝑉 | denoting the size of the vocabulary, and 𝑓Lex is typically BM25. A retrieval
system o is the space Q × D equipped with a metric 𝑓o (·, ·)—which need not be a proper metric.
  We denote the set of top-𝑘 documents retrieved for query 𝑞 by retrieval system o by 𝑅𝑘o (𝑞). We
write 𝜋o (𝑞, 𝑑) to denote the rank of document 𝑑 with respect to query 𝑞 according to retrieval
system o. Note that, 𝜋o (𝑞, 𝑑𝑖 ) can be expressed as the sum of indicator functions:


                                                                  1 𝑓o (𝑞,𝑑 𝑗 ) >𝑓o (𝑞,𝑑𝑖 ) ,
                                                      ∑︁
                               𝜋o (𝑞, 𝑑𝑖 ) = 1 +                                                                        (1)
                                                   𝑑 𝑗 ∈𝑅𝑘o (𝑞)



where 1𝑐 is 1 when the predicate 𝑐 holds and 0 otherwise. In words, and ignoring the subtleties
introduced by the presence of score ties, the rank of document 𝑑 is the count of documents whose
score is larger than the score of 𝑑.                    Î                         Î
    Hybrid retrieval operates on the product space of o𝑖 with metric 𝑓Fusion : 𝑓o𝑖 → R. Without
                                                 Î
loss of generality, in this work, we restrict o𝑖 to be Lex × Sem. That is, we only consider the
problem of fusing two retrieval scores, but note that much of the anlysis can be trivially extended
to the fusion of multiple retrieval systems. We refer to this hybrid metric as a fusion function.
    A fusion function 𝑓Fusion is typically applied to documents in the union of retrieved sets U𝑘 (𝑞) =
Ð 𝑘
   o 𝑅o (𝑞), which we simply call the union set. When a document 𝑑 in the union set is not present in
one of the top-𝑘 sets (i.e., 𝑑 ∈ U𝑘 (𝑞) but 𝑑 ∉ 𝑅𝑘o𝑖 (𝑞) for some o𝑖 ), we compute its missing score
(i.e., 𝑓o𝑖 (𝑞, 𝑑)) prior to fusion.
An Analysis of Fusion Functions for Hybrid Retrieval                                                     5


             Table 1. Datasets used in this work for evaluation purposes along with select statistics.


                                    Dataset            Document Count          Query Count
                        MS MARCO Passage v1                   8.8M                 6,980
                       Natural Questions (NQ)                 2.68M                3,452
                               Quora                          523K                10,000
                             NFCorpus                          3.6K                 323
                            HotpotQA                          5.23M                7,405
                               Fever                          5.42M                6,666
                              SciFact                           5K                  300
                             DBPedia                          4.63M                 400
                                FiQA                           57K                  648



3.2     Empirical Setup
Datasets: We evaluate our methods on a variety of publicly available benchmark datasets, summa-
rized in Table 1 both in in-domain and out-of-domain, zero-shot settings. One of the datasets is the
MS MARCO3 Passage Retrieval v1 dataset [26], a publicly available retrieval and ranking collection
from Microsoft. It consists of roughly 8.8 million short passages which, along with queries in natu-
ral language, originate from Bing. The queries are split into train, dev, and eval non-overlapping
subsets. We use the train queries for any learning or tuning and evaluate exclusively on the small
dev query set (consisting of 6,980 queries) in our analysis. Included in the dataset also are relevance
labels.
   We additionally experiment with 8 datasets from the BeIR collection [37]4 : Natural Questions
(NQ, question answering), Quora (duplicate detection), NFCorpus (medical), HotpotQA (question
answering), Fever (fact extraction), SciFact (scientific claim verification), DBPedia (entity search),
and FiQA (financial). For a more detailed description of each dataset, we refer the reader to [37].
   Lexical search: We use PISA [23] for keyword-based lexical retrieval. We tokenize queries
and documents by space and apply stemming available in PISA—we do not employ any other
preprocessing steps such as stopword removal, lemmatization, or expansion. We use BM25 with
the same hyperparameters as [5] (k1=0.9 and b=0.4) to retrieve the top 1,000 candidates.
   Semantic search: We use the all-MiniLM-L6-v2 model checkpoint available on HuggingFace5
to project queries and documents into 384-dimensional vectors, which can subsequently be used
for indexing and top-𝑘 retrieval using cosine similarity. This model has been shown to achieve
competitive quality on an array of benchmark datasets while remaining compact in size and efficient
to infer6 , thereby allowing us to conduct extensive experiments with results that are competitive
with existing state-of-the-art models. This model has been fine-tuned on a large number of datasets,
exceeding a total of 1 billion pairs of text, including NQ, MS MARCO Passage, and Quora. As such,
we consider all experiments on these three datasets as in-domain, and the rest as out-of-domain.
We use the exact search for inner product algorithm (IndexFlatIP) from FAISS [12] to retrieve top
1,000 nearest neighbors.

2 http://pinecone.io
3 Available at https://microsoft.github.io/msmarco/
4 Available at https://github.com/beir-cellar/beir
5 Available at https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2
6 c.f. https://sbert.net for details.
6                                                                           Sebastian Bruch, Siyu Gai, and Amir Ingber


   Supplementary models and fusions: Our primary set of experiments presented in the body
of this manuscript focus exclusively on the fusion of BM25 with the all-MiniLM-L6-v2 model as
representatives of lexical and semantic retrieval functions. We do, however, note that our analysis
of fusion functions is not limited to lexical-semantic search per se: all normalization and fusion
functions studied in this work can be applied to arbitrary scoring functions! As such, we conduct
additional experiments using a variety of pairs of retrieval models to confirm the generality of the
main theoretical findings of this work. We report these results in Appendix A through Appendix D.
   In Appendix A, we examine the fusion of the Splade model with BM25. Splade7 [9] is a deep
learning model that produces sparse representations for a given piece of text, where each non-zero
entry in the resulting embedding is the importance weight of a term in the BERT [8] WordPiece [43]
vocabulary comprising of roughly 30, 000 terms. Appendix B studies the fusion of BM25 with
the Tas-B [10] model.8 Tas-B is a bi-encoder model that was trained using supervision from a
cross-encoder and a ColBERT model. In Appendix C we fuse Splade and Tas-B, and in Appendix D
Tas-B and all-MiniLM-L6-v2.
   We note that, both Splade and Tas-B were fine-tuned on the MS MARCO dataset. As such, in all
the supplementary experiments, results reported on the MS MARCO dataset should be considered
“in-domain” while the remaining datasets represent out-of-domain distributions.
   Evaluation: Unless noted otherwise, we form the union set for every query from the candidates
retrieved by the lexical and semantic search systems. We then compute missing scores where
required, compute 𝑓Fusion on the union set, and re-order according to the hybrid scores. We then
measure Recall@1000 and NDCG@1000 to quantify ranking quality, as recommended by Zamani
et al. [46]. Due to the much smaller size of SciFact and NFCorpus, we evaluate Recall and NDCG
at rank cutoff 100 instead, retrieving roughly 2% and 2.7% of the size of the dataset, respectively.
We note that, this choice of cutoff does not affect the outcome of our experiments or change our
conclusions, but it more clearly highlights the differences between the various methods; recall
approaches 1 regardless of the retrieval method if rank cutoff was 1,000 (or 20% and 27% of the size
of the datasets). Further note that, we choose to evaluate deep (i.e., with a larger rank cut-off) rather
than shallow metrics per the discussion in [40] to understand the performance of each system more
completely.

4   ANALYSIS OF CONVEX COMBINATION OF RETRIEVAL SCORES
We are interested in understanding the behavior and properties of fusion functions. In the remainder
of this work, we study through that lens two popular methods that are representative of existing
ideas in the literature, beginning with a convex combination of scores.
   As noted earlier, most existing works use a convex combination of lexical and semantic scores as
follows: 𝑓Convex (𝑞, 𝑑) = 𝛼 𝑓Sem (𝑞, 𝑑) + (1 − 𝛼)𝑓Lex (𝑞, 𝑑) for some 0 ≤ 𝛼 ≤ 1. When 𝛼 = 1 the above
collapses to semantic scores and when it is 0, to lexical scores.
   An interesting property of this fusion is that it takes into account the distribution of scores. In
other words, the distance between lexical (or semantic) scores of two documents plays a significant
role in determining their final hybrid score. One disadvantage, however, is that the range of 𝑓Sem
can be very different from 𝑓Lex . Moreover, as with TF-IDF in lexical search or with inner product in
semantic search, the range of individual functions 𝑓o may depend on the norm of the query and
document vectors (e.g., BM25 is a function of the number of query terms). As such any constant 𝛼
is likely to yield inconsistently-scaled hybrid scores.


7 Pre-trained checkpoint from HuggingFace available at https://huggingface.co/naver/splade-cocondenser-ensembledistil
8 Available at https://huggingface.co/sentence-transformers/msmarco-distilbert-base-tas-b
An Analysis of Fusion Functions for Hybrid Retrieval                                                   7


  The problem above is trivially addressed by applying score normalization prior to fusion [16, 40].
Suppose we have collected a union set U𝑘 (𝑞) for 𝑞, and that for every candidate we have computed
both lexical and semantic scores. Now, consider the min-max scaling of scores 𝜙 mm : R → [0, 1]
below:
                                                      𝑓o (𝑞, 𝑑) − 𝑚𝑞
                                   𝜙 mm (𝑓o (𝑞, 𝑑)) =                ,                           (2)
                                                         𝑀𝑞 − 𝑚𝑞
where 𝑚𝑞 = min𝑑 ∈U𝑘 (𝑞) 𝑓o (𝑞, 𝑑) and 𝑀𝑞 = max𝑑 ∈U𝑘 (𝑞) 𝑓o (𝑞, 𝑑). We note that, min-max scaling is
the de facto method in the literature, but other choices of 𝜙 o (·) in the more general expression
below:
                   𝑓Convex (𝑞, 𝑑) = 𝛼𝜙 Sem (𝑓Sem (𝑞, 𝑑)) + (1 − 𝛼)𝜙 Lex (𝑓Lex (𝑞, 𝑑)),           (3)
are valid as well so long as 𝜙 Sem, 𝜙 Lex : R → R are monotone in their argument. For example, for
reasons that will become clearer later, we can redefine the normalization by replacing the minimum
of the set with the theoretical minimum of the function (i.e., the maximum value that is always less
than or equal to all values attainable by the scoring function, or its infimum) to arrive at:
                                                         𝑓o (𝑞, 𝑑) − inf 𝑓o (𝑞, ·)
                                   𝜙 tmm (𝑓o (𝑞, 𝑑)) =                             .                 (4)
                                                            𝑀𝑞 − inf 𝑓o (𝑞, ·)
As an example, when 𝑓Lex is BM25, then its infimum is 0. When 𝑓Sem is cosine similarity, then that
quantity is −1.
  Another popular choice is the standard score (z-score) normalization which is defined as follows:
                                                     𝑓o (𝑞, 𝑑) − 𝜇
                                          𝜙 z (𝑓o (𝑞, 𝑑)) =        ,                                 (5)
                                                           𝜎
where 𝜇 and 𝜎 denote the mean and standard deviation of the set of scores 𝑓o (𝑞, ·) for query 𝑞.
   We will return to normalization shortly, but we make note of one small but important fact: in
cases where the variance of lexical (semantic) scores in the union set is 0, we may skip the fusion
step altogether because retrieval quality will be unaffected by lexical (semantic) scores. The case
where the variance is arbitrarily close to 0, however, creates challenges for certain normalization
functions. While this would make for an interesting theoretical analysis, we do not study this
particular setting in this work as, empirically, we do observe a reasonably large variance among
scores in the union set on all datasets using state-of-the-art lexical and semantic retrieval functions.

4.1   Suitability of Convex Combination
A convex combination of scores is a natural choice for creating a mixture of two retrieval systems,
but is it a reasonable choice? It has been established in many past empirical studies that 𝑓Convex with
min-max normalization often serves as a strong baseline. So the answer to our question appears to
be positive. Nonetheless, we believe it is important to understand precisely why this fusion works.
  We investigate this question empirically, by visualizing lexical and semantic scores of query-
document pairs from an array of datasets. Because we operate in a two-dimensional space, observing
the pattern of positive (where document is relevant to query) and negative samples in a plot can
reveal a lot about whether and how they are separable and how the fusion function behaves. To
that end, we sample up to 20,000 positive and up to the same number of negative query-document
pairs from the validation split of each dataset, and illustrate the collected points in a scatter plot in
Figure 1.
  From these figures, it is clear that positive and negative samples form clusters that are, with
some error, separable by a linear function. What is different between datasets is the slope of this
separating line. For example, in MS MARCO, Quora, and NQ, which are in-domain datasets, the
separating line is almost vertical, suggesting that the semantic scores serve as a sufficiently strong
8                                                                    Sebastian Bruch, Siyu Gai, and Amir Ingber




                          (a) MS MARCO                               (b) Quora




                               (c) NQ                                 (d) FiQA




                           (e) HotpotQA                               (f) Fever

Fig. 1. Visualization of the normalized lexical (𝜙 tmm (𝑓Lex )) and semantic (𝜙 tmm (𝑓Sem )) scores of query-
document pairs sampled from the validation split of each dataset. Shown in red are up to 20,000 positive
samples where document is relevant to query, and in black up to the same number of negative samples.
Adding a lexical (semantic) dimension to query-document pairs helps tease out the relevant documents
that would be statistically indistinguishable in a one-dimensional semantic (lexical) view of the data—when
samples are projected onto the 𝑥 (𝑦) axis.




signal for relevance. This is somewhat true of FiQA. In other out-of-domain datasets, however, the
line is rotated counter-clockwise, indicating a more balanced weighting of lexical and semantic
scores. Said differently, adding a lexical (semantic) dimension to query-document pairs helps tease
An Analysis of Fusion Functions for Hybrid Retrieval                                                   9




                          (a) 𝛼 = 0.6                                        (b) 𝛼 = 0.8

                        Fig. 2. Effect of 𝑓Convex on pairs of lexical and semantic scores.



out the relevant documents that would be statistically indistinguishable in a one-dimensional
semantic (lexical) view of the data. Interestingly, across all datasets, there is a higher concentration
of negative samples where lexical scores vanish.
   This empirical evidence suggests that lexical and semantic scores may indeed be complementary—
an observation that is in agreement with prior work [5]—and a line may be a reasonable choice for
distinguishing between positive and negative samples. But while these figures shed light on the
shape of positive and negative clusters and their separability, our problem is not classification but
ranking. We seek to order query-document pairs and, as such, separability is less critical and, in fact,
not required. It is therefore instructive to understand the effect of a particular convex combination
on pairs of lexical and semantic scores. This is visualized in Figure 2 for two values of 𝛼 in 𝑓Convex .
   The plots in Figure 2 illustrate how the parameter 𝛼 determines how different regions of the
plane are ranked relative to each other. This is a trivial fact, but it is nonetheless interesting to map
these patterns to the distributions in Figure 1. In-domain datasets, for example, form a pattern of
positives and negatives that is unsurprisingly more in tune with the 𝛼 = 0.8 setting of 𝑓Convex than
𝛼 = 0.6.

4.2   Role of Normalization
We have thus far used min-max normalization to be consistent with the literature. In this section,
we ask the question first raised by Chen et al. [5] on whether and to what extent the choice of nor-
malization matters and how carefully one must choose the normalization protocol. In other words,
we wish to examine the effect of 𝜙 Sem (·) and 𝜙 Lex (·) on the convex combination in Equation (3).
  Before we begin, let us consider the following suite of functions:
   • 𝜙 mm : Min-max scaling of Equation (2);
   • 𝜙 tmm : Theoretical min-max scaling of Equation (4);
   • 𝜙 z : z-score normalization of Equation (5);
   • 𝜙 mm−Lex : Min-max scaling of lexical scores, unnormalized semantic scores;
   • 𝜙 tmm−Lex : Theoretical min-max normalized lexical scores, unnormalized semantic scores;
   • 𝜙 z−Lex : z-score normalized lexical scores, unnormalized semantic scores; and,
   • 𝐼 : The identity transformation, leaving both semantic and lexical scores unnormalized.
10                                                                       Sebastian Bruch, Siyu Gai, and Amir Ingber


We believe these transformations together test the various conditions in our upcoming arguments.
 Let us first state the notion of rank-equivalence more formally:
                                                                                                            𝜋
  Definition 4.1. We say two functions 𝑓 and 𝑔 are rank-equivalent on the set U and write 𝑓 = 𝑔, if
the order among documents in a set U induced by 𝑓 is the same as that induced by 𝑔.
   For example, when 𝜙 Sem (𝑥) = 𝑎𝑥 + 𝑏 and 𝜙 Lex (𝑥) = 𝑐𝑥 + 𝑑 are linear transformations of scores
for some positive coefficients 𝑎, 𝑏 and real intercepts 𝑏, 𝑐, then they can be reduced to the following
rank-equivalent form:
                                            𝜋
                             𝑓Convex (𝑞, 𝑑) = (𝑎𝛼) 𝑓Sem (𝑞, 𝑑) + 𝑐 (1 − 𝛼) 𝑓Lex (𝑞, 𝑑).
In fact, letting 𝛼 ′ = 𝑐𝛼/[𝑐𝛼 + 𝑐 (1 − 𝛼)] transforms the problem to one of learning a convex
combination of the original scores with a modified weight. This family of functions includes 𝜙 mm ,
𝜙 z , and 𝜙 tmm , and as such solutions for one family can be transformed to solutions for another
normalization protocol. More formally:
   Lemma 4.2. For every query, given an arbitrary 𝛼, there exists a 𝛼 ′ such that the convex combination
of min-max normalized scores with parameter 𝛼 is rank-equivalent to a convex combination of z-score
normalized scores with 𝛼 ′, and vice versa.
  Proof. Write 𝑚 o and 𝑀o for the minimum and maximum scores retrieved by system o, and 𝜇o
and 𝜎o for their mean and standard deviation. We also write 𝑅o = 𝑀o − 𝑚 o for brevity. For every
document 𝑑, we have the following:
         𝑓Sem (𝑞, 𝑑) − 𝑚 Sem           𝑓Lex (𝑞, 𝑑) − 𝑚 Lex 𝜋 𝛼                    1−𝛼
     𝛼                       + (1 − 𝛼)                       =      𝑓Sem (𝑞, 𝑑) +       𝑓Lex (𝑞, 𝑑)
                𝑅Sem                          𝑅Lex             𝑅sem                𝑅Lex
                             𝜋     1      𝛼                   1−𝛼                   𝛼           1−𝛼        
                             =                   𝑓Sem (𝑞, 𝑑) +       𝑓Lex (𝑞, 𝑑) −      𝜇Sem −         𝜇Lex
                               𝜎Sem𝜎Lex 𝑅Sem                   𝑅Lex                𝑅Sem           𝑅Lex
                             𝜋     𝛼       𝑓Sem (𝑞, 𝑑) − 𝜇Sem       1 − 𝛼 𝑓Lex (𝑞, 𝑑) − 𝜇Lex 
                             =                                  +                                 ,
                                𝑅Sem𝜎Lex          𝜎Sem            𝑅Lex𝜎Sem           𝜎Lex
where in every step we either added a constant or multiplied the expression by a positive constant,
both rank-preserving operations. Finally, setting
                                              𝛼        𝛼      1−𝛼
                                    𝛼′ =           /(       +         )
                                           𝑅Sem𝜎Lex 𝑅Sem𝜎Lex 𝑅Lex𝜎Sem
completes the proof. The other direction is similar.                                                             □

   The fact above implies that the problem of tuning 𝛼 for a query in a min-max normalization
regime is equivalent to learning 𝛼 ′ in a z-score normalized setting. In other words, there is a
one-to-one relationship between these parameters, and as a result solutions can be mapped from
one problem space to the other. However, this statement is only true for individual queries and
does not have any implications for the learning of the weight in the convex combination over an
entire collection of queries. Let us now consider this more complex setup.
   The question we wish to answer is as follows: under what conditions is 𝑓Convex with parameter
                                                                                  ′
𝛼 and a pair of normalization functions (𝜙 Sem, 𝜙 Lex ) rank-equivalent to an 𝑓Convex    of a new pair of
                            ′     ′                  ′
normalization functions (𝜙 Sem, 𝜙 Lex ) with weight 𝛼 ? That is, for a constant 𝛼 with one normalization
protocol, when is there a constant 𝛼 ′ that produces the same ranked lists for every query but with
a different normalization protocol? The answer to this question helps us understand whether and
when changing normalization schemes from min-max to z-score, for example, matters. We state
the following definitions followed by a theorem that answers this question.
An Analysis of Fusion Functions for Hybrid Retrieval                                                       11


   Definition 4.3. We say 𝑓 : R → R is a 𝛿-expansion with respect to 𝑔 : R → R if for any 𝑥 and 𝑦
in the domains of 𝑓 and 𝑔 we have that |𝑓 (𝑦) − 𝑓 (𝑥)| ≥ 𝛿 |𝑔(𝑦) − 𝑔(𝑥)| for some 𝛿 ≥ 1.
  For example, 𝜙 mm (·) is an expansion with respect to 𝜙 tmm (·) with a factor 𝛿 that depends on the
range of the scores. As another example, 𝜙 z (·) is an expansion with respect to 𝜙 mm (·).
   Definition 4.4. For two pairs of functions 𝑓 , 𝑔 : R → R and 𝑓 ′, 𝑔 ′ : R → R, and two points 𝑥 and
𝑦 in their domains, we say that 𝑓 ′ expands with respect to 𝑓 more rapidly than 𝑔 ′ expands with
respect to 𝑔, with a relative expansion rate of 𝜆 ≥ 1, if the following condition holds:
                                 |𝑓 ′ (𝑦) − 𝑓 ′ (𝑥)|     |𝑔 ′ (𝑦) − 𝑔 ′ (𝑥)|
                                                     =𝜆                      .
                                  |𝑓 (𝑦) − 𝑓 (𝑥)|         |𝑔(𝑦) − 𝑔(𝑥)|
When 𝜆 is independent of the points 𝑥 and 𝑦, we call this relative expansion uniform:
                                          |Δ𝑓 ′ |/|Δ𝑓 |
                                                        = 𝜆, ∀𝑥, 𝑦.
                                          |Δ𝑔 ′ |/|Δ𝑔|

  As an example, if 𝑓 and 𝑔 are min-max scaling and 𝑓 ′ and 𝑔 ′ are z-score normalization, then
their respective rate of expansion is roughly similar. We will later show that this property often
holds empirically across different transformations.
  Theorem 4.5. For every choice of 𝛼, there exists a constant 𝛼 ′ such that the following functions are
rank-equivalent on a collection of queries 𝑄:
                               𝑓Convex = 𝛼𝜙 (𝑓Sem (𝑞, 𝑑)) + (1 − 𝛼)𝜔 (𝑓Lex (𝑞, 𝑑)),
and
                           ′
                         𝑓Convex = 𝛼 ′𝜙 ′ (𝑓Sem (𝑞, 𝑑)) + (1 − 𝛼 ′)𝜔 ′ (𝑓Lex (𝑞, 𝑑)),
if for the monotone functions 𝜙, 𝜔, 𝜙 ′, 𝜔 ′ : R → R, 𝜙 ′ expands with respect to 𝜙 more rapidly than 𝜔 ′
expands with respect to 𝜔 with a uniform rate 𝜆.
  Proof. Consider a pair of documents 𝑑𝑖 and 𝑑 𝑗 in the ranked list of a query 𝑞 such that 𝑑𝑖 is
ranked above 𝑑 𝑗 according to 𝑓Convex . Shortening 𝑓o (𝑞, 𝑑𝑘 ) to 𝑓o(𝑘) for brevity, we have that:
     (𝑖)       ( 𝑗)               (𝑖)          ( 𝑗)            ( 𝑗)          (𝑖)         ( 𝑗)          (𝑖)
   𝑓Convex > 𝑓Convex  =⇒ 𝛼 (𝜙 (𝑓Sem    ) − 𝜙 (𝑓Sem   )) + (𝜔 (𝑓Lex   ) − 𝜔 (𝑓Lex )) > 𝜔 (𝑓Lex   ) − 𝜔 (𝑓Lex  )
                               |        {z           } |              {z         }
                                              Δ𝜙𝑖 𝑗                         Δ𝜔 𝑗𝑖

   This holds if and only if we have the following:
                                            Δ𝜙
                                𝛼 > 1/(1 + Δ𝜔𝑖𝑗𝑖𝑗 ), if Δ𝜙𝑖 𝑗 + Δ𝜔 𝑗𝑖 > 0,
                              (
                                                      Δ𝜙                                                   (6)
                                     𝛼 < 1/(1 + Δ𝜔𝑖𝑗𝑖𝑗 ),   otherwise.
   Observe that, because of the monotonicity of a convex combination and the monotonicity of
the normalization functions, the case Δ𝜙𝑖 𝑗 < 0 and Δ𝜔 𝑗𝑖 > 0 (which implies that the semantic and
lexical scores of 𝑑 𝑗 are both larger than 𝑑𝑖 ) is not valid as it leads to a reversal of ranks. Similarly,
the opposite case Δ𝜙𝑖 𝑗 > 0 and Δ𝜔 𝑗𝑖 < 0 always leads to the correct order regardless of the weight
in the convex combination. We consider the other two cases separately below.
   Case 1: Δ𝜙𝑖 𝑗 > 0 and Δ𝜔 𝑗𝑖 > 0. Because of the monotonicity property, we can deduce that
Δ𝜙𝑖′𝑗 > 0 and Δ𝜔 𝑗𝑖′ > 0. From Equation (6), for the order between 𝑑𝑖 and 𝑑 𝑗 to be preserved under
                ′
the image of 𝑓Convex   , we must therefore have the following:
                                                              Δ𝜙𝑖′𝑗
                                               𝛼 ′ > 1/(1 +            ).
                                                              Δ𝜔 𝑗𝑖′
12                                                                               Sebastian Bruch, Siyu Gai, and Amir Ingber


By assumption, using Definition 4.4, we observe that:
                                     Δ𝜙𝑖′𝑗         Δ𝜔 𝑗𝑖′        Δ𝜙𝑖′𝑗         Δ𝜙𝑖 𝑗
                                             ≥              =⇒             ≥         .
                                     Δ𝜙𝑖 𝑗         Δ𝜔 𝑗𝑖         Δ𝜔 𝑗𝑖′        Δ𝜔 𝑗𝑖
As such, the lower-bound on 𝛼 ′ imposed by documents 𝑑𝑖 and 𝑑 𝑗 of query 𝑞, 𝐿𝑖′𝑗 (𝑞), is smaller than
the lower-bound on 𝛼, 𝐿𝑖 𝑗 (𝑞). Like 𝛼, this case does not additionally constrain 𝛼 ′ from above (i.e.,
the upper-bound does not change: 𝑈𝑖′𝑗 (𝑞) = 𝑈𝑖 𝑗 (𝑞) = 1).
  Case 2: Δ𝜙𝑖 𝑗 < 0, Δ𝜔 𝑗𝑖 < 0. Once again, due to monotonicity, it is easy to see that Δ𝜙𝑖′𝑗 < 0 and
Δ𝜔 𝑗𝑖′ < 0. Equation (6) tells us that, for the order to be preserved under 𝑓Convex
                                                                              ′     , we must similarly
have that:
                                              ′
                                                         Δ𝜙𝑖′𝑗
                                            𝛼 < 1/(1 +          ).
                                                         Δ𝜔 𝑗𝑖′
Once again, by assumption we have that the upper-bound on 𝛼 ′ is a translation of the upper-bound
on 𝛼 to the left. The lower-bound is unaffected and remains 0.
        ′
  For 𝑓Convex  to induce the same order as 𝑓Convex among all pairs of documents for all queries in 𝑄,
the intersection of the intervals produced by the constraints on 𝛼 ′ has to be non-empty:
                       Ù
                  𝐼′ ≜    [max 𝐿𝑖′𝑗 (𝑞), min 𝑈𝑖′𝑗 (𝑞)] = [max 𝐿𝑖′𝑗 (𝑞), min 𝑈𝑖′𝑗 (𝑞)] ≠ ∅.
                              𝑖𝑗              𝑖𝑗                   𝑞,𝑖 𝑗            𝑞,𝑖 𝑗
                        𝑞
We next prove that 𝐼 ′ is always non-empty to conclude the proof of the theorem.
  By Equation (6) and the existence of 𝛼, we know that max𝑞,𝑖 𝑗 𝐿𝑖 𝑗 (𝑞) ≤ min𝑞,𝑖 𝑗 𝑈𝑖 𝑗 (𝑞). Suppose
that documents 𝑑𝑖 and 𝑑 𝑗 of query 𝑞 1 maximize the lower-bound, and that documents 𝑑𝑚 and 𝑑𝑛 of
query 𝑞 2 minimize the upper-bound. We therefore have that:
                                   Δ𝜙𝑖 𝑗            Δ𝜙𝑚𝑛      Δ𝜙𝑖 𝑗   Δ𝜙𝑚𝑛
                        1/(1 +           ) ≤ 1/(1 +      ) =⇒       ≥
                                   Δ𝜔 𝑗𝑖            Δ𝜔𝑛𝑚      Δ𝜔 𝑗𝑖   Δ𝜔𝑛𝑚
Because of the uniformity of the relative expansion rate, we can deduce that:
                            Δ𝜙𝑖′𝑗          Δ𝜙𝑚𝑛
                                             ′
                                     ≥          =⇒ max 𝐿𝑖′𝑗 (𝑞) ≤ min 𝑈𝑖′𝑗 (𝑞).
                            Δ𝜔 𝑗𝑖′         Δ𝜔𝑛𝑚
                                             ′     𝑞,𝑖 𝑗          𝑞,𝑖 𝑗

                                                                                                                         □
   It is easy to show that the theorem above also holds when the condition is updated to reflect a
shift of lower- and upper-bounds to the right, which happens when 𝜙 ′ contracts with respect to 𝜙
more rapidly than 𝜔 ′ does with respect to 𝜔.
   The picture painted by Theorem 4.5 is that switching from min-max scaling to z-score nor-
malization or any other linear transformation that is bounded and does not severely distort the
distribution of scores, especially among the top-ranking documents, results in a rank-equivalent
function. At most, for any given value of the ranking metric of interest such as NDCG, we should
observe a shift of the weight in the convex combination to the right or left. Figure 3 illustrates this
effect empirically on select datasets. As anticipated, the peak performance in terms of NDCG shifts
to the left or right depending on the type of normalization.
   The uniformity requirement on the relative expansion rate, 𝜆, in Theorem 4.5 is not as strict and
restrictive as it may appear. First, it is only necessary for 𝜆 to be stable on the set of ordered pairs
of documents as ranked by 𝑓Convex :
                      |Δ𝜙𝑖′𝑗 |/|Δ𝜙𝑖 𝑗 |
                                           = 𝜆, ∀(𝑑𝑖 , 𝑑 𝑗 ) st 𝑓Convex (𝑑𝑖 ) > 𝑓Convex (𝑑 𝑗 ).
                      |Δ𝜔 𝑗𝑖′ |/|Δ𝜔 𝑗𝑖 |
An Analysis of Fusion Functions for Hybrid Retrieval                                                         13




                       (a) MS MARCO                                       (b) Quora




                        (c) HotpotQA                                       (d) FiQA

   Fig. 3. Effect of normalization on the performance of 𝑓Convex as a function of 𝛼 on the validation set.



Second, as we will observe experimentally, 𝜆 being concentrated around one value, rather than being
the same constant everywhere as uniformity requires, is often sufficient for the effect to materialize
in practice. We observe this phenomenon empirically by fixing the parameter 𝛼 in 𝑓Convex with one
transformation and forming ranked lists, then choosing another transformation and computing
its relative expansion rate 𝜆 on all ordered pairs of documents. We show the measured relative
expansion rate in Figure 4 for various transformations.
   Figure 4 shows that most pairs of transformations yield a stable relative expansion rate. For
                                     ′
example, if 𝑓Convex uses 𝜙 tmm and 𝑓Convex  uses 𝜙 mm —denoted by 𝜙 tmm → 𝜙 mm —for every choice of 𝛼,
the relative expansion rate 𝜆 is concentrated around a constant value. This implies that any ranked
                                                        ′
list obtained from 𝑓Convex can be reconstructed by 𝑓Convex    . Interestingly, 𝜙 z−Lex → 𝜙 mm−Lex has a
comparatively less stable 𝜆, but removing normalization altogether (i.e., 𝜙 mm−Lex → 𝐼 ) dramatically
distorts the expansion rates. This goes some way to explain why normalization and boundedness
are important properties.
   This connection between boundedness and the effect that changing the normalization function
has on ranking quality, is clearer in the experiments presented in Appendix A through Appendix D.
14                                                                     Sebastian Bruch, Siyu Gai, and Amir Ingber




                      (a) MS MARCO                                          (b) Quora




                       (c) HotpotQA                                          (d) FiQA

Fig. 4. Relative expansion rate of semantic scores with respect to lexical scores, 𝜆, when changing from one
transformation to another, with 95% confidence intervals. Prior to visualization, we normalize values of 𝜆
to bring them into a similar scale—this only affects aesthetics and readability, but is the reason why the
vertical axis is not scaled. For most transformations and every value of 𝛼, we observe a stable relative rate of
expansion where 𝜆 concentrates around one value for the vast majority of queries.




In general, when a function is unbounded, fusing with normalization versus without results in
a relative expansion rate 𝜆 with a high variance, which leads to relatively different classes of
rankings: there exists ranked lists which are produced by a fusion with normalization that cannot
be reconstructed by a fusion without normalization. For pairs of normalization functions whose
relative expansion rate is stable and highly concentrated, on the other hand, the curves showing
the effect of 𝛼 on 𝑓Convex are translations of each other, as Theorem 4.5 predicts: every ranked
list produced by a fusion using one normalization function can be reproduced by a fusion using
another.
   In the last two sections, we have answered RQ1: convex combination is an appropriate fusion
function and its performance is not sensitive to the choice of normalization so long as the transfor-
mation has reasonable properties. Interestingly, the behavior of 𝜙 tmm appears to be more robust to
An Analysis of Fusion Functions for Hybrid Retrieval                                                15


the data distribution—its peak remains within a small neighborhood as we move from one dataset
to another. We believe the reason 𝜙 tmm -normalized scores are more stable is because it has one
fewer data-dependent statistic in the transformation (i.e., minimum score in the retrieved set is
replaced with minimum feasible value regardless of the candidate set). In the remainder of this
work, we use 𝜙 tmm and denote a convex combination of scores normalized by it by TM2C2 for
brevity. Where the theoretical minimum does not exist (e.g., with the Tas-B model), we use 𝜙 mm
instead and denote it by M2C2.

5 ANALYSIS OF RECIPROCAL RANK FUSION
Chen et al. [5] show that RRF performs better and more reliably than a convex combination of
normalized scores. RRF is computed as follows:
                                                       1                      1
                                 𝑓RRF (𝑞, 𝑑) =                     +                      ,        (7)
                                                 𝜂 + 𝜋Lex (𝑞, 𝑑)       𝜂 + 𝜋 Sem (𝑞, 𝑑)
where 𝜂 is a free parameter. The authors of [5] take a non-parametric view of RRF, where the
parameter 𝜂 is set to its default value 60, in order to apply the fusion to out-of-domain datasets
in a zero-shot manner. In this work, we additionally take a parametric view of RRF, where as we
elaborate later, the number of free parameters is the same as the number of functions being fused
together, a quantity that is always larger than the number of parameters in a convex combination.
   Let us begin by comparing the performance of RRF and TM2C2 empirically to get a sense of their
relative efficacy. We first verify whether hybrid retrieval leads to significant gains in in-domain and
out-of-domain experiments. In a way, we seek to confirm the findings reported in [5] and compare
the two fusion functions in the process.
   Table 2 summarizes our results for our primary models, with results for the remaining fusions
reported in the appendices. We note that, we set RRF’s 𝜂 to 60 per [5] but tuned TM2C2’s 𝛼 on the
validation set of the in-domain datasets and found that 𝛼 = 0.8 works well for the three datasets.
In the experiments leading to Table 2, we fix 𝛼 = 0.8 and evaluate methods on the test split of
the datasets. Per [5, 40], we have also included the performance of an oracle system that uses a
per-query 𝛼, to establish an upper-bound—the oracle knows which value of 𝛼 works best for any
given query.
   Our results show that hybrid retrieval using RRF outperforms pure-lexical and pure-semantic
retrieval on most datasets. This fusion method is particularly effective on out-of-domain datasets,
rendering the observation of [5] a robust finding and asserting once more the remarkable perfor-
mance of RRF in zeros-shot settings.
   Contrary to [5], however, we find that TM2C2 significantly outperforms RRF on all datasets
in terms of NDCG, and does generally better in terms of Recall. Our observation is consistent
with [40] that TM2C2 substantially boosts NDCG even on in-domain datasets.
   To contextualize the effect of 𝛼 on ranking quality, we visualize a parameter sweep on the
validation split of in-domain datasets in Figure 5(a), and for completeness, on the test split of
out-of-domain datasets in Figure 5(b). These figures also compare the performance of TM2C2 with
RRF by reporting the difference between NDCG of the two methods. These plots show that there
always exists an interval of 𝛼 for which 𝑓TM2C2 ≻ 𝑓RRF with ≻ indicating better rank quality.

5.1   Effect of Parameters
Chen et al. [5] rightly argue that because RRF is merely a function of ranks, rather than scores,
it naturally addresses the scale and range problem without requiring normalization—which, as
we showed, is not a consequential choice anyway. While that statement is accurate, we believe it
introduces new problems that must be recognized too.
16                                                                     Sebastian Bruch, Siyu Gai, and Amir Ingber


Table 2. Recall@1000 and NDCG@1000 (except SciFact and NFCorpus where cutoff is 100) on the test split
of various datasets for lexical and semantic search as well as hybrid retrieval using RRF [5] (𝜂 = 60) and
TM2C2 (𝛼 = 0.8). The symbols ‡ and ∗ indicate statistical significance (𝑝-value < 0.01) with respect to TM2C2
and RRF respectively, according to a paired two-tailed 𝑡-test.

                                     Recall                                         NDCG
             Dataset    Lex.      Sem.     TM2C2     RRF       Lex.        Sem.      TM2C2       RRF      Oracle
                       0.836‡∗   0.964‡∗           0.969‡    0.309‡∗     0.441‡∗                0.425‡

in-domain
            MS MARCO                       0.974                                     0.454                 0.547
               NQ      0.886‡∗   0.978‡∗   0.985   0.984     0.382‡∗     0.505‡      0.542      0.514‡     0.637
             Quora     0.992‡∗    0.999    0.999   0.999     0.800‡∗     0.889‡∗     0.901      0.877‡     0.936

            NFCorpus   0.255‡∗   0.320‡∗   0.338    0.327    0.268‡∗     0.296‡∗     0.327      0.312‡     0.371
                       0.878‡∗   0.756‡∗   0.884             0.682‡∗     0.520‡∗                0.675‡     0.767

zero-shot
            HotpotQA                                0.888                            0.699
              FEVER    0.969‡∗   0.931‡∗   0.972    0.972    0.689‡∗     0.558‡∗     0.744      0.721‡     0.814
             SciFact   0.900‡∗   0.932‡∗   0.958    0.955    0.698‡∗     0.681‡∗     0.753      0.730‡     0.796
             DBPedia   0.540‡∗   0.408‡∗   0.564    0.567    0.415‡∗     0.425‡∗     0.512      0.489‡     0.553
               FiQA    0.720‡∗    0.908    0.907    0.904    0.315‡∗     0.467‡      0.496      0.464‡     0.561




                         (a) in-domain                                  (b) out-of-domain

Fig. 5. Difference in NDCG@1000 of TM2C2 and RRF (positive indicates better ranking quality by TM2C2)
as a function of 𝛼. When 𝛼 = 0 the model is rank-equivalent to lexical search while 𝛼 = 1 is rank-equivalent
to semantic search.



  The first, more minor issue is that ranks cannot be computed exactly unless the entire collection
D is ranked by retrieval system o for every query. That is because, there may be documents that
appear in the union set, but not in one of the individual top-𝑘 sets. Their true rank is therefore
unknown, though is often approximated by ranking documents within the union set. We take this
approach when computing ranks.
  The second issue is that, unlike TM2C2, RRF ignores the raw scores and discards information
about their distribution. In this regime, whether or not a document has a low or high semantic score
does not matter so long as its rank in 𝑅𝑘Sem stays the same. It is arguable in this case whether rank is
An Analysis of Fusion Functions for Hybrid Retrieval                                                       17


a stronger signal of relevance than score, a measurement in a metric space where distance matters
greatly. We intuit that, such distortion of distances may result in a loss of valuable information that
would lead to better final ranked lists.
   To understand these issues better, let us first repeat the exercise in Section 4.1 for RRF. In Figure 6,
we have plotted the reciprocal rank (i.e., 𝑟𝑟 (𝜋o ) = 1/(𝜂 + 𝜋o ) with 𝜂 = 60) for sampled query-
document pairs as before. We choose 𝜂 = 60 per the setup in [5], but note that changing this value
leads to different distributions: as 𝜂 approaches ∞, for example, all scores will collapse to a single
point regardless of the original ranks (𝜋 o ). From the figure, we can see that samples are pulled
towards one of the poles at (0, 0) and (1/61, 1/61). The former attracts a higher concentration of
negative samples while the latter positive samples. While this separation is somewhat consistent
across datasets, the concentration around poles and axes changes. Indeed, on HotpotQA and
Fever there is a higher concentration of positive documents near the top, whereas on FiQA and
the in-domain datasets more positive samples end up along the vertical line at 𝑟𝑟 (𝜋Sem ) = 1/61,
indicating that lexical ranks matter less. This suggests that a simple addition of reciprocal ranks
does not behave consistently across domains.
   We argued earlier that RRF is parametric and that it, in fact, has as many parameters as there are
retrieval functions to fuse. To see this more clearly, let us rewrite Equation (7) as follows:
                                                      1                    1
                             𝑓RRF (𝑞, 𝑑) =                       +                    .                   (8)
                                             𝜂 Lex + 𝜋 Lex (𝑞, 𝑑) 𝜂 Sem + 𝜋Sem (𝑞, 𝑑)
   We study the effect of parameters on 𝑓RRF by comparing the NDCG obtained from RRF with a
particular choice of 𝜂 Lex and 𝜂 Sem against a realization of RRF with 𝜂 Lex = 𝜂 Sem = 60. In this way,
we are able to visualize the impact on performance relative to the baseline configuration that is
typically used in the literature. This difference in NDCG is rendered as a heatmap in Figure 7 for
select datasets—figures for all other datasets show a similar pattern. We note that, we select 𝜂 Lex
and 𝜂 Sem from the set {1, 2, . . . , 100}, but selectively illustrated a subset of values in Figure 7 to make
the figures more readable; the omitted combinations of 𝜂 Lex and 𝜂 Sem do not bring more insight
than what can already be deduced from these figures.
   As a general observation, we note that NDCG swings wildly as a function of RRF parameters.
Crucially, performance improves off-diagonal, where the parameter takes on different values for
the semantic and lexical components. On MS MARCO, shown in Figure 7(a), NDCG improves when
𝜂 Lex > 𝜂 Sem , while the opposite effect can be seen for HotpotQA, an out-of-domain dataset. This
can be easily explained by the fact that increasing 𝜂 o for retrieval system o effectively discounts the
contribution of ranks from o to the final hybrid score. On in-domain datasets where the semantic
model already performs strongly, for example, discounting the lexical system by increasing 𝜂 Lex
leads to better performance.
   Having observed that tuning RRF potentially leads to gains in NDCG, we ask if tuned parameters
generalize on out-of-domain datasets. To investigate that question, we tune RRF on in-domain
datasets and pick the value of parameters that maximize NDCG on the validation split of in-domain
datasets, and measure the performance of the resulting function on the test split of all (in-domain
and out-of-domain) datasets. We present the results in Table 3. While tuning a parametric RRF does
indeed lead to gains in NDCG on in-domain datasets, the tuned function does not generalize well
to out-of-domain datasets.
   The poor generalization can be explained by the reversal of patterns observed in Figure 7 where
𝜂 Lex > 𝜂 Sem suits in-domain datasets better but the opposite is true for out-of-domain datasets. By
modifying 𝜂 Lex and 𝜂 Sem we modify the fusion of ranks and boost certain regions and discount
others in an imbalanced manner. Figure 8 visualizes this effect on 𝑓RRF for particular values of its
parameters. This addresses RQ2.
18                                                                   Sebastian Bruch, Siyu Gai, and Amir Ingber




                          (a) MS MARCO                               (b) Quora




                               (c) NQ                                 (d) FiQA




                           (e) HotpotQA                               (f) Fever

Fig. 6. Visualization of the reciprocal rank determined by lexical (𝑟𝑟 (𝜋Lex ) = 1/(60 + 𝜋Lex )) and semantic
(𝑟𝑟 (𝜋 Sem ) = 1/(60 + 𝜋Sem )) retrieval for query-document pairs sampled from the validation split of each
dataset. Shown in red are up to 20,000 positive samples where document is relevant to query, and in black up
to the same number of negative samples.




5.2   Effect of Lipschitz Continuity
In the previous section, we stated an intuition that because RRF does not preserve the distribution
of raw scores, it loses valuable information in the process of fusing retrieval systems. In our final
research question, RQ3, we investigate if this indeed matters in practice.
An Analysis of Fusion Functions for Hybrid Retrieval                                                                                    19




                               (a) MS MARCO                                         (b) HotpotQA

Fig. 7. Difference in NDCG@1000 of 𝑓RRF with distinct values 𝜂 Lex and 𝜂 Sem , and 𝑓RRF with 𝜂 Lex = 𝜂 Sem = 60
(positive indicates better ranking quality by the former). On MS MARCO, an in-domain dataset, NDCG
improves when 𝜂 Lex > 𝜂 Sem , while the opposite effect can be seen for HotpotQA, an out-of-domain dataset.




        (a) 𝜂 Lex = 60, 𝜂 Sem = 60                 (b) 𝜂 Lex = 10, 𝜂 Sem = 4                        (c) 𝜂 Lex = 3, 𝜂 Sem = 5

Fig. 8. Effect of 𝑓RRF with select configurations of 𝜂 Lex and 𝜂 Sem on pairs of ranks from lexical and semantic
systems. When 𝜂 Lex > 𝜂 Sem , the fusion function discounts the lexical system’s contribution.




   The notion of “preserving” information is well captured by the concept of Lipschitz continuity.9
When a function is Lipschitz continuous with a small Lipschitz constant, it does not oscillate wildly
with a small change to its input. Intuitively, and in the context of this work, this means that a small
change to the individual scores does not lead to a sudden and exaggerated effect on the fused score;
the fusion function does not dramatically distort the distribution of scores or ranks, an effect we
characterize informally as “preserving information.” RRF does not have this property because the
moment one lexical (or semantic) score becomes larger than another the function makes a hard
transition to a new value.

9 A function 𝑓 is Lipschitz continous with constant 𝐿 if | |𝑓 (𝑦) − 𝑓 (𝑥) | |
                                                                                𝑜 ≤ 𝐿 | |𝑦 − 𝑥 | |𝑖 for some norm | | · | |𝑜 and | | · | |𝑖
on the output and input space of 𝑓 .
20                                                                           Sebastian Bruch, Siyu Gai, and Amir Ingber


Table 3. Mean NDCG@1000 (NDCG@100 for SciFact and NFCorpus) on the test split of various datasets
for hybrid retrieval using TM2C2 (𝛼 = 0.8) and RRF (𝜂 Lex , 𝜂 Sem ). The symbols ‡ and ∗ indicate statistical
significance (𝑝-value < 0.01) with respect to TM2C2 and baseline RRF (60, 60) respectively, according to a
paired two-tailed 𝑡-test.

                                                                    NDCG
                              Dataset     TM2C2        RRF (60, 60)      RRF (5, 5)        RRF (10, 4)
                                                           0.425‡          0.435‡∗          0.451∗

                 in-domain
                             MS MARCO      0.454
                                NQ         0.542           0.514‡          0.521‡∗          0.528‡∗
                              Quora        0.901           0.877‡          0.885‡∗          0.896∗

                             NFCorpus      0.327           0.312‡          0.318‡∗          0.310‡
                             HotpotQA                      0.675‡          0.693∗           0.621‡∗

                 zero-shot
                                           0.699
                               FEVER       0.744           0.721‡          0.727‡∗          0.649‡∗
                              SciFact      0.753           0.730‡          0.738‡           0.715‡∗
                              DBPedia      0.512           0.489‡          0.489‡           0.480‡∗
                                FiQA       0.496           0.464‡          0.470‡∗          0.482‡∗



   We can therefore cast RQ3 as a question of whether Lipschitz continuity is an important property
in practice. To put that hypothesis to the test, we design a smooth approximation of RRF using
known techniques [4, 31].
   As expressed in Equation (1), the rank of a document is simply the sum of indicators. It is
thus trivial to approximate this quantity using a generalized sigmoid with parameter 𝛽: 𝜎𝛽 (𝑥) =
1/(1 + exp(−𝛽𝑥)). As 𝛽 approaches 1, the sigmoid takes its usual S shape, while 𝛽 → ∞ produces a
very close approximation of the indicator. Interestingly, the Lipschitz constant of 𝜎𝛽 (·) is, in fact,
𝛽. As 𝛽 increases, the approximation of ranks becomes more accurate, but the Lipschitz constant
becomes larger. When 𝛽 is too small, however, the approximation breaks down but the function
transitions more slowly, thereby preserving much of the characteristics of the underlying data
distribution.
   RRF being a function of ranks can now be approximated by plugging in approximate ranks in
Equation (7), resulting in SRRF:
                                                           1                 1
                                  𝑓SRRF (𝑞, 𝑑) =                    +                  ,                           (9)
                                                   𝜂 + 𝜋˜ Lex (𝑞, 𝑑) 𝜂 + 𝜋˜ Sem (𝑞, 𝑑)
                           Í
where 𝜋˜ o (𝑞, 𝑑𝑖 ) = 0.5 + 𝑑 𝑗 ∈𝑅𝑘o (𝑞) 𝜎𝛽 (𝑓o (𝑞, 𝑑 𝑗 ) − 𝑓o (𝑞, 𝑑𝑖 )). By increasing 𝛽 we increase the Lipschitz
constant of 𝑓SRRF . This is the lever we need to test the idea that Lipschitz continuity matters and
that functions that do not distort the distributional properties of raw scores lead to better ranking
quality.
   Figures 9 and 10 visualize the difference between SRRF and RRF for two settings of 𝜂 selected
based on the results in Table 3. As anticipated, when 𝛽 is too small, the approximation error is
large and ranking quality degrades. As 𝛽 becomes larger, ranking quality trends in the direction
of RRF. Interestingly, as 𝛽 becomes gradually smaller, the performance of SRRF improves over
the RRF baseline. This effect is more pronounced for the 𝜂 = 60 setting of RRF, as well as on the
out-of-domain datasets. Empirical evidence reported for other fusions in Appendices A through D
shows this finding to be robust.
An Analysis of Fusion Functions for Hybrid Retrieval                                                     21




                        (a) in-domain                                 (b) out-of-domain

Fig. 9. The difference in NDCG@1000 of 𝑓SRRF and 𝑓RRF with 𝜂 = 60 (positive indicates better ranking quality
by SRRF) as a function of 𝛽.




                        (a) in-domain                                 (b) out-of-domain

Fig. 10. The difference in NDCG@1000 of 𝑓SRRF and 𝑓RRF with 𝜂 = 5 (positive indicates better ranking quality
by SRRF) as a function of 𝛽.




   While we acknowledge the possibility that the approximation in Equation (9) may cause a change
in ranking quality, we expected that change to be a degradation, not an improvement. However,
given we do observe gains by smoothing the function, and that the only other difference between
SRRF and RRF is their Lipschitz constant, we believe these results highlight the role of Lipschitz
continuity in ranking quality. For completeness, we have also included a comparison of SRRF, RRF,
and TM2C2 in Table 4.
22                                                                 Sebastian Bruch, Siyu Gai, and Amir Ingber


Table 4. Mean NDCG@1000 (NDCG@100 for SciFact and NFCorpus) on the test split of various datasets
for hybrid retrieval using TM2C2 (𝛼 = 0.8), RRF (𝜂), and SRRF(𝜂, 𝛽). The parameters 𝛽 are fixed to values
that maximize NDCG on the validation split of in-domain datasets. The symbols ‡ and ∗ indicate statistical
significance (𝑝-value < 0.01) with respect to TM2C2 and RRF respectively, according to a paired two-tailed
𝑡-test.

                                              NDCG
                       Dataset   TM2C2    RRF(60)    SRRF (60, 40)    RRF(5)     SRRF (5, 100)
                                           0.425‡       0.431‡∗       0.435‡        0.431‡∗

          in-domain
                      MS MARCO   0.454
                         NQ      0.542     0.514‡        0.516‡       0.521‡        0.517‡
                       Quora     0.901     0.877‡       0.889‡∗       0.885‡        0.889‡∗

                      NFCorpus   0.327     0.312‡       0.323‡∗       0.318‡         0.322‡
                      HotpotQA   0.699     0.675‡       0.695∗        0.693‡        0.705‡∗

          zero-shot
                        FEVER    0.744     0.721‡       0.725‡        0.727‡        0.735‡∗
                       SciFact   0.753     0.730‡       0.740‡        0.738‡         0.740‡
                       DBPedia   0.512     0.489‡       0.501‡∗       0.489‡         0.492‡
                         FiQA    0.496     0.464‡       0.468‡        0.470‡         0.469‡



6    DISCUSSION
The analysis in this work motivates us to identify and document the properties of a well-behaved
fusion function, and present the principles that, we hope, will guide future research in this space.
These desiderata are stated below.
   Monotonicity: When 𝑓o is positively correlated with a target ranking metric (i.e., ordering
documents in decreasing order of 𝑓o must lead to higher quality), then it is natural to require
that 𝑓Hybrid be monotone increasing in its arguments. We have already seen and indeed used this
property in our analysis of the convex combination fusion function. It is trivial to show why this
property is crucial.
   Homogeneity: The order induced by a fusion function must be unaffected by a positive re-
                                                               𝜋                 𝜋
scaling of query and document vectors. That is: 𝑓Hybrid (𝑞, 𝑑) = 𝑓Hybrid (𝑞, 𝛾𝑑) = 𝑓Hybrid (𝛾𝑞, 𝑑) where
𝜋
= denotes rank-equivalence and 𝛾 > 0. This property prevents any retrieval system from inflating
its contribution to the final hybrid score by simply boosting its document or query vectors.
   Boundedness: Recall that, a convex combination without score normalization is often ineffective
and inconsistent because BM25 is unbounded and that lexical and semantic scores are on different
scales. To see this effect we turn to Figure 11.
   We observe in Figure 11(a) that, for in-domain datasets, adding the unnormalized lexical scores
using a convex combination leads to a severe degradation of ranking quality. We believe this
is because of the fact that the semantic retrieval model, which is fine-tuned on these datasets,
already produces ranked lists of high quality, and that adding the lexical scores which are on a very
different scale distorts the rankings and leads to poor performance. In out-of-domain experiments
as shown in Figure 11(b), however, the addition of lexical scores leads to often significant gains
in quality. We believe this can be explained exactly as the in-domain observations: the semantic
model generally does poorly on out-of-domain datasets while the lexical retriever does well. But
because the semantic scores are bounded and relatively small, they do not significantly distort the
rankings produced by the lexical retriever.
An Analysis of Fusion Functions for Hybrid Retrieval                                                  23




                        (a) in-domain                               (b) out-of-domain

Fig. 11. The difference in NDCG of convex combination of unnormalized scores and a pure semantic search
(positive indicates better ranking quality by a convex combination) as a function of 𝛼.




   To avoid that pitfall, we require that 𝑓Hybrid be bounded: |𝑓Hybrid | ≤ 𝑀 for some 𝑀 > 0. As we
have seen before, normalizing the raw scores addresses this issue.
   Lipschitz Continuity: We argued that because RRF does not take into consideration the raw
scores, it distorts their distribution and thereby loses valuable information. On the other hand,
TM2C2 (or any convex combination of scores) is a smooth function of scores and preserves much
of the characteristics of its underlying distribution. We formalized this idea using the notion of
Lipschitz continuity: A larger Lipschitz constant leads to a larger distortion of retrieval score
distribution.
   Interpretability and Sample Efficiency: The question of hybrid retrieval is an important topic
in IR. What makes it particularly pertinent is its zero-shot applicability, a property that makes
deep models reusable, reducing computational costs and emissions as a result [3, 35], and enabling
resource-constrained research labs to innovate. Given the strong evidence supporting the idea that
hybrid retrieval is most valuable when applied to out-of-domain datasets [5], we believe that 𝑓Hybrid
should be robust to distributional shifts and should not need training or fine-tuning on target
datasets. This implies that either the function must be non-parametric, that its parameters can be
tuned efficiently with respect to the training samples required, or that they are highly interpretable
such that their value can be guided by expert knowledge.
   In the absence of a truly non-parametric approach, however, we believe a fusion that is more
sample-efficient to tune is preferred. Because convex combination has fewer parameters than the
fully parameterized RRF, we believe it should have this property. To confirm, we ask how many
training queries it takes to converge to the correct 𝛼 on a target dataset.
   Figure 12 visualizes our experiments, where we plot NDCG of RRF (𝜂 = 60) and TM2C2 with
𝛼 = 0.8 from Table 2. Additionally, we take the train split of each dataset and sample from it
progressively larger subsets (with a step size of 5%), and use it to tune the parameters of each
function. We then measure NDCG of the tuned functions on the test split. For the depicted datasets
as well as all other datasets in this work, we observe a similar trend: with less than 5% of the training
data, which is often a small set of queries, TM2C2’s 𝛼 converges, regardless of the magnitude of
domain shift. This sample efficiency is remarkable because it enables significant gains with little
24                                                                      Sebastian Bruch, Siyu Gai, and Amir Ingber




                      (a) MS MARCO                                           (b) Quora




                       (c) HotpotQA                                           (d) Fever




                        (e) NFCorpus                                           (f) FiQA

Fig. 12. Sample efficiency of TM2C2 and the parameterized variants of RRF (single parameter where 𝜂 Sem =
𝜂 Lex , and two parameters where we allow different values of 𝜂 Sem and 𝜂 Lex , and a third variation that is a
convex combination of RRF terms defined in Equation 10). We sample progressively larger subsets of the
training set (with a step size of 5%), tune the parameters of each function on the resulting set, and evaluate the
resulting function on the test split. These figures depict NDCG@1000 as a function of the size of the tuning
set, averaged over 5 trials with the shaded regions illustrating the 95% confidence intervals. For reference, we
have also plotted NDCG on the test split for RRF (𝜂 = 60) and TM2C2 with 𝛼 = 0.8 from Table 2.
An Analysis of Fusion Functions for Hybrid Retrieval                                                25


labeling effort. Finally, while RRF does not settle on a value and its parameters are sensitive to the
training sample, its performance does more or less converge. However, the performance of the
fully parameterized RRF is still sub-optimal compared with TM2C2.
   In Figure 12, we also include a convex combination of fully parameterized RRF terms, denoted
by RRF-CC and defined as:
                                                     1                      1
                      𝑓RRF (𝑞, 𝑑) = (1 − 𝛼)                     +𝛼                     ,          (10)
                                            𝜂 Lex + 𝜋Lex (𝑞, 𝑑)    𝜂 Sem + 𝜋Sem (𝑞, 𝑑)
where 𝛼, 𝜂 Lex , and 𝜂 Sem are tunable parameters. The question this particular formulation tries to
answer is whether adding an additional weight to the combination of the RRF terms affects retrieval
quality. From the figure, it is clear that the addition of this parameter does not have a significant
impact on the overall performance. This also serves as additional evidence supporting the claim
that Lipschitz continuity is an important property.

7   CONCLUSION
We studied the behavior of two popular functions that fuse together lexical and semantic retrieval
to produce hybrid retrieval, and identified their advantages and pitfalls. Importantly, we inves-
tigated several questions and claims in prior work. We established theoretically that the choice
of normalization is not as consequential as once thought for a convex combination-based fusion
function. We found that RRF is sensitive to its parameters. We also observed empirically that convex
combination of normalized scores outperforms RRF on in-domain and out-of-domain datasets—a
finding that is in disagreement with [5].
   We believe that a convex combination with theoretical minimum-maximum normalization
(TM2C2) indeed enjoys properties that are important in a fusion function. Its parameter, too,
can be tuned sample-efficiently or set to a reasonable value based on domain knowledge. In our
experiments, for example, we found the range 𝛼 ∈ [0.6, 0.8] to consistently lead to improvements.
   While we observed that a line appears to be appropriate for a collection of query-document pairs,
we acknowledge that, that may change if our analysis was conducted on a per-query basis—itself a
rather non-trivial effort. For example, it is unclear if bringing non-linearity to the design of the
fusion function or the normalization itself leads to a more accurate prediction of 𝛼 on a per-query
basis. We leave an exploration of this question to future work.
   We also note that, while our analysis does not exclude the use of multiple retrieval engines as
input, and indeed can be extended, both theoretically and empirically, to a setting where we have
more than just lexical and semantic scores, it is nonetheless important to conduct experiments
and validate that our findings generalize. In particular, we ask if the role of normalization changes
when fusing three or more models, and if so, what is the behavior of convex combination given
a particular normalization function, and how does that compare with RRF. We believe, however,
that our current assumptions are practical and are reflective of the current state of hybrid search
where we typically fuse only lexical and semantic retrieval systems. As such, we leave an extended
analysis of fusion on multiple retrieval systems to future work.

ACKNOWLEDGMENTS
We benefited greatly from conversations with Brian Hentschel, Edo Liberty, and Michael Bendersky.
We are grateful to them for their insight and time. We further thank the anonymous reviewers for
their meticulous examination of our claims and for their insightful feedback.
26                                                                             Sebastian Bruch, Siyu Gai, and Amir Ingber


REFERENCES
 [1] Nima Asadi. 2013. Multi-Stage Search Architectures for Streaming Documents. University of Maryland.
 [2] Nima Asadi and Jimmy Lin. 2013. Effectiveness/Efficiency Tradeoffs for Candidate Generation in Multi-Stage Retrieval
     Architectures. In Proceedings of the 36th International ACM SIGIR Conference on Research and Development in Information
     Retrieval (Dublin, Ireland). 997–1000.
 [3] Sebastian Bruch, Claudio Lucchese, and Franco Maria Nardini. 2022. ReNeuIR: Reaching Efficiency in Neural Information
     Retrieval. In Proceedings of the 45th International ACM SIGIR Conference on Research and Development in Information
     Retrieval (Madrid, Spain). 3462–3465.
 [4] Sebastian Bruch, Masrour Zoghi, Michael Bendersky, and Marc Najork. 2019. Revisiting Approximate Metric Optimiza-
     tion in the Age of Deep Neural Networks. In Proceedings of the 42nd International ACM SIGIR Conference on Research
     and Development in Information Retrieval (Paris, France). 1241–1244.
 [5] Tao Chen, Mingyang Zhang, Jing Lu, Michael Bendersky, and Marc Najork. 2022. Out-of-Domain Semantics to the
     Rescue! Zero-Shot Hybrid Retrieval Models. In Advances in Information Retrieval: 44th European Conference on IR
     Research, ECIR 2022, Stavanger, Norway, April 10–14, 2022, Proceedings, Part I (Stavanger, Norway). 95–110.
 [6] Gordon V. Cormack, Charles L A Clarke, and Stefan Buettcher. 2009. Reciprocal Rank Fusion Outperforms Condorcet
     and Individual Rank Learning Methods. In Proceedings of the 32nd International ACM SIGIR Conference on Research and
     Development in Information Retrieval (Boston, MA, USA). 758–759.
 [7] Van Dang, Michael Bendersky, and W Bruce Croft. 2013. Two-Stage learning to rank for information retrieval. In
     Advances in Information Retrieval. Springer, 423–434.
 [8] Jacob Devlin, Ming-Wei Chang, Kenton Lee, and Kristina Toutanova. 2019. BERT: Pre-training of Deep Bidirectional
     Transformers for Language Understanding. In Proceedings of the 2019 Conference of the North American Chapter of the
     Association for Computational Linguistics: Human Language Technologies, Volume 1 (Long and Short Papers). 4171–4186.
 [9] Thibault Formal, Carlos Lassance, Benjamin Piwowarski, and Stéphane Clinchant. 2022. From Distillation to Hard
     Negative Sampling: Making Sparse Neural IR Models More Effective. In Proceedings of the 45th International ACM
     SIGIR Conference on Research and Development in Information Retrieval (Madrid, Spain). 2353–2359.
[10] Sebastian Hofstätter, Sheng-Chieh Lin, Jheng-Hong Yang, Jimmy Lin, and Allan Hanbury. 2021. Efficiently Teaching
     an Effective Dense Retriever with Balanced Topic Aware Sampling. In Proceedings of the 44th International ACM SIGIR
     Conference on Research and Development in Information Retrieval (Virtual Event, Canada). 113–122.
[11] Kalervo Järvelin and Jaana Kekäläinen. 2000. IR evaluation methods for retrieving highly relevant documents. In
     Proceedings of the 23rd annual international ACM SIGIR conference on Research and development in information retrieval.
     ACM, 41–48.
[12] Jeff Johnson, Matthijs Douze, and Hervé Jégou. 2021. Billion-Scale Similarity Search with GPUs. IEEE Transactions on
     Big Data 7 (2021), 535–547.
[13] Vladimir Karpukhin, Barlas Oguz, Sewon Min, Patrick Lewis, Ledell Wu, Sergey Edunov, Danqi Chen, and Wen-tau
     Yih. 2020. Dense Passage Retrieval for Open-Domain Question Answering. In Proceedings of the 2020 Conference on
     Empirical Methods in Natural Language Processing (EMNLP).
[14] Saar Kuzi, Mingyang Zhang, Cheng Li, Michael Bendersky, and Marc Najork. 2020. Leveraging Semantic and Lexical
     Matching to Improve the Recall of Document Retrieval Systems: A Hybrid Approach. (2020). arXiv:2010.01195 [cs.IR]
[15] Hang Li, Shuai Wang, Shengyao Zhuang, Ahmed Mourad, Xueguang Ma, Jimmy Lin, and Guido Zuccon. 2022. To
     Interpolate or Not to Interpolate: PRF, Dense and Sparse Retrievers. In Proceedings of the 45th International ACM SIGIR
     Conference on Research and Development in Information Retrieval (Madrid, Spain). 2495–2500.
[16] Jimmy Lin, Rodrigo Nogueira, and Andrew Yates. 2021. Pretrained Transformers for Text Ranking: BERT and Beyond.
     arXiv:2010.06467 [cs.IR]
[17] Tie-Yan Liu. 2009. Learning to Rank for Information Retrieval. Foundations and Trends in Information Retrieval 3, 3
     (2009), 225–331.
[18] Yi Luan, Jacob Eisenstein, Kristina Toutanova, and Michael Collins. 2021. Sparse, Dense, and Attentional Representations
     for Text Retrieval. Transactions of the Association for Computational Linguistics 9 (2021), 329–345.
[19] Ji Ma, Ivan Korotkov, Keith Hall, and Ryan T. McDonald. 2020. Hybrid First-stage Retrieval Models for Biomedical
     Literature. In CLEF.
[20] Xueguang Ma, Kai Sun, Ronak Pradeep, and Jimmy J. Lin. 2021. A Replication Study of Dense Passage Retriever. (2021).
     arXiv:2004.04906 [cs.CL]
[21] Craig Macdonald, Rodrygo LT Santos, and Iadh Ounis. 2013. The whens and hows of learning to rank for web search.
     Information Retrieval 16, 5 (2013), 584–628.
[22] Yu. A. Malkov and D. A. Yashunin. 2016. Efficient and robust approximate nearest neighbor search using Hierarchical
     Navigable Small World graphs. arXiv:1603.09320 [cs.DS]
[23] Antonio Mallia, Michal Siedlaczek, Joel Mackenzie, and Torsten Suel. 2019. PISA: Performant Indexes and Search for
     Academia. In Proceedings of the Open-Source IR Replicability Challenge co-located with 42nd International ACM SIGIR
An Analysis of Fusion Functions for Hybrid Retrieval                                                                     27


     Conference on Research and Development in Information Retrieval Paris, France, July 25, 2019. 50–56.
[24] Yoshitomo Matsubara, Thuy Vu, and Alessandro Moschitti. 2020. Reranking for Efficient Transformer-Based Answer
     Selection. In Proceedings of the 43rd International ACM SIGIR Conference on Research and Development in Information
     Retrieval. 1577–1580.
[25] Bhaskar Mitra, Eric Nalisnick, Nick Craswell, and Rich Caruana. 2016. A dual embedding space model for document
     ranking. (2016). arXiv:1602.01137 [cs.IR]
[26] Tri Nguyen, Mir Rosenberg, Xia Song, Jianfeng Gao, Saurabh Tiwary, Rangan Majumder, and Li Deng. 2016. MS
     MARCO: A Human Generated MAchine Reading COmprehension Dataset. (November 2016).
[27] Rodrigo Nogueira and Kyunghyun Cho. 2020. Passage Re-ranking with BERT. arXiv:1901.04085 [cs.IR]
[28] Rodrigo Nogueira, Zhiying Jiang, Ronak Pradeep, and Jimmy Lin. 2020. Document Ranking with a Pretrained
     Sequence-to-Sequence Model. In Findings of the Association for Computational Linguistics: EMNLP 2020. 708–718.
[29] Rodrigo Nogueira, Wei Yang, Kyunghyun Cho, and Jimmy Lin. 2019. Multi-stage document ranking with BERT. (2019).
     arXiv:1910.14424 [cs.IR]
[30] Rodrigo Nogueira, Wei Yang, Jimmy Lin, and Kyunghyun Cho. 2019. Document Expansion by Query Prediction. (2019).
     arXiv:1904.08375 [cs.IR]
[31] Tao Qin, Tie-Yan Liu, and Hang Li. 2010. A general approximation framework for direct optimization of information
     retrieval measures. Information retrieval 13, 4 (2010), 375–397.
[32] Nils Reimers and Iryna Gurevych. 2019. Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks. In
     Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing. Association for Computational
     Linguistics.
[33] Stephen Robertson and Hugo Zaragoza. 2009. The Probabilistic Relevance Framework: BM25 and Beyond. Foundations
     and Trends in Information Retrieval 3, 4 (April 2009), 333–389.
[34] Stephen E. Robertson, Steve Walker, Susan Jones, Micheline Hancock-Beaulieu, and Mike Gatford. 1994. Okapi at
     TREC-3. In TREC (NIST Special Publication, Vol. 500-225). National Institute of Standards and Technology (NIST),
     109–126.
[35] Harrisen Scells, Shengyao Zhuang, and Guido Zuccon. 2022. Reduce, Reuse, Recycle: Green Information Retrieval
     Research. In Proceedings of the 45th International ACM SIGIR Conference on Research and Development in Information
     Retrieval (Madrid, Spain). 2825–2837.
[36] Tao Tao, Xuanhui Wang, Qiaozhu Mei, and ChengXiang Zhai. 2006. Language Model Information Retrieval with
     Document Expansion. In Proceedings of the Main Conference on Human Language Technology Conference of the North
     American Chapter of the Association of Computational Linguistics (New York, New York). 407–414.
[37] Nandan Thakur, Nils Reimers, Andreas Rücklé, Abhishek Srivastava, and Iryna Gurevych. 2021. BEIR: A Heterogeneous
     Benchmark for Zero-shot Evaluation of Information Retrieval Models. In Proceedings of the 35th Conference on Neural
     Information Processing Systems Datasets and Benchmarks Track (Round 2).
[38] Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N. Gomez, Łukasz Kaiser, and Illia
     Polosukhin. 2017. Attention is All You Need. In Proceedings of the 31st International Conference on Neural Information
     Processing Systems (Long Beach, California, USA). 6000–6010.
[39] Lidan Wang, Jimmy Lin, and Donald Metzler. 2011. A cascade ranking model for efficient ranked retrieval. In Proceedings
     of the 34th international ACM SIGIR conference on Research and development in Information Retrieval. ACM, 105–114.
[40] Shuai Wang, Shengyao Zhuang, and Guido Zuccon. 2021. BERT-Based Dense Retrievers Require Interpolation with
     BM25 for Effective Passage Retrieval. In Proceedings of the 2021 ACM SIGIR International Conference on Theory of
     Information Retrieval (Virtual Event, Canada). 317–324.
[41] Qiang Wu, Christopher J.C. Burges, Krysta M. Svore, and Jianfeng Gao. 2010. Adapting boosting for information
     retrieval measures. Information Retrieval (2010).
[42] Xiang Wu, Ruiqi Guo, David Simcha, Dave Dopson, and Sanjiv Kumar. 2019. Efficient Inner Product Approximation in
     Hybrid Spaces. (2019). arXiv:1903.08690 [cs.LG]
[43] Yonghui Wu, Mike Schuster, Zhifeng Chen, Quoc V. Le, Mohammad Norouzi, Wolfgang Macherey, Maxim Krikun,
     Yuan Cao, Qin Gao, Klaus Macherey, Jeff Klingner, Apurva Shah, Melvin Johnson, Xiaobing Liu, Łukasz Kaiser, Stephan
     Gouws, Yoshikiyo Kato, Taku Kudo, Hideto Kazawa, Keith Stevens, George Kurian, Nishant Patil, Wei Wang, Cliff
     Young, Jason Smith, Jason Riesa, Alex Rudnick, Oriol Vinyals, Greg Corrado, Macduff Hughes, and Jeffrey Dean.
     2016. Google’s Neural Machine Translation System: Bridging the Gap between Human and Machine Translation.
     arXiv:1609.08144 [cs.CL]
[44] Lee Xiong, Chenyan Xiong, Ye Li, Kwok-Fung Tang, Jialin Liu, Paul Bennett, Junaid Ahmed, and Arnold Overwijk. 2021.
     Approximate Nearest Neighbor Negative Contrastive Learning for Dense Text Retrieval. In International Conference on
     Learning Representations.
[45] Dawei Yin, Yuening Hu, Jiliang Tang, Tim Daly, Mianwei Zhou, Hua Ouyang, Jianhui Chen, Changsung Kang, Hongbo
     Deng, Chikashi Nobata, et al. 2016. Ranking relevance in yahoo search. In Proceedings of the 22nd ACM SIGKDD
28                                                                         Sebastian Bruch, Siyu Gai, and Amir Ingber


     International Conference on Knowledge Discovery and Data Mining. ACM, 323–332.
[46] Hamed Zamani, Mike Bendersky, Donald Metzler, Honglei Zhuang, and Marc Najork. 2022. Stochastic Retrieval-
     Conditioned Reranking. In Proceedings of the 2022 ACM SIGIR International Conference on the Theory of Information
     Retrieval (Madrid, Spain).
[47] Jingtao Zhan, Jiaxin Mao, Yiqun Liu, Min Zhang, and Shaoping Ma. 2020. RepBERT: Contextualized Text Embeddings
     for First-Stage Retrieval. arXiv:2006.15498 [cs.IR]
An Analysis of Fusion Functions for Hybrid Retrieval                                                        29


A    FUSION OF SPLADE AND BM25




                                                   (a) MS MARCO




                                                        (b) Quora




                                                       (c) HotpotQA




                                                         (d) FiQA

Fig. 13. Effect of normalization on 𝑓Convex = 𝛼 𝑓𝐴 + (1 − 𝛼)𝑓𝐵 , where 𝑓𝐴 is Splade and 𝑓𝐵 is BM25, as a
function of 𝛼 (left); and, the relative expansion rate of Splade scores with respect to BM25 scores (i.e., 𝜆 in
Definition 4.4), with 95% confidence intervals (right). 𝜙-𝑓𝑜 indicates that the normalization function 𝜙 was
only applied to 𝑓𝑜 , with the other function entering fusion without normalization.
30                                                                   Sebastian Bruch, Siyu Gai, and Amir Ingber


Table 5. NDCG@1000 (except SciFact and NFCorpus where cutoff is 100) on the test split of various
datasets for individual systems and their fusion using RRF [5] (𝜂 = 60) and TM2C2 (𝛼 = 0.8 in 𝑓Convex =
𝛼Splade + (1 − 𝛼)BM25). The symbols ‡ and ∗ indicate statistical significance (𝑝-value < 0.01) with respect
to TM2C2 and RRF respectively, according to a paired two-tailed 𝑡-test.

                                                          NDCG
                             Dataset       BM25      Splade     TM2C2       RRF
                           MS MARCO       0.309‡∗    0.508∗      0.507    0.444‡
                               NQ         0.382‡∗    0.591‡∗     0.587    0.520‡
                             Quora        0.798‡∗     0.853‡     0.876    0.859‡
                           NFCorpus       0.269‡∗     0.314∗     0.317    0.304‡
                           HotpotQA       0.682‡∗    0.727‡∗     0.751    0.737‡
                             FEVER        0.689‡∗    0.806‡∗     0.825    0.786‡
                            SciFact       0.698‡∗    0.723‡∗     0.740    0.732‡
                            DBPedia       0.415‡∗    0.546‡∗     0.556    0.526‡
                              FiQA        0.315‡∗     0.442∗     0.446    0.406‡




                      (a) in-domain                                   (b) out-of-domain

Fig. 14. The difference in NDCG@1000 of 𝑓SRRF and 𝑓RRF with 𝜂 = 60 (positive indicates better ranking quality
by SRRF) as a function of 𝛽.



B    FUSION OF TAS-B AND BM25
An Analysis of Fusion Functions for Hybrid Retrieval                                                            31




                                                   (a) MS MARCO




                                                        (b) Quora




                                                       (c) HotpotQA




                                                         (d) FiQA

Fig. 15. Effect of normalization on 𝑓Convex = 𝛼 𝑓𝐴 + (1 − 𝛼) 𝑓𝐵 , where 𝑓𝐴 is the Tas-B function and 𝑓𝐵 is BM25,
as a function of 𝛼 (left); and, the relative expansion rate of Tas-B scores with respect to BM25 scores (i.e., 𝜆 in
Definition 4.4), with 95% confidence intervals (right). 𝜙-𝑓𝑜 indicates that the normalization function 𝜙 was
only applied to 𝑓𝑜 , with the other function entering fusion without normalization.
32                                                                   Sebastian Bruch, Siyu Gai, and Amir Ingber


Table 6. NDCG@1000 (except SciFact and NFCorpus where cutoff is 100) on the test split of various datasets
for individual systems and their fusion using RRF [5] (𝜂 = 60) and M2C2 (𝛼 = 0.8 in 𝛼Tas-B+ (1−𝛼)BM25). The
symbols ‡ and ∗ indicate statistical significance (𝑝-value < 0.01) with respect to M2C2 and RRF respectively,
according to a paired two-tailed 𝑡-test.

                                                          NDCG
                             Dataset        BM25      Tas-B     M2C2        RRF
                           MS MARCO        0.309‡∗   0.477‡∗    0.486     0.434‡
                                NQ         0.382‡∗   0.522‡∗    0.552     0.513‡
                              Quora        0.798‡∗   0.856‡     0.881     0.860‡
                            NFCorpus       0.269‡∗   0.292‡     0.307      0.299
                            HotpotQA       0.682‡∗   0.631‡∗    0.702     0.711‡
                              FEVER        0.689‡∗   0.725‡∗    0.785     0.776‡
                             SciFact       0.698‡∗   0.670‡∗    0.715     0.719
                             DBPedia       0.415‡∗   0.495‡∗    0.533     0.512‡
                               FiQA        0.315‡∗   0.396‡∗    0.422     0.401‡




                      (a) in-domain                                     (b) out-of-domain

Fig. 16. The difference in NDCG@1000 of 𝑓SRRF and 𝑓RRF with 𝜂 = 60 (positive indicates better ranking quality
by SRRF) as a function of 𝛽.
An Analysis of Fusion Functions for Hybrid Retrieval                                                           33


C    FUSION OF TAS-B AND SPLADE




                                                   (a) MS MARCO




                                                        (b) Quora




                                                       (c) HotpotQA




                                                         (d) FiQA

Fig. 17. Effect of normalization on 𝑓Convex = 𝛼 𝑓𝐴 + (1 − 𝛼) 𝑓𝐵 , where 𝑓𝐴 is the Tas-B function and 𝑓𝐵 is Splade,
as a function of 𝛼 (left); and, the relative expansion rate of Tas-B scores with respect to Splade scores (i.e., 𝜆
in Definition 4.4), with 95% confidence intervals (right). 𝜙-𝑓𝑜 indicates that the normalization function 𝜙 was
only applied to 𝑓𝑜 , with the other function entering fusion without normalization.
34                                                                   Sebastian Bruch, Siyu Gai, and Amir Ingber


Table 7. NDCG@1000 (except SciFact and NFCorpus where cutoff is 100) on the test split of various datasets
for individual systems and their fusion using RRF [5] (𝜂 = 60) and M2C2 (𝛼 = 0.2 in 𝛼Tas-B+(1−𝛼)Splade). The
symbols ‡ and ∗ indicate statistical significance (𝑝-value < 0.01) with respect to M2C2 and RRF respectively,
according to a paired two-tailed 𝑡-test.

                                                          NDCG
                              Dataset      Splade     Tas-B     M2C2       RRF
                            MS MARCO        0.508    0.477‡∗    0.512 0.504‡
                                NQ         0.589     0.522‡∗    0.593     0.581‡
                              Quora        0.853      0.856     0.859     0.857
                            NFCorpus       0.313     0.292‡∗    0.318     0.314
                            HotpotQA       0.727∗    0.631‡∗    0.728     0.686‡
                              FEVER        0.806∗    0.725‡∗    0.811     0.795‡
                             SciFact       0.723∗    0.670‡∗    0.730     0.709‡
                             DBPedia       0.546‡    0.495‡∗    0.555     0.545‡
                               FiQA        0.442‡    0.396‡∗    0.453     0.440‡




                      (a) in-domain                                     (b) out-of-domain

Fig. 18. The difference in NDCG@1000 of 𝑓SRRF and 𝑓RRF with 𝜂 = 60 (positive indicates better ranking quality
by SRRF) as a function of 𝛽.



D    FUSION OF TAS-B AND ALL-MINILM-L6-V2
An Analysis of Fusion Functions for Hybrid Retrieval                                                         35




                                                   (a) MS MARCO




                                                        (b) Quora




                                                       (c) HotpotQA




                                                         (d) FiQA

Fig. 19. Effect of normalization on 𝑓Convex = 𝛼 𝑓𝐴 + (1 − 𝛼) 𝑓𝐵 , where 𝑓𝐴 is Tas-B and 𝑓𝐵 is All-MiniLM-l6-v2,
as a function of 𝛼 (left); and, the relative expansion rate of Tas-B scores with respect to All-MiniLM-l6-v2
scores (i.e., 𝜆 in Definition 4.4), with 95% confidence intervals (right). 𝜙-𝑓𝑜 indicates that the normalization
function 𝜙 was only applied to 𝑓𝑜 , with the other function entering fusion without normalization.
36                                                                   Sebastian Bruch, Siyu Gai, and Amir Ingber


Table 8. NDCG@1000 (except SciFact and NFCorpus where cutoff is 100) on the test split of various
datasets for individual systems and their fusion using RRF [5] (𝜂 = 60) and M2C2 (𝛼 = 0.8 in 𝛼Tas-B + (1 −
𝛼)All-MiniLM-l6-v2). The symbols ‡ and ∗ indicate statistical significance (𝑝-value < 0.01) with respect to
M2C2 and RRF respectively, according to a paired two-tailed 𝑡-test.

                                                          NDCG
                       Dataset        All-MiniLM-l6-v2      Tas-B     M2C2       RRF
                     MS MARCO             0.441‡∗           0.477‡    0.483     0.474‡
                          NQ              0.505‡∗          0.522‡∗    0.547 0.550
                        Quora             0.889‡∗           0.856‡    0.872 0.877
                      NFCorpus            0.296‡∗          0.292‡∗    0.307 0.316‡
                      HotpotQA            0.520‡∗          0.631‡∗    0.646 0.610‡
                        FEVER             0.558‡∗           0.725∗    0.730 0.669‡
                       SciFact            0.681‡∗          0.670‡∗    0.704 0.712
                       DBPedia            0.425‡∗           0.495‡    0.510 0.496‡
                         FiQA             0.467‡           0.396‡∗    0.438 0.467‡




                      (a) in-domain                                   (b) out-of-domain

Fig. 20. The difference in NDCG@1000 of 𝑓SRRF and 𝑓RRF with 𝜂 = 60 (positive indicates better ranking quality
by SRRF) as a function of 𝛽.
