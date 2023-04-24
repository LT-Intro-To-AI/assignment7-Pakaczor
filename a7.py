from neural import NeuralNet
import os
os.system('cls')
xor_training_data = [([1, 1], [0]), ([1, 0], [1]), ([0, 1], [1]), ([0, 0], [0])]

xorn = NeuralNet(2, 10, 1)
xorn.train(xor_training_data)

print('\nTraining Voter Opinion\n')

voter_opinion = [([0.9,0.6,0.8,0.3,0.1],[1.0]),
    ([0.8,0.8,0.4,0.6,0.4],[1.0]),
    ([0.7,0.2,0.4,0.6,0.3],[1.0]),
    ([0.5,0.5,0.8,0.4,0.8],[0.0]),
    ([0.3,0.1,0.6,0.8,0.8],[0.0]),
    ([0.6,0.3,0.4,0.3,0.6],[0.0])]

pie = NeuralNet(5,10,1)
pie.train(voter_opinion)

test_data = [
    [1,1,1,.1,.1],
    [.5,.2,.1,.7,.7],
    [.8,.3,.3,.3,.8],
    [.8,.3,.3,.8,.3],
    [.9,.8,.8,.3,.6]
]

for x in range(5):
    if float(von.evaluate(test_data[x])[0]) > 0.5:
        print(f'case {x+1}: {test_data[x]} is 1')
    if float(von.evaluate(test_data[x])[0]) < 0.5:
        print(f'case {x+1}: {test_data[x]} is 0')
