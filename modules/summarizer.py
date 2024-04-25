from transformers import pipeline

def summarize_article(article, max_length=200, min_length=100):
	
	#initialize the pipeline for summarization
	pipe = pipeline("summarization", model="./models/bart-large-cnn")

	#summarize the article
	summary = pipe(article, max_length=max_length, min_length=min_length, do_sample=False)
	summarized_article = summary[0]['summary_text']
	summarized_article_list_of_sentences = split_into_sentences(summarized_article)
	return summarized_article, summarized_article_list_of_sentences

if __name__ == "__main__":
	pass

def split_into_sentences(text):
    sentences = text.split('. ')
    # If the last sentence doesn't end with a '.', add it to the list
    if sentences[-1] and not sentences[-1].endswith('.'):
        sentences[-1] += '.'
    return sentences