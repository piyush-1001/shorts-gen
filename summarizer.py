from transformers import pipeline
import torch

def summarize_article(article, max_length=200, min_length=100):
	
	#initialize the pipeline for summarization
	pipe = pipeline("summarization", model="bart-large-cnn")

	#summarize the article
	summary = pipe(article, max_length=max_length, min_length=min_length, do_sample=False)
	summarized_article = summary[0]['summary_text']
	return summarized_article

if __name__ == "__main__":
	pass
