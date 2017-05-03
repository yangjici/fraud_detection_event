from pipeline import Pipeline
import cPickle as pickle

# p = Pipeline('../data/data.json')
# X, y = p.get_X_y()
# model = p.train(X, y)

# with open('model.p', 'w') as f:
#     pickle.dump(model, f)

with open('model.p') as f:
    m = pickle.load(f)
