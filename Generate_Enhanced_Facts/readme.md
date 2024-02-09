
Generate Enhance Facts “To generate enhance facts from the given sentence”

Proposed Methodology:

For the generation of enhanced facts at the beginning I was using a Natural Language tool kit like tokenization and lemmatizer by which I was able to get the root word and then I can modify it to its similar meaning but that was far away from the expected result because we have to enhance the fact not to paraphrase the sentence: Here is the code snippet to get the root word of any word: word = "swimming" lemma = lemmatizer.lemmatize(word, pos='v') # 'v' indicates verb print(f"Original Word: {word}, Lemma: {lemma}")

Used PorterStremmer to stem the word porter_stemmer=PorterStemmer() words=['Amazing','Happily','Playing','Singing'] stem_word=[porter_stemmer.stem(word) for word in words] print("Oringial word", words) print("Stemmed word",stem_word)

Oringial word ['Amazing', 'Happily', 'Playing', 'Singing'] Stemmed word ['amaz', 'happili', 'play', 'sing']

Used WordNetLemmatizer to generate synonyms of the word:

from nltk.stem import WordNetLemmatizer

Create a WordNetLemmatizer object
lemmatizer = WordNetLemmatizer()

Example usage
word = "better" lemma = lemmatizer.lemmatize(word, pos='a') print(f"Original Word: {word}, Lemma: {lemma}")

Original Word: better, Lemma: good

But this way I was only able to paraphrase the sentence, so I got to understand that either we have to give internal knowledge embedded in the input text or we have to use external knowledge from outside sources such as knowledge base and knowledge graph in the text generation system

Analysis: I have researched for AI tools that can perform the same task other than Open AI and Google Bard for free, I have encountered one tool that was free but for limited access Tool is: https://deepai.org/chat/text-generator Prompt:- Loan taken from Bank Response:- A loan obtained from a financial institution, such as a bank, is a financial product that provides an individual or business with access to funds for various purposes. This type of loan typically involves repayment of principal and interest over an agreed-upon period, with interest rates and fees varying depending on the loan terms and the borrower's creditworthiness. Loans from banks can be used for various purposes, such as purchasing a home, starting a business, or covering unexpected expenses.

Result

By Using Lamini-Flan-T5-248M

For text to text generation classifier =pipeline(task="text2text-generation",model="MBZUAI/LaMini-Flan-T5-248M")

Fact: Loan pending with bank [{'generated_text': 'A Loan pending with bank'}]

Fact: Physical or Mental Torture [{'generated_text': 'Physical Torture: a physical discomfort or discomfort caused by physical or mental stress. Mental Tor'}]

Fact: "The accused did not create or submit forged documents to the authority." [{'generated_text': 'The accused did not submit forged documents to the authority.'}]

References: https://deepai.org/chat/text-generator https://huggingface.co/models?other=instruction+fine-tuning https://huggingface.co/tasks/text-generation https://youtu.be/CDmPBsZ09wg?si=IAvuFyD0tz_1Om8E Google Bard Chat GPT
