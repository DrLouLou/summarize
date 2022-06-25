from app import app
from flask import render_template
import cohere
import time
# import pandas as pd
api_key = 'VQQattBOwmpc16qSuIqlMTn71XPCUWqKrcP9hDus'
co = cohere.Client(api_key, '2021-11-08')

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/summarize')
def summarize():
    prompt = 'In 1754 Jean-Jacques Rousseau, at the comfortable age of 42, was composing a monograph for an essay contest not dissimilar to this one. Hosted by a local university, the prompt for the contest was "What is the origin of inequality among people, and is it authorized by natural law?” His submission, Discourse on the Origin and Basis of Inequality Among Men, became an intellectual sensation. In its long life as one of the foundational documents of the Western world it has been, at times, blamed for the bloody slaughter of The Terror, and, at other times, lauded as the inventor of the progressive Left. In summary, '
    # n_generations = 5
    prediction = co.generate(
    model='large',
    prompt=prompt,
    return_likelihoods = 'GENERATION',
    stop_sequences=['"'],
    max_tokens=50,
    temperature=0.7,
    # num_generations=n_generations,
    k=0,
    p=0.75)
    gens = []
    likelihoods = []
    for gen in prediction.generations:
        gens.append(gen.text)
        
        sum_likelihood = 0
        for t in gen.token_likelihoods:
            sum_likelihood += t.likelihood
        # Get sum of likelihoods
        likelihoods.append(sum_likelihood)

    # pd.options.display.max_colwidth = 200
    # # Create a dataframe for the generated sentences and their likelihood scores
    # df = pd.DataFrame({'generation':gens, 'likelihood': likelihoods})
    # # Drop duplicates
    # df = df.drop_duplicates(subset=['generation'])
    # # Sort by highest sum likelihood
    # df = df.sort_values('likelihood', ascending=False, ignore_index=True)
    # print(df)

    # print(gens[0])
    return render_template('summarize.html', gens=gens)
