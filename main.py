from summarizer import summarize_article
from text_to_speech import text_to_speech_files
from movie_maker import create_video

# hard coded article for now
article = """The opening minutes of Train to the End of the World left me with a strong initial impression — it seemed like a wacky, zany comedy series that doesn’t take itself too seriously. As someone with an interest in trains and train-related media (yes, super specific, I know), the title of this anime immediately caught my attention. A train to the end of the world? Is it ominous? Or is it a heart-warming travel tale about a group of girls going on a journey to a distant destination? Perhaps it’s the former cloaked within the guise of a wholesome travel story? The myriad questions swirling in my mind intrigued me greatly. In today’s landscape saturated with overly-familiar isekai anime and fantasy stories done to death, standing out from the crowd, that too as an original anime, is no small feat. So here’s the gist: In the town of Agano, when residents hit the ripe age of 21 years and three months, they undergo a bizarre transformation into talking animals. This transformation isn’t voluntary, and they have no say in which animal they’ll become. This curious phenomenon traces back to what’s known as “the 7G incident.” It’s the seventh generation of broadband cellular network technology but takes it a step further, delving into the human mind and seemingly linking individuals together, forming a peculiar network. So, how does this tie into taking a journey to the end of the world? Well, following the activation of 7G, the distances between train stations and towns expanded to impossible lengths due to the physics-defying consequences of the technology, reshaping the world and its inhabitants. And as it turns out, there’s a chance to halt this transformation by venturing to Ikebukuro, where the creator of 7G, and a friend to the four main characters, was last seen. And thus, their journey begins! I should also mention that the anime was announced in commemoration of the 150th anniversary of Japan’s first railway. This suggests that it will serve as one of those promotional anime pieces highlighting the cultural heritage of the country. Fortunately, it goes beyond the typical slice-of-life genre, adding a unique premise."""

#get a list of sentences of summary
summarized_article, summarized_article_list_of_sentences = summarize_article(article)
print(summarized_article_list_of_sentences)

# test to speech
saved_audio_files = text_to_speech_files(summarized_article_list_of_sentences)

print("Audio files saved at the following locations:")
for file_path in saved_audio_files:
    print(file_path)

# movie generation
create_video(summarized_article_list_of_sentences)