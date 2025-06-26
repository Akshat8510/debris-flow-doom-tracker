from sklearn.ensemble import RandomForestClassifier
from utils import load_raster

# Load example data
rain = np.load('data/rain.npy')  # Simulated
elev = np.load('data/elevation.npy')
ndvi = np.load('data/ndvi.npy')

X = np.stack([rain.ravel(), elev.ravel(), ndvi.ravel()], axis=1)
y = np.load('data/labels.npy').ravel()

clf = RandomForestClassifier()
clf.fit(X, y)
