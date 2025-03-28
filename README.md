# Convert pdfs to markdown

This has the methods we use to convert selected .pdfs to markdown. The process is part of making RAG applications and context for llms'. We do not handle 1'000s of pdfs. We have a person who
does literature review, sometimes two people. Once they select an article they convert it to markdown and review the converted text. They check for the following:

1. Stray characters
2. Repeated headers and footers
3. Remove the references
4. Check the order of the paragraphs, the two column format does not always work
5. Check the order of the markdown headers #, ##, ###

This has given us real good results with plain vector search and reduces the space needed in our vector store. This expands the task of literature review but adds confidence in our applications.

Not meant to replace packages like unstructured or other automated versions. 
