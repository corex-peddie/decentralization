from joblib import load

def model_prediction():
    # Loading the model
    model = load('model_file.joblib')

    # Last week's website data 
    prior_week_data = [710, 500, 454, 250]

    new_users = int(model.predict([[710, 500]])[0][0])
    returning_users = int(model.predict([[710, 500]])[0][1])

    return {'New Users (Predicted)': new_users, 'Returning Users (Predicted)': returning_users}

