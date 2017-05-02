from pipeline import Pipeline
p = Pipeline('../data/data.json')
X, y = p.get_matrix_target()
model = p.get_model(X, y)
p.save_model(model, '../data/saved-model')
