import pickle


with open('CodeRL_copy/train/test_results/987.pkl', 'rb') as f:
    data = pickle.load(f)
    print(data)