class Perceptron:
    def __init__(self, learning_rate = 0.1, num_inputs = 4):
        self.learning_rate = 0.1
        self.weights = [0 for _ in range(num_inputs)]
        self.bias = 0
        
    def activation(self, input_vector):
        return 1 if sum([w * v for w, v in zip(self.weights, input_vector)]) + self.bias > 0 else -1
    
    def train(self, data, epochs = 10):   
        
        for _ in range(epochs):
            for dp in data:
                prediction = self.activation(dp[:4])
                loss = dp[4] - prediction
                self.weights = [w + self.learning_rate * loss * v for w, v in zip(self.weights, dp[:4])]
                self.bias += self.learning_rate * loss
                
                
def main():
    with open("iris.csv", "r") as f:
        data = f.readlines()
        data = [d.replace("Iris-setosa", "-1").replace("Iris-versicolor", "1") for d in data]
        data = [d.strip().split(",") for d in data]
        data = [[float(v) for v in d] for d in data]
        
    perceptron = Perceptron()
    
    test_set = data[45:50] + data[95:100]
    training_set = data[:45] + data[50:95]
    
    perceptron.train(training_set)
    
    print(f"Trained Weights: {perceptron.weights} | Bias weight: {perceptron.bias}")
    
    print("Test Set: ")
    for dp in test_set:
        prediction = perceptron.activation(dp[:4])
        print(f"Predicted: {prediction} | Actual: {dp[4]}")
    
    import matplotlib.pyplot as plt
    plt.scatter([d[1] for d in data[:50]], [d[2] for d in data[:50]], color="red", marker="x" ,label="Iris-setosa")
    plt.scatter([d[1] for d in data[50:100]], [d[2] for d in data[50:100]], color="blue", label="Iris-versicolor")
    plt.xlabel("Sepal Width")
    plt.ylabel("Petal Length")
    
    slope = (-(perceptron.bias)/(perceptron.weights[2])) / ((perceptron.bias)/(perceptron.weights[1]))
    plt.plot([2, 5], [slope * x + (-perceptron.bias / perceptron.weights[2]) for x in (2, 5)], label='Decision Boundary', color='black')
    plt.legend()
    plt.show()
    

main()