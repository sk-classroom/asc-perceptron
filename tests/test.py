import unittest
import numpy as np


class TestPerceptron(unittest.TestCase):
    def setUp(self):
        self.p = Perceptron(eta=1e-2, n_iter=100)
        # Generate 10 linearly separable points
        self.X = np.array([[i, i + 1] for i in range(1, 11)])
        self.y = np.array([1 if i <= 5 else 0 for i in range(1, 11)])

    def test_fit(self):
        self.p.fit(self.X, self.y)
        self.assertIsNotNone(self.p.w_)
        self.assertIsNotNone(self.p.b_)

    def test_predict(self):
        prediction = self.p.predict([[-1, -1], [20, 20]])
        self.assertEqual(len(prediction), 2)
        self.assertIn(prediction, [1, 0])
        self.assertAlmostEqual(prediction[0], 1)
        self.assertAlmostEqual(prediction[1], 0)


if __name__ == "__main__":
    unittest.main()
