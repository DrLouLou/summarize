from app import app
from flask import render_template, request
from app.forms import SummarizeForm
import cohere

# import pandas as pd
api_key = 'VQQattBOwmpc16qSuIqlMTn71XPCUWqKrcP9hDus'
co = cohere.Client(api_key, '2021-11-08')

@app.route('/')
@app.route('/index', methods=["GET", "POST"])
def index():
    message = 'please enter a prompt'
    if request.method == "POST":
        form = SummarizeForm(request.form)
        if form.validate_on_submit():
            prompt = form.prompt.data + " In summary, "
            # n_generations = 5
            prediction = co.generate(
            model='large',
            prompt=prompt,
            return_likelihoods = 'GENERATION',
            stop_sequences=['.'],
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
            return render_template('index.html', form=form, gens=gens)
        else:
            message = "Please enter a valid prompt"
            
    form = SummarizeForm()
    return render_template('index.html', form=form, message=message)

def isCorrectLength(prompt):
    words = prompt.split(" ")
    if 1<len(words)<300:
        return True
    else:
        return False
